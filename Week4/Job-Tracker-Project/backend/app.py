from flask import Flask, render_template, request, redirect, session, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
app.secret_key = "secret123"


# ---------- DATABASE ----------

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    # Jobs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        role TEXT,
        status TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------- API TEST ----------

@app.route("/api")
def api():
    return jsonify({"message": "Job Tracker Backend Running"})


# ---------- LOGIN ----------

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


# ---------- REGISTER ----------

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


# --------- DASHBOARD ----------

@app.route("/dashboard")
def dashboard():

    db = get_db()

    jobs = db.execute(
        "SELECT * FROM jobs"
    ).fetchall()

    return render_template("dashboard.html", jobs=jobs)


# ---------- ADD JOB ----------

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


# ---------- UPDATE JOB ----------

@app.route("/update_job/<int:id>", methods=["POST"])
def update_job(id):

    status = request.form["status"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE jobs SET status=? WHERE id=?",
        (status, id)
    )

    conn.commit()
    conn.close()

    return redirect("/dashboard")


# ---------- DELETE JOB ----------

@app.route("/delete/<int:id>")
def delete(id):

    db = get_db()

    db.execute(
        "DELETE FROM jobs WHERE id=?",
        (id,)
    )

    db.commit()

    return redirect("/dashboard")


# ---------- RUN SERVER ----------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)