from os import path

from flask import render_template

from gangulaabhinav import app
from gangulaabhinav.box3d import Get3dSnippet

@app.route('/')
@app.route('/home')
def Home():
    #            Name        URL
    myLinks = [["LinkedIn", "https://www.linkedin.com/in/abhinav-gangula-b0872462/"],
               ["GitHub",   "https://github.com/gangulaabhinav"],
               ["Facebook", "https://www.facebook.com/agangula"],
               ["Zomato",   "https://www.zomato.com/agangula"],
               ["IMDb",     "https://www.imdb.com/user/ur50420048"]]
    return render_template("ListOfLinks.html",
                           title = "Abhinav Gangula",
                           links = myLinks,
                           icon = path.join("static", "gangulaabhinav.ico"))

# There might be a conflict on removing /hello from url and using <name> directly. Conflict with /3d
@app.route('/hello', defaults={'name': 'World'})
@app.route('/hello/<name>')
def Hello(name = "World"):
    return render_template("Body.html",
                           title = "Hello",
                           content = "Hello " + name,
                           icon = path.join("static", "gangulaabhinav.ico")) # favico not working here. hello is being added to favicon path

@app.route('/3d')
def Box3d():
    try:
        return render_template("Body.html",
                               title = "Box3d",
                               content = Get3dSnippet(),
                               icon = path.join("static", "box3d.ico"))
    except Exception as e:
        return(str(e))  
