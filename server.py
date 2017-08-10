from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("list.html")



if __name__=="__main__":
    app.secret_key = "hurkaleves"
    app.run(
        debug=True,
        port=5000
    )