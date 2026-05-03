import sqlite3

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

conn = sqlite3.connect("bmi.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM bmi_records")

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()