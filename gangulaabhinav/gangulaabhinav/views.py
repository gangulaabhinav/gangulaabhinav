import os, sys
from importlib import reload
import traceback

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
                           heading = "Welcome",
                           links = myLinks,
                           icon = os.path.join("static", "gangulaabhinav.ico"))

# There might be a conflict on removing /hello from url and using <name> directly. Conflict with /3d
@app.route('/hello', defaults={'name': 'World'})
@app.route('/hello/<name>')
def Hello(name = "World"):
    return render_template("Body.html",
                           title = "Hello",
                           content = "Hello " + name,
                           icon = os.path.join("static", "gangulaabhinav.ico")) # favico not working here. hello is being added to favicon path

@app.route('/3d')
def Box3d():
    title = "Box3d"
    try:
        return render_template("Content.html",
                               content = Get3dSnippet(),
                               icon = os.path.join("static", "box3d.ico"))
    except Exception as e:
        encodingStr = "System encoding = " + str(sys.stdout.encoding or 'NONE')
        return render_template("Error.html",
                               title = title,
                               error = str(e) + "\n" + encodingStr,
                               callstack = traceback.format_exc())

# Temperory url to check import IPython. IPython is failing for pythreejs
@app.route('/ip')
def ImportIPython():
    title = "IPython"
    #os.environ['PYTHONIOENCODING'] = "utf-8"
    #reload(sys)
    #import codecs
    #sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    encodingStr = "sys.stdout.encoding = " + str(sys.stdout.encoding or 'NONE')
    encodingStr += "\n"
    encodingStr += "sys.stdin.encoding = " + str(sys.stdin.encoding or 'NONE')
    encodingStr += "\n"
    encodingStr += "sys.getdefaultencoding() = " + str(sys.getdefaultencoding() or 'NONE')
    encodingStr += "\n"
    encodingStr += "sys.getfilesystemencoding() = " + str(sys.getfilesystemencoding() or 'NONE')
    encodingStr += "\n"
    encodingStr += "PYTHONIOENCODING = " + str(os.getenv('PYTHONIOENCODING') or 'NONE')
    try:
        import IPython
        return render_template("Body.html",
                               title = title,
                               heading = "Improting IPython",
                               content = "IPython imported successfuly" + "\n" + encodingStr)
    except Exception as e:
        return render_template("Error.html",
                               title = title,
                               error = str(e) + "\n" + encodingStr,
                               callstack = traceback.format_exc())
