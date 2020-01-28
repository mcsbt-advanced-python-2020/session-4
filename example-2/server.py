from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        title = "Homepage",
        name = "Pepe")


app.run(debug = True)
