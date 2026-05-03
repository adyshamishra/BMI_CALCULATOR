import tkinter as tk
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def open_analytics(username, previous_window):

    # Close previous window
    previous_window.destroy()

    analytics_window = tk.Tk()
    analytics_window.configure(bg="#1E1E2F")

    analytics_window.title("BMI Analytics")
    center_window(analytics_window, 600, 500)

    # ---------------- Title ---------------- #

    tk.Label(
        analytics_window,
        text="BMI Analytics Dashboard",
        font=("Segoe UI", 12, "bold")
    ).pack(pady=20)

    # ---------------- Fetch Data ---------------- #

    conn = sqlite3.connect("bmi.db")

    query = """
    SELECT weight, bmi
    FROM bmi_records
    WHERE username=?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(username,)
    )

    conn.close()

    # ---------------- No Data Check ---------------- #

    if df.empty:

        tk.Label(
            analytics_window,
            text="No BMI Records Found",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=20)

        return

    # ---------------- Statistics ---------------- #

    avg_bmi = round(df["bmi"].mean(), 2)

    max_bmi = round(df["bmi"].max(), 2)

    min_bmi = round(df["bmi"].min(), 2)

    stats_text = f"""
Average BMI : {avg_bmi}

Highest BMI : {max_bmi}

Lowest BMI : {min_bmi}
"""
    
    tk.Label(
        analytics_window,
        text=stats_text,
        font=("Segoe UI", 12, "bold"),
        justify="left"
    ).pack(pady=10)

    # ---------------- Insight Text ---------------- #

    latest_bmi = df["bmi"].iloc[-1]

    if latest_bmi < avg_bmi:

        insight = "Great progress! Your latest BMI is below your average."

    elif latest_bmi > avg_bmi:

        insight = "Your BMI has increased recently. Stay consistent."

    else:

        insight = "Your BMI is stable."

    tk.Label(
        analytics_window,
        text=insight,
        font=("Segoe UI", 11, "bold"),
        bg="#1E1E2F",
        fg="#00C2FF"
    ).pack(pady=10)

    # ---------------- Graph Figure ---------------- #

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(
        df.index + 1,
        df["bmi"],
        marker="o"
    )

    ax.set_title("BMI Trend")

    ax.set_xlabel("Record Number")

    ax.set_ylabel("BMI")

    # ---------------- Show Graph in Tkinter ---------------- #

    canvas = FigureCanvasTkAgg(
        fig,
        master=analytics_window
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill=tk.BOTH,
        expand=True
    )

    # ---------------- Back Button ---------------- #

    def go_back():

        from dashboard import open_dashboard

        open_dashboard(username, analytics_window)

    tk.Button(
        analytics_window,
        text="Back to Dashboard",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        command=go_back
    ).pack(pady=10)

    analytics_window.mainloop()