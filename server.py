from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("list.html")


@app.route("/story")
def story():
    return render_template("form.html")


if __name__=="__main__":
    app.secret_key = "kekekeke"
    app.run(
        debug=True,
        port=5000
    )