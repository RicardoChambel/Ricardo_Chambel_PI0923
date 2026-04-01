using Microsoft.AspNetCore.Mvc;
using RicardoIvanAPI.Data;
using System.Net.Http;

namespace RicardoIvanAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class RicardoController : ControllerBase
    {
        private readonly ApiContext _context;
        private readonly IHttpClientFactory _clientFactory;

        public RicardoController(ApiContext context, IHttpClientFactory clientFactory)
        {
            _context = context;
            _clientFactory = clientFactory;
        }

        [HttpGet("request-mountebank")]
        public async Task<IActionResult> GetFromMountebank()
        {
            var client = _clientFactory.CreateClient();

            string url = "http://localhost:2525";

            try
            {
                var response = await client.GetAsync(url);
                if (response.IsSuccessStatusCode)
                {
                    var content = await response.Content.ReadAsStringAsync();
                    return Ok(new { msg = "Lido do Mountebank!", dados = content });
                }
                return BadRequest("Mountebank offline ou porta errada.");
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Erro: {ex.Message}");
            }
        }
    }
}