using Microsoft.EntityFrameworkCore;
using RicardoIvanAPI.Models;
using System.Collections.Generic;

namespace RicardoIvanAPI.Data
{
    public class ApiContext : DbContext
    {
        public ApiContext(DbContextOptions<ApiContext> options) : base(options) { }
        public DbSet<Item> Items { get; set; }
    }
}