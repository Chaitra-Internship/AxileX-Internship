from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/api")
def api():
    return jsonify({"message": "Job Tracker Backend Running"})


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        ).fetchone()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Login"

    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        db.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username,password)
        )

        db.commit()

        return redirect("/")

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():

    db = get_db()

    jobs = db.execute(
        "SELECT * FROM jobs"
    ).fetchall()

    return render_template("dashboard.html", jobs=jobs)


@app.route("/add", methods=["GET","POST"])
def add():

    if request.method == "POST":

        company = request.form["company"]
        role = request.form["role"]
        status = request.form["status"]
        date = request.form["date"]

        db = get_db()

        db.execute(
            "INSERT INTO jobs(company,role,status,date) VALUES (?,?,?,?)",
            (company,role,status,date)
        )

        db.commit()

        return redirect("/dashboard")

    return render_template("add_job.html")


@app.route("/delete/<int:id>")
def delete(id):

    db = get_db()

    db.execute(
        "DELETE FROM jobs WHERE id=?",
        (id,)
    )

    db.commit()

    return redirect("/dashboard")


if __name__ == "__main__":
    app.run()