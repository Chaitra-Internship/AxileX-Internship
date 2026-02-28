from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kismatkharab@999",   
    database="internship_db"
)

cursor = db.cursor()

# Login Page
@app.route("/")
def login():
    return render_template("login.html")


# Handle Login
@app.route("/login", methods=["POST"])
def handle_login():
    username = request.form["username"]
    password = request.form["password"]

    sql = "SELECT * FROM user1 WHERE username=%s AND password=%s"
    values = (username, password)

    cursor.execute(sql, values)
    user = cursor.fetchone()

    if user:
        return redirect("/dashboard")
    else:
        return "Invalid Username or Password!"


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)