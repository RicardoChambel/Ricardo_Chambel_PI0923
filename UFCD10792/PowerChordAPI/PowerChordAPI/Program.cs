using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using Polly;
using PowerChordAPI.Data;
using PowerChordAPI.Models;
using PowerChordAPI.Services;
using StackExchange.Redis;
using System.Text;

var builder = WebApplication.CreateBuilder(args);

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");

builder.Services.AddDbContext<ApiContext>(options =>
{
    if (!string.IsNullOrWhiteSpace(connectionString))
    {
        options.UseSqlServer(connectionString);
    }
    else
    {
        options.UseInMemoryDatabase("PowerChordDB");
    }
});

builder.Services.AddControllers();
builder.Services.AddMemoryCache();

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowFrontend", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new Microsoft.OpenApi.Models.OpenApiInfo
    {
        Title = "PowerChordAPI",
        Version = "v1",
        Description = "API REST para gestão de concertos e venda de bilhetes da banda Power Chord."
    });

    options.AddSecurityDefinition("Bearer", new Microsoft.OpenApi.Models.OpenApiSecurityScheme
    {
        Name = "Authorization",
        Type = Microsoft.OpenApi.Models.SecuritySchemeType.Http,
        Scheme = "Bearer",
        BearerFormat = "JWT",
        In = Microsoft.OpenApi.Models.ParameterLocation.Header,
        Description = "Insere o token JWT no formato: Bearer {token}"
    });

    options.AddSecurityRequirement(new Microsoft.OpenApi.Models.OpenApiSecurityRequirement
    {
        {
            new Microsoft.OpenApi.Models.OpenApiSecurityScheme
            {
                Reference = new Microsoft.OpenApi.Models.OpenApiReference
                {
                    Type = Microsoft.OpenApi.Models.ReferenceType.SecurityScheme,
                    Id = "Bearer"
                }
            },
            Array.Empty<string>()
        }
    });
});

var redisConnectionString = builder.Configuration["Redis:ConnectionString"] ?? "localhost:6379,abortConnect=false";
builder.Services.AddSingleton<IConnectionMultiplexer>(_ =>
    ConnectionMultiplexer.Connect(redisConnectionString));

var paymentsBaseUrl = builder.Configuration["ExternalServices:PaymentsBaseUrl"] ?? "http://localhost:3000";

builder.Services.AddHttpClient("payments", client =>
    {
        client.BaseAddress = new Uri(paymentsBaseUrl);
    })
    .AddPolicyHandler(
        Policy<HttpResponseMessage>
            .Handle<HttpRequestException>()
            .OrResult(response => !response.IsSuccessStatusCode)
            .RetryAsync(3)
    )
    .AddPolicyHandler(
        Policy<HttpResponseMessage>
            .Handle<HttpRequestException>()
            .OrResult(response => !response.IsSuccessStatusCode)
            .CircuitBreakerAsync(2, TimeSpan.FromSeconds(30))
    );

var jwtKey = builder.Configuration["Jwt:Key"];
if (string.IsNullOrWhiteSpace(jwtKey) || jwtKey.Length < 32)
{
    throw new InvalidOperationException("Configura Jwt:Key com pelo menos 32 caracteres em appsettings.json, .env ou variável de ambiente.");
}

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = builder.Configuration["Jwt:Issuer"],
            ValidAudience = builder.Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(jwtKey))
        };
    });

builder.Services.AddAuthorization();

var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<ApiContext>();

    for (var attempt = 1; attempt <= 10; attempt++)
    {
        try
        {
            db.Database.EnsureCreated();
            break;
        }
        catch when (attempt < 10)
        {
            await Task.Delay(TimeSpan.FromSeconds(5));
        }
    }

    if (!db.Concerts.Any())
    {
        db.Concerts.AddRange(
            new Concert { Name = "Power Chord Live", Location = "Lisboa", Date = new DateTime(2026, 6, 1, 21, 0, 0), Price = 25 },
            new Concert { Name = "Power Chord Rock Night", Location = "Porto", Date = new DateTime(2026, 7, 15, 22, 0, 0), Price = 30 },
            new Concert { Name = "Power Chord Summer Tour", Location = "Coimbra", Date = new DateTime(2026, 8, 10, 20, 30, 0), Price = 20 }
        );
    }

    if (!db.Users.Any(u => u.Email == "admin@powerchord.com"))
    {
        db.Users.Add(new User
        {
            Email = "admin@powerchord.com",
            PasswordHash = PasswordService.HashPassword("123456")
        });
    }

    db.SaveChanges();
}

app.UseSwagger();
app.UseSwaggerUI();

app.UseHttpsRedirection();
app.UseCors("AllowFrontend");

app.UseAuthentication();
app.UseAuthorization();

app.MapControllers();
app.MapGet("/health", () => Results.Ok(new { status = "ok", service = "PowerChordAPI" }));

app.Run();

public partial class Program { }
