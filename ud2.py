import tkinter as tk
from tkinter import messagebox
from ud3 import open_document_window
import pymysql

def request_document_page():
    def check_document():
        doc_id = doc_id_entry.get()

        if not doc_id.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid document ID.")
            return

        # Call the function to open the document in a new window
        open_document_window(doc_id)

    # New window for document ID input
    request_window = tk.Toplevel()
    request_window.title("Request Document")
    request_window.geometry("500x300")
    request_window.configure(bg="#f7f9fc")  # Light background for a clean look

    # Header Section
    header_frame = tk.Frame(request_window, bg="#87CEEB", height=50)  # Light pastel blue
    header_frame.pack(fill="x")
    header_label = tk.Label(
        header_frame,
        text="Request a Document",
        font=("Arial", 18, "bold"),
        bg="#87CEEB",
        fg="white"
    )
    header_label.pack(pady=10)

    # Content Section
    content_frame = tk.Frame(request_window, bg="#ffffff", relief="groove", bd=2)
    content_frame.pack(padx=20, pady=20, expand=True, fill="both")

    tk.Label(
        content_frame, 
        text="Enter Document ID:", 
        font=("Arial", 14, "bold"),
        bg="#ffffff",
        fg="#2b2b2b"
    ).pack(pady=10)
    doc_id_entry = tk.Entry(content_frame, font=("Arial", 14), relief="solid", bd=2, justify="center")
    doc_id_entry.pack(pady=10, ipadx=10, ipady=5)

    # Button Section
    tk.Button(
        content_frame,
        text="Request",
        font=("Arial", 14, "bold"),
        bg="#87CEEB",  # Light pastel blue
        fg="white",
        activebackground="#add8e6",  # Even lighter blue on hover
        command=check_document
    ).pack(pady=20, ipadx=20, ipady=5)

    request_window.mainloop()
