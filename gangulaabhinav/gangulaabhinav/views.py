from flask import render_template

from gangulaabhinav import app

@app.route('/')
@app.route('/home')
def home():
    #            Name        URL
    myLinks = [["LinkedIn", "https://www.linkedin.com/in/abhinav-gangula-b0872462/"],
               ["GitHub",   "https://github.com/gangulaabhinav"],
               ["Facebook", "https://www.facebook.com/agangula"],
               ["Zomato",   "https://www.zomato.com/agangula"],
               ["IMDb",     "https://www.imdb.com/user/ur50420048"]]
    return render_template("ListOfLinks.html",
                           title = "Abhinav Gangula",
                           links = myLinks)

# There mmight be a conflict on removing /hello from url and using <name> directly. Conflict with /3d
@app.route('/hello', defaults={'name': 'World'})
@app.route('/hello/<name>')
def hello(name = "World"):
    return render_template("Body.html",
                           title = "Hello",
                           content = "Hello " + name)
