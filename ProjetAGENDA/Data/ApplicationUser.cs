using Microsoft.AspNetCore.Identity;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ProjetAGENDA.Data
{
    public class ApplicationUser: IdentityUser
    {
        public string Name { get; set; }
        public string Pseudo { get; set; }

        public string jsonName { get; set; }

    }
}
