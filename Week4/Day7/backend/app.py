from flask import Flask, render_template, request, redirect, session, jsonify
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = "secret123"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kismatkharab@999",
    database="backend_project"
)

cursor = db.cursor()

#  HOME API (For Netlify frontend)
@app.route("/api")
def api():
    return jsonify({"message": "Backend Connected Successfully!"})

#  Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("INSERT INTO users (username, password) VALUES (%s,%s)", (username,password))
        db.commit()
        return redirect("/")
    return render_template("register.html")

# Login
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
        user = cursor.fetchone()
        if user:
            session["user"] = username
            return redirect("/dashboard")
        return "Invalid Credentials"
    return render_template("login.html")

#  Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template("dashboard.html", students=data)

#  Add Student
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]
        cursor.execute("INSERT INTO students (name,course,marks) VALUES (%s,%s,%s)",(name,course,marks))
        db.commit()
        return redirect("/dashboard")
    return render_template("add.html")

# Edit Student
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]
        cursor.execute("UPDATE students SET name=%s,course=%s,marks=%s WHERE id=%s",(name,course,marks,id))
        db.commit()
        return redirect("/dashboard")
    cursor.execute("SELECT * FROM students WHERE id=%s",(id,))
    student = cursor.fetchone()
    return render_template("edit.html", student=student)

# Delete Student
@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM students WHERE id=%s",(id,))
    db.commit()
    return redirect("/dashboard")

# Logout
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5001))
    app.run(host="0.0.0.0", port=port)