import os

from flask import Flask, flash, redirect, render_template, request, session, url_for

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


def _login_is_correct(user, password):
    """This function simulates validation & db pass check.
    If everything is ok, user is added to the session."""

    saved_username = os.getenv("SAVED_USERNAME")
    saved_password = os.getenv("SAVED_PASSWORD")

    if saved_username == user and saved_password == password:
        session["user"] = user
        return True
    else:
        flash("Bad login.")
        return False


@app.route("/")
def main():
    user = session.get("user")
    print(user)
    # user loged in
    if user:
        return render_template("index.html", user=user)

    # else
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if _login_is_correct(username, password):
            return redirect(url_for("main"))

    return render_template("login.html")
