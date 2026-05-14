using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PowerChordAPI.Data;
using PowerChordAPI.Models;
using System.Security.Claims;

namespace PowerChordAPI.Controllers;

[ApiController]
[Route("api/[controller]")]
public class TicketController : ControllerBase
{
    private readonly ApiContext _context;
    private readonly IHttpClientFactory _httpClientFactory;

    public TicketController(ApiContext context, IHttpClientFactory httpClientFactory)
    {
        _context = context;
        _httpClientFactory = httpClientFactory;
    }

    [Authorize]
    [HttpPost]
    public async Task<IActionResult> BuyTicket(Ticket ticket)
    {
        if (ticket.Quantity <= 0)
            return BadRequest("A quantidade deve ser superior a zero.");

        var concert = await _context.Concerts.FindAsync(ticket.ConcertId);

        if (concert == null)
            return BadRequest("Concerto não existe.");

        try
        {
            var client = _httpClientFactory.CreateClient("payments");
            var response = await client.PostAsync("/payments", null);

            if (!response.IsSuccessStatusCode)
                return StatusCode(500, "Pagamento falhou.");
        }
        catch
        {
            return StatusCode(500, "Serviço de pagamento indisponível.");
        }

        ticket.UserId = User.FindFirstValue(ClaimTypes.NameIdentifier) ?? ticket.UserId;

        _context.Tickets.Add(ticket);
        await _context.SaveChangesAsync();

        return CreatedAtAction(nameof(GetTicketById), new { id = ticket.Id }, ticket);
    }

    [Authorize]
    [HttpGet]
    public async Task<IActionResult> GetTickets()
    {
        return Ok(await _context.Tickets.AsNoTracking().ToListAsync());
    }

    [Authorize]
    [HttpGet("{id:int}")]
    public async Task<IActionResult> GetTicketById(int id)
    {
        var ticket = await _context.Tickets.AsNoTracking().FirstOrDefaultAsync(t => t.Id == id);

        if (ticket == null)
            return NotFound("Bilhete não encontrado.");

        return Ok(ticket);
    }

    [Authorize]
    [HttpDelete("{id:int}")]
    public async Task<IActionResult> DeleteTicket(int id)
    {
        var ticket = await _context.Tickets.FindAsync(id);

        if (ticket == null)
            return NotFound("Bilhete não encontrado.");

        _context.Tickets.Remove(ticket);
        await _context.SaveChangesAsync();

        return Ok("Bilhete apagado com sucesso.");
    }
}
