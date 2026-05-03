import sqlite3

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def connect_db():
    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT DEFAULT 'user'
    )
    """)

    # BMI records table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bmi_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        height REAL,
        weight REAL,
        bmi REAL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()

connect_db()