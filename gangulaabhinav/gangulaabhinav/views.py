from gangulaabhinav import app

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"
