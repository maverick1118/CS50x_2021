import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, abort, flash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get('name')
        if not name:
            return abort(404, description = 'Name missing')
        day = request.form.get('day')
        if not day:
            # return abort(404, description = 'Day missing')
            return flash("Day missing")
        month = request.form.get('month')
        if not month:
            return flash(abort(404, description = 'Month missing'))
        birthdays = db.execute('INSERT INTO birthdays(name, month, day) values (?, ?, ?)', name, month, day)
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays = birthdays)


