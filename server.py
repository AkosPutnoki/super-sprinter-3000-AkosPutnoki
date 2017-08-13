from flask import Flask, render_template, redirect, request, session, url_for
import csv

app = Flask(__name__)

@app.route("/")
@app.route("/list")
def index():
    database = import_data("database.csv")
    return render_template("list.html", database=database)


@app.route("/story")
def story():
    update = False
    return render_template("form.html", update=update)


@app.route("/save", methods=["POST"])
def save():
    table = import_data("database.csv")
    new_input = input_to_list()
    if len(table) > 0:
        id_list = [int(record[0]) for record in table]
        new_input.insert(0, max(id_list)+1)
    else:
        new_input.insert(0, 1)
    table.append(new_input)
    export_data("database.csv", table)
    return redirect("/")


@app.route("/story/<story_id>")
def show_story(story_id):
    update = True
    table = import_data("database.csv")
    for record in table:
        if record[0] == story_id:
            id_ = record[0]
            storytitle = record[1]
            userstory = record[2]
            criteria = record[3]
            bvalue = record[4]
            estimation = record[5]
            status = record[6]
    return render_template("form.html", update=update, table=table, story_id=id_, storytitle=storytitle, userstory=userstory, criteria=criteria, bvalue=bvalue,
                            estimation=estimation, status=status)


@app.route("/update/<story_id>", methods=["POST"])
def update(story_id):
    table = import_data("database.csv")
    new_input = input_to_list()
    new_input.insert(0, story_id)
    for record in table:
        if record[0] == story_id:
            table.remove(record)
    table.insert(int(story_id) - 1,new_input)
    export_data("database.csv", table)
    return redirect("/")


@app.route("/delete/<story_id>", methods=["POST"])
def delete(story_id):
    table = import_data("database.csv")
    for record in table:
        if record[0] == story_id:
            table.remove(record)
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