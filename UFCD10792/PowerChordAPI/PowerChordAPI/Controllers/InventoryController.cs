using Microsoft.AspNetCore.Mvc;

namespace PowerChordAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class InventoryController : ControllerBase
{
    private readonly IHttpClientFactory _httpClientFactory;

    public InventoryController(IHttpClientFactory httpClientFactory)
    {
        _httpClientFactory = httpClientFactory;
    }

    [HttpGet("{sku}")]
    public async Task<IActionResult> GetInventory(string sku)
    {
        try
        {
            var client = _httpClientFactory.CreateClient("payments");
            var response = await client.GetAsync($"/inventory/{sku}");
            var body = await response.Content.ReadAsStringAsync();

            if (!response.IsSuccessStatusCode)
                return StatusCode((int)response.StatusCode, body);

            return Content(body, "application/json");
        }
        catch
        {
            return StatusCode(500, "Serviço de inventário indisponível.");
        }
    }
}
