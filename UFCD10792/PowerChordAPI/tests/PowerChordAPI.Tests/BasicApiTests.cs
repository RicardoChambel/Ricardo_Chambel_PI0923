using Microsoft.AspNetCore.Mvc.Testing;
using System.Net;
using Xunit;

namespace PowerChordAPI.Tests;

public class BasicApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public BasicApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task Health_ReturnsOk()
    {
        var response = await _client.GetAsync("/health");
        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    }

    [Fact]
    public async Task Concerts_ReturnsOk()
    {
        var response = await _client.GetAsync("/api/concert");
        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    }
}
