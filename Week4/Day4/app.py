from flask import Flask, render_template, request
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

# Route: Show Form
@app.route("/")
def form():
    return render_template("form.html")


# Route: Handle Form Submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]

    sql = "INSERT INTO form_data (name, email, course) VALUES (%s, %s, %s)"
    values = (name, email, course)

    cursor.execute(sql, values)
    db.commit()

    return "Data Stored Successfully!"


# Route: Display Stored Data
@app.route("/display")
def display():
    cursor.execute("SELECT * FROM form_data")
    data = cursor.fetchall()
    return render_template("display.html", records=data)


if __name__ == "__main__":
    app.run(debug=True)