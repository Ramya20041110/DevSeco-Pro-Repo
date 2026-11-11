from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="arn:aws:rds:ap-south-1:819439780802:db:terraform-78465c5dfd7fd0f9bcc853d8b3",
        user="admin",
        password="AdminUser5564",
        database="devopspro123"
    )

@app.route("/")
def home():
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        db = get_db_connection()
        cursor = db.cursor()

        sql = "INSERT INTO students (name, course) VALUES (%s, %s)"
        cursor.execute(sql, (name, course))

        db.commit()

        cursor.close()
        db.close()

        return redirect("/")

    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete_student(id):

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    db.commit()

    cursor.close()
    db.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
