import sqlite3
def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

# ---------------- REGISTER USER ---------------- #

def register_user(username, password):

    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            (username, password)
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()

# ---------------- LOGIN USER ---------------- #

def login_user(username, password):

    conn = sqlite3.connect("bmi.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user