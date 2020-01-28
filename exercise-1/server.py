from flask import Flask, render_template


app = Flask(__name__)

tweets = [
    {
        "username": "harry_p",
        "tweet": "haha, magic's fun!"
    },
    {
        "username": "voldemort",
        "tweet": "I wouldn't say so..."
    },
    {
        "username": "harry_p",
        "tweet": "@voldemort I'll wingardium the cr*p out of u!"
    },
]


@app.route("/")
def index():
    return render_template("tweet.html")


app.run(debug = True)
