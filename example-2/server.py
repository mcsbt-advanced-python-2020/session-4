from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    logged_in = False
    
    return render_template(
        "index.html",
        title = "Homepage",
        name = "World",
        logged_in = logged_in)


app.run(debug = True)
