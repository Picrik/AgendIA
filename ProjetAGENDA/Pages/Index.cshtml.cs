using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using ProjetAGENDA.Models;
using ProjetAGENDA.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetAGENDA.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;
        public JsonFileEventsService EventsService;
        public IEnumerable<CalendarEvent> Events { get; private set; }

        public IndexModel(ILogger<IndexModel> logger,JsonFileEventsService eventsService)
        {
            _logger = logger;
            EventsService = eventsService;
        }

        public void OnGet()
        {
            Events = EventsService.GetEvents(HttpContext.User.Identity.Name+".json");
        }
    }
}
