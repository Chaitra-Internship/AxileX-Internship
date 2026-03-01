from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kismatkharab@999",
    database="internship_db"
)

cursor = db.cursor()

# View Records

@app.route("/")
def index():
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    return render_template("index.html", products=data)


# Add Record

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]

        sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        values = (name, price, quantity)

        cursor.execute(sql, values)
        db.commit()

        return redirect("/")
    return render_template("add.html")


# Delete Record

@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    db.commit()
    return redirect("/")

# Edit Record

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        quantity = request.form["quantity"]

        sql = "UPDATE products SET name=%s, price=%s, quantity=%s WHERE id=%s"
        values = (name, price, quantity, id)

        cursor.execute(sql, values)
        db.commit()

        return redirect("/")

    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchone()
    return render_template("edit.html", product=product)


if __name__ == "__main__":
    app.run(debug=True)