using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetAGENDA.Models
{
    public class NewCalendarEvent: CalendarEvent
    {
        public NewCalendarEvent(string id, string maker, string SDT,string EDT, string sub)
        {
            this.Id = id;
            this.Maker = maker;
            this.StartDateTime = SDT;
            this.EndDateTime = EDT;
            this.Subject = sub;
        }
    }
}
