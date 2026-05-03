import tkinter as tk
from tkinter import messagebox
from auth import register_user, login_user
from dashboard import open_dashboard

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.configure(bg="#1E1E2F")
root.title("BMI Calculator Login")
center_window(root, 400, 400)
root.resizable(False, False)

# Username
tk.Label(
    root,
    text="Username",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2F",
    fg="white"
).pack(pady=10)
username_entry = tk.Entry(
    root,
    width=30,
    font=("Segoe UI", 11),
    bg="#2A2A40",
    fg="white",
    insertbackground="white"
)
username_entry.pack()

# Password
tk.Label(
    root,
    text="Password",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2F",
    fg="white"
).pack(pady=10)
password_entry = tk.Entry(
    root,
    width=30,
    font=("Segoe UI", 11),
    bg="#2A2A40",
    fg="white",
    insertbackground="white",
    show="."
)
password_entry.pack()


def signup():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    success = register_user(username, password)

    if success:
        messagebox.showinfo("Success", "Account created successfully")
    else:
        messagebox.showerror("Error", "Username already exists")


def login():
    username = username_entry.get()
    password = password_entry.get()

    user = login_user(username, password)

    if user:
        messagebox.showinfo(
            "Success",
            "Login successful"
        )

        open_dashboard(username)

    else:
        messagebox.showerror(
            "Error",
            "Invalid credentials"
        )


# Buttons
tk.Button(
    root,
    text="Login",
    width=20,
    height=2,
    bg="#4A90E2",
    fg="white",
    activebackground="#357ABD",
    activeforeground="white",
    font=("Segoe UI", 12, "bold"),
    bd=0,
    cursor="hand2",
    command=login
).pack(pady=10)

tk.Button(
    root,
    text="Signup",
    width=20,
    height=2,
    bg="#4A90E2",
    fg="white",
    activebackground="#357ABD",
    activeforeground="white",
    font=("Segoe UI", 12, "bold"),
    bd=0,
    cursor="hand2",
    command=signup
).pack(pady=10)

root.mainloop()