from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret123"

# Database Connection (SQLite)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create tables automatically if not exists
conn = get_db_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT,
    marks TEXT
)
""")

conn.commit()
conn.close()

# API Route (for frontend test)

@app.route("/api")
def api():
    return jsonify({"message": "Backend Connected Successfully!"})

# Registration

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except:
            return "User already exists!"

        conn.close()
        return redirect("/")

    return render_template("register.html")

# Login

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid Credentials!"

    return render_template("login.html")

# Dashboard (View Records)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    return render_template("dashboard.html", students=students)

# Add Student

@app.route("/add", methods=["GET", "POST"])
def add():
    if "user" not in session:
        return redirect("/")

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, course, marks) VALUES (?, ?, ?)",
                       (name, course, marks))
        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("add.html")

# Edit Student

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if "user" not in session:
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]

        cursor.execute("UPDATE students SET name=?, course=?, marks=? WHERE id=?",
                       (name, course, marks, id))
        conn.commit()
        conn.close()

        return redirect("/dashboard")

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()

    return render_template("edit.html", student=student)

# Delete Student

@app.route("/delete/<int:id>")
def delete(id):
    if "user" not in session:
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")

# Logout

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# Run App (Local Only)

if __name__ == "__main__":
    app.run(debug=True)