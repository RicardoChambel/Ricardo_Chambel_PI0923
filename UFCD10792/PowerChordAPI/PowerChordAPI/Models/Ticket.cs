namespace PowerChordAPI.Models;

public class Ticket
{
    public int Id { get; set; }
    public string UserId { get; set; } = string.Empty;
    public int ConcertId { get; set; }
    public int Quantity { get; set; }
}