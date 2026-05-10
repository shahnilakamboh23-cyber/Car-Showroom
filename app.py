from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# 📌 CONNECT DATABASE
def get_db():
    conn = sqlite3.connect("cars.db")
    conn.row_factory = sqlite3.Row
    return conn

# 🏠 HOME PAGE (SHOW ALL CARS)
@app.route("/")
def home():
    conn = get_db()
    cars = conn.execute("SELECT * FROM cars").fetchall()
    conn.close()
    return render_template("index.html", cars=cars)

# 🔍 SEARCH FUNCTION
@app.route("/search")
def search():
    query = request.args.get("q")

    conn = get_db()
    cars = conn.execute(
        "SELECT * FROM cars WHERE name LIKE ?",
        ('%' + query + '%',)
    ).fetchall()
    conn.close()

    return render_template("index.html", cars=cars)

# 🚗 CAR DETAILS PAGE
@app.route("/car/<int:id>")
def car_detail(id):
    conn = get_db()
    car = conn.execute("SELECT * FROM cars WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("car.html", car=car)

# ▶️ RUN SERVER
if __name__ == "__main__":
    app.run(debug=True,port=5000)