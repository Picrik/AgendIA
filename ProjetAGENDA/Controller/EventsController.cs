using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using ProjetAGENDA.Models;
using ProjetAGENDA.Services;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetAGENDA.Controller
{
    [Route("[controller]")]
    [ApiController]
    public class EventsController : ControllerBase
    {
        public EventsController(JsonFileEventsService eventsService)
        {
            this.EventsService = eventsService;
        }

        public JsonFileEventsService EventsService { get; }

        [HttpGet]
        public IEnumerable<CalendarEvent> Get()
        {
            return EventsService.GetEvents(HttpContext.User.Identity.Name+".json");
        }

        //[HttpPatch] "[FromBody]"
        [Route("AddEvent")]
        [HttpGet]
        public ActionResult Get(
            [FromQuery]string PersonId,
            [FromQuery]string Maker,
            [FromQuery]string StartDateTime,
            [FromQuery]string EndDateTime,
            [FromQuery]string Subject)
        {
            EventsService.AddEvent(PersonId, new NewCalendarEvent(PersonId,Maker,StartDateTime,EndDateTime,Subject));
            return Ok();
        }
    }
}
