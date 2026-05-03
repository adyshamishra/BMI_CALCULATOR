import sqlite3
def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def view_users():

    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, role FROM users")

    users = cursor.fetchall()

    print("\n--- USERS ---")

    for user in users:
        print(user)

    conn.close()


def delete_user():

    username = input("Enter username to delete: ")

    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE username=?",
        (username,)
    )

    conn.commit()
    conn.close()

    print("User deleted successfully")


def view_records():

    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT username, bmi, category
    FROM bmi_records
    """)

    records = cursor.fetchall()

    print("\n--- BMI RECORDS ---")

    for record in records:
        print(record)

    conn.close()


while True:

    print("""
1. View Users
2. Delete User
3. View BMI Records
4. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        view_users()

    elif choice == "2":
        delete_user()

    elif choice == "3":
        view_records()

    elif choice == "4":
        break

    else:
        print("Invalid choice")