using System;
using System.Collections.Generic;

namespace gangulaabhinav.Models
{
    public class Link
    {
        public string Name { get; set; }
        public string Url { get; set; }
    }

    public class HomeModel
    {
        public List<Link> GetListOfLinks()
        {
            return new List<Link>
            {
                new Link{
                Name = "LinkedIn",
                Url  = "https://github.com/gangulaabhinav"
                },

                new Link{
                Name = "GitHub",
                Url  = "https://github.com/gangulaabhinav"
                },

                new Link{
                Name = "Facebook",
                Url  ="https://www.facebook.com/agangula"
                },

                new Link{
                Name = "Zomato",
                Url  ="https://www.zomato.com/agangula"
                },

                new Link{
                Name = "IMDb",
                Url  ="https://www.imdb.com/user/ur50420048"
                }
            };
        }
    }
}
