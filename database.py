import sqlite3

# Connect Database
conn = sqlite3.connect("student.db")

# Create Cursor
cursor = conn.cursor()

# Create Login Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS login(
    username TEXT,
    password TEXT
)
""")

# Create Students Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    course TEXT,
    email TEXT,
    phone TEXT,
    address TEXT
)
""")

# Insert Default Admin Login
cursor.execute("SELECT * FROM login")

if cursor.fetchone() is None:
    cursor.execute("""
    INSERT INTO login(username,password)
    VALUES('admin','admin123')
    """)

conn.commit()
conn.close()

print("Database Created Successfully")
