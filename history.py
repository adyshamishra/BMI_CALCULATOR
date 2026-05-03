import tkinter as tk
from tkinter import ttk
import sqlite3

def center_window(window, width, height):

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    window.geometry(f"{width}x{height}+{x}+{y}")

def open_history(username, previous_window):

    # Close previous window
    previous_window.destroy()

    history_window = tk.Tk()

    history_window.title("BMI History")
    center_window(history_window, 700, 400)

    # ---------------- Table ---------------- #

    columns = (
        "ID",
        "Height",
        "Weight",
        "BMI",
        "Category"
    )

    tree = ttk.Treeview(
        history_window,
        columns=columns,
        show="headings"
    )

    for col in columns:

        tree.heading(col, text=col)

        tree.column(col, width=120)

    tree.pack(fill="both", expand=True)

    # ---------------- Database ---------------- #

    conn = sqlite3.connect("bmi.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, height, weight, bmi, category
    FROM bmi_records
    WHERE username=?
    """, (username,))

    records = cursor.fetchall()

    for record in records:

        tree.insert("", tk.END, values=record)

    conn.close()

    # ---------------- Delete Record ---------------- #

    def delete_record():

        selected_item = tree.selection()

        if not selected_item:
            return

        item = tree.item(selected_item)

        record_id = item["values"][0]

        conn = sqlite3.connect("bmi.db")

        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM bmi_records WHERE id=?",
            (record_id,)
        )

        conn.commit()

        conn.close()

        tree.delete(selected_item)

        from tkinter import messagebox

        messagebox.showinfo(
            "Deleted",
            "Record deleted successfully"
        )

    tk.Button(
        history_window,
        text="Delete Selected Record",
        command=delete_record,
        font=("Segoe UI", 12, "bold")
    ).pack(pady=10)

    # ---------------- Back Function ---------------- #

    def go_back():

        from dashboard import open_dashboard

        open_dashboard(username, history_window)

    # ---------------- Back Button ---------------- #

    tk.Button(
        history_window,
        text="Back to Dashboard",
        width=20,
        height=2,
        font=("Segoe UI", 12, "bold"),
        command=go_back
    ).pack(pady=10)

    history_window.mainloop()