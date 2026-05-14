using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Caching.Memory;
using Newtonsoft.Json;
using PowerChordAPI.Data;
using PowerChordAPI.Models;
using StackExchange.Redis;

namespace PowerChordAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ConcertController : ControllerBase
{
    private const string ConcertsCacheKey = "concerts";

    private readonly ApiContext _context;
    private readonly IConnectionMultiplexer _redis;
    private readonly IMemoryCache _memoryCache;

    public ConcertController(ApiContext context, IConnectionMultiplexer redis, IMemoryCache memoryCache)
    {
        _context = context;
        _redis = redis;
        _memoryCache = memoryCache;
    }

    [HttpGet]
    public async Task<IActionResult> GetConcerts()
    {
        if (_memoryCache.TryGetValue(ConcertsCacheKey, out List<Concert>? localConcerts))
            return Ok(localConcerts);

        try
        {
            if (_redis.IsConnected)
            {
                var cache = _redis.GetDatabase();
                var cached = await cache.StringGetAsync(ConcertsCacheKey);

                if (!cached.IsNullOrEmpty)
                {
                    var redisConcerts = JsonConvert.DeserializeObject<List<Concert>>(cached!) ?? new List<Concert>();
                    _memoryCache.Set(ConcertsCacheKey, redisConcerts, TimeSpan.FromSeconds(60));
                    return Ok(redisConcerts);
                }
            }
        }
        catch
        {
            // Se Redis falhar, continua pela base de dados.
        }

        var concertsFromDb = await _context.Concerts.AsNoTracking().ToListAsync();

        _memoryCache.Set(ConcertsCacheKey, concertsFromDb, TimeSpan.FromSeconds(60));

        try
        {
            if (_redis.IsConnected)
            {
                var cache = _redis.GetDatabase();
                await cache.StringSetAsync(
                    ConcertsCacheKey,
                    JsonConvert.SerializeObject(concertsFromDb),
                    TimeSpan.FromMinutes(5)
                );
            }
        }
        catch { }

        return Ok(concertsFromDb);
    }

    [HttpGet("{id:int}")]
    public async Task<IActionResult> GetConcertById(int id)
    {
        var concert = await _context.Concerts.AsNoTracking().FirstOrDefaultAsync(c => c.Id == id);

        if (concert == null)
            return NotFound("Concerto não encontrado.");

        return Ok(concert);
    }

    [Authorize]
    [HttpPost]
    public async Task<IActionResult> CreateConcert(Concert concert)
    {
        _context.Concerts.Add(concert);
        await _context.SaveChangesAsync();
        await ClearConcertCache();

        return CreatedAtAction(nameof(GetConcertById), new { id = concert.Id }, concert);
    }

    [Authorize]
    [HttpPut("{id:int}")]
    public async Task<IActionResult> UpdateConcert(int id, Concert updatedConcert)
    {
        var concert = await _context.Concerts.FindAsync(id);

        if (concert == null)
            return NotFound("Concerto não encontrado.");

        concert.Name = updatedConcert.Name;
        concert.Location = updatedConcert.Location;
        concert.Date = updatedConcert.Date;
        concert.Price = updatedConcert.Price;

        await _context.SaveChangesAsync();
        await ClearConcertCache();

        return Ok(concert);
    }

    [Authorize]
    [HttpDelete("{id:int}")]
    public async Task<IActionResult> DeleteConcert(int id)
    {
        var concert = await _context.Concerts.FindAsync(id);

        if (concert == null)
            return NotFound("Concerto não encontrado.");

        _context.Concerts.Remove(concert);
        await _context.SaveChangesAsync();
        await ClearConcertCache();

        return Ok("Concerto apagado com sucesso.");
    }

    private async Task ClearConcertCache()
    {
        _memoryCache.Remove(ConcertsCacheKey);

        try
        {
            if (_redis.IsConnected)
            {
                var cache = _redis.GetDatabase();
                await cache.KeyDeleteAsync(ConcertsCacheKey);
            }
        }
        catch { }
    }
}
