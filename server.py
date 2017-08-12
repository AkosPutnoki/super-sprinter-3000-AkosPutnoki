from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/list")
def index():
    return render_template("list.html")


@app.route("/story")
def story():
    return render_template("form.html")


@app.route("/save", methods=["POST"])
def save():
    table = import_data("database.csv")
    new_input = input_to_list()
    new_input.insert(0, len(table)+1)
    table.append(new_input)
    export_data("database.csv", table)
    return redirect("/")


def import_data(filename):
    with open(filename, "r") as data:
        table = [list(line) for line in csv.reader(data, delimiter=",")]
    return table


def export_data(filename, table):
    with open(filename, "w") as data:
        writer = csv.writer(data)
        writer.writerows(table)
    

def input_to_list():
    inputs = []
    inputs.extend((request.form["storytitle"], request.form["userstory"], request.form["criteria"], request.form["bvalue"], 
                   request.form["estimation"], request.form["status"]))
    return inputs


if __name__=="__main__":
    app.secret_key = "kekekeke"
    app.run(
        debug=True,
        port=5000
    )