import sqlite3

# Connect (creates file automatically)
conn = sqlite3.connect("cars.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price TEXT,
    engine TEXT,
    fuel TEXT,
    description TEXT
)
""")

# Car data (Pakistan cars)
cars = [
    ("Suzuki Alto", "28–32 lakh PKR", "660cc", "Petrol", "Best budget city car with great mileage"),
    ("Suzuki Cultus", "38–45 lakh PKR", "1000cc", "Petrol", "Reliable hatchback for families"),
    ("Toyota Corolla", "60–80 lakh PKR", "1800cc", "Petrol", "Most popular sedan in Pakistan"),
    ("Toyota Yaris", "45–55 lakh PKR", "1300cc", "Petrol", "Fuel efficient modern sedan"),
    ("Honda Civic", "85–95 lakh PKR", "1500cc Turbo", "Petrol", "Sport luxury performance sedan"),
    ("Honda City", "50–60 lakh PKR", "1500cc", "Petrol", "Comfortable family sedan"),
    ("Kia Sportage", "95–120 lakh PKR", "2000cc", "Petrol", "Luxury SUV with modern features"),
    ("Hyundai Tucson", "98–115 lakh PKR", "2000cc", "Petrol", "Smart premium SUV"),
    ("MG HS", "85–105 lakh PKR", "1500cc Turbo", "Petrol", "Tech luxury SUV")
]

# Insert data
cursor.executemany("""
INSERT INTO cars (name, price, engine, fuel, description)
VALUES (?, ?, ?, ?, ?)
""", cars)

# Save changes
conn.commit()
conn.close()

print("Database created successfully 🚗")