using Microsoft.AspNetCore.Hosting;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

using ProjetAGENDA.Models;
using System.Text.Json;
using Microsoft.AspNetCore.Identity;
using ProjetAGENDA.Data;
using Microsoft.AspNetCore.Mvc.Razor;
using System.Text;

namespace ProjetAGENDA.Services
{
    public class JsonFileEventsService
    {
        public JsonFileEventsService(IWebHostEnvironment webHostEnvironment,
            UserManager<ApplicationUser> userManager,
            SignInManager<ApplicationUser> signInManager
            )
        {
            WebHostEnvironment = webHostEnvironment;
            UserMan = userManager;
            SignInMan = signInManager;
        }

        public IWebHostEnvironment WebHostEnvironment;
        public UserManager<ApplicationUser> UserMan;
        SignInManager<ApplicationUser> SignInMan;

        private string JsonFileName(string PersonJson)
        {
            return Path.Combine(WebHostEnvironment.WebRootPath, "jsonData", PersonJson);
        }

        public IEnumerable<CalendarEvent> GetEvents(string PersonJson)
        {
            if (!File.Exists(JsonFileName(PersonJson)))
            {
                File.Create(JsonFileName(PersonJson)).Close();
                using (StreamWriter sw = new StreamWriter(JsonFileName(PersonJson)))
                    sw.WriteLine("[\n]");
            }
                

            using (var jsonFileReader = File.OpenText(JsonFileName(PersonJson)))
            {
                return JsonSerializer.Deserialize<CalendarEvent[]>(jsonFileReader.ReadToEnd(),
                    new JsonSerializerOptions 
                    {
                        PropertyNameCaseInsensitive = true 
                    });
            }
        }

        public void AddEvent(string PersonId,CalendarEvent cEvent)
        {
            var events = GetEvents(PersonId+".json");

            var query = events.ToList();
            query.Add(cEvent);

            using (var outputStream = File.OpenWrite(JsonFileName(PersonId + ".json")))
            {
                JsonSerializer.Serialize<IEnumerable<CalendarEvent>>(
                new Utf8JsonWriter(outputStream, new JsonWriterOptions
                {
                    SkipValidation = true,
                    Indented = true
                }),
                query
                );
            }
        }
    }
}
