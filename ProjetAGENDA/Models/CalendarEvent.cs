using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Text.Json;
namespace ProjetAGENDA.Models
{
    public class CalendarEvent
    {
        public string Id { get; set; }

        public string Maker { get; set; }

        //Informations about the Event
        
        public string StartDateTime { get; set; }

        public string EndDateTime { get; set; }

        public string Subject { get; set; }



        public override string ToString() => JsonSerializer.Serialize<CalendarEvent>(this);
    }
}
