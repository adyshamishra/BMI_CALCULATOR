import tkinter as tk
from tkinter import messagebox
import sqlite3

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")
# ---------------- BMI Formula ---------------- #

def calculate_bmi(weight, height):

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    return round(bmi, 2)

# ---------------- BMI Category ---------------- #

def get_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"

# ---------------- Save Record ---------------- #

def save_record(username, height, weight, bmi, category):

    conn = sqlite3.connect("bmi.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bmi_records
    (username, height, weight, bmi, category)
    VALUES (?, ?, ?, ?, ?)
    """, (username, height, weight, bmi, category))

    conn.commit()
    conn.close()

# ---------------- Open BMI Calculator ---------------- #

def open_bmi_calculator(username, previous_window):

    # Close previous page
    previous_window.destroy()

    bmi_window = tk.Tk()

    bmi_window.title("BMI Calculator")
    bmi_window.configure(bg="#1E1E2F")
    center_window(bmi_window, 400, 450)

    # ---------------- Heading ---------------- #

    tk.Label(
        bmi_window,
        text="BMI Calculator",
        font=("Segoe UI", 18, "bold"),
        bg="#1E1E2F",
        fg="white"
    ).pack(pady=20)

    # ---------------- Height Input ---------------- #

    tk.Label(
        bmi_window,
        text="Enter Height (in cm)",
        font=("Segoe UI", 12, "bold"),
        bg="#1E1E2F",
        fg="white"
    ).pack(pady=10)

    height_entry = tk.Entry(
        bmi_window,
        width=25
    )

    height_entry.pack()

    # ---------------- Weight Input ---------------- #

    tk.Label(
        bmi_window,
        text="Enter Weight (in kg)",
        font=("Segoe UI", 12, "bold"),
        bg="#1E1E2F",
        fg="white"
    ).pack(pady=10)

    weight_entry = tk.Entry(
        bmi_window,
        width=25
    )

    weight_entry.pack()

    # ---------------- Result Label ---------------- #

    result_label = tk.Label(
        bmi_window,
        text="",
        font=("Segoe UI", 12, "bold"),
        bg="#1E1E2F",
        fg="white"
    )

    result_label.pack(pady=20)

    # ---------------- Status Label ---------------- #

    status_label = tk.Label(
        bmi_window,
        text="",
        font=("Segoe UI", 10),
        bg="#1E1E2F",
        fg="#00C2FF"
    )

    status_label.pack(pady=5)

    # ---------------- Calculate Function ---------------- #

    def calculate():

        try:

            height = float(height_entry.get())
            weight = float(weight_entry.get())

            # Validation
            if height <= 0 or weight <= 0:

                messagebox.showerror(
                    "Error",
                    "Enter valid height and weight"
                )

                return

            # Calculate BMI
            status_label.config(text="Calculating BMI...")
            bmi = calculate_bmi(weight, height)

            # Get Category
            category = get_category(bmi)

            # Show Result
            result_label.config(
                text=f"BMI: {bmi}\nCategory: {category}"
            )
            status_label.config(text="BMI calculated successfully")

            # Save to Database
            save_record(
                username,
                height,
                weight,
                bmi,
                category
            )

            messagebox.showinfo(
                "Success",
                "BMI Record Saved Successfully"
            )

        except:

            messagebox.showerror(
                "Error",
                "Please enter numeric values only.\nExample: Height = 170, Weight = 65"
            )

    # ---------------- Calculate Button ---------------- #

    tk.Button(
        bmi_window,
        text="Calculate BMI",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        command=calculate
    ).pack(pady=10)

    # ---------------- Go Back Function ---------------- #

    def go_back():

        from dashboard import open_dashboard

        open_dashboard(username, bmi_window)

    # ---------------- Back Button ---------------- #

    tk.Button(
        bmi_window,
        text="Back to Dashboard",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        command=go_back
    ).pack(pady=10)

    bmi_window.mainloop()