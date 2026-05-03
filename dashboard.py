import tkinter as tk
from bmi_calculator import open_bmi_calculator
from history import open_history
from analytics import open_analytics

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def open_dashboard(username, previous_window=None):

    # Close previous page
    if previous_window:
        previous_window.destroy()

    dashboard = tk.Tk()
    dashboard.configure(bg="#1E1E2F")

    dashboard.title("Dashboard")
    center_window(dashboard, 400, 400)

    # ---------------- Welcome Label ---------------- #

    tk.Label(
        dashboard,
        text=f"Welcome, {username}",
        font=("Segoe UI", 18, "bold"),
        bg="#1E1E2F",
        fg="white"
    ).pack(pady=20)
    # ---------------- BMI Calculator Button ---------------- #

    tk.Button(
        dashboard,
        text="BMI Calculator",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        bg="#4A90E2",
        fg="white",
        activebackground="#357ABD",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=lambda: open_bmi_calculator(username, dashboard)
    ).pack(pady=10)

    # ---------------- History Button ---------------- #

    tk.Button(
        dashboard,
        text="View History",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        bg="#4A90E2",
        fg="white",
        activebackground="#357ABD",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=lambda: open_history(username, dashboard)
    ).pack(pady=10)

    # ---------------- Analytics Button ---------------- #

    tk.Button(
        dashboard,
        text="Analytics",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        bg="#4A90E2",
        fg="white",
        activebackground="#357ABD",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=lambda: open_analytics(username, dashboard)
    ).pack(pady=10)

    # ---------------- Logout Button ---------------- #

    tk.Button(
        dashboard,
        text="Logout",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        bg="#4A90E2",
        fg="white",
        activebackground="#357ABD",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=dashboard.destroy
    ).pack(pady=10)

    dashboard.mainloop()