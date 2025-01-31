import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from ud2 import request_document_page

def document_list_window():
    root = tk.Tk()
    root.title("Document List")
    root.geometry("900x600")
    root.configure(bg="#e3f2fd")  # Changed to a light blue background color

    # Database connection
    def connect_db():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="admin@123",  # Replace with your MySQL password
            database="admin"
        )

    # Fetch documents from the database
    def fetch_documents():
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description FROM docs")
        documents = cursor.fetchall()
        conn.close()
        return documents

    # Fetch documents and display
    try:
        documents = fetch_documents()
    except:
        messagebox.showerror("Error", "Unable to connect to the database. Closing the application.")
        root.destroy()
        return

    # Header Section
    header_frame = tk.Frame(root, bg="#42a5f5", height=50)  # Changed to a soft blue header
    header_frame.pack(fill="x")
    header_label = tk.Label(
        header_frame,
        text="Document List",font=("Arial", 24, "bold"),bg="#42a5f5", fg="white"
    )
    header_label.pack(pady=10)

    # Content Frame
    content_frame = tk.Frame(root, bg="#ffffff", relief="groove", bd=2)
    content_frame.pack(padx=20, pady=20, expand=True, fill="both")

    # Treeview for displaying documents
    columns = ("ID", "Title", "Description")
    tree = ttk.Treeview(content_frame, columns=columns, show="headings", height=15)
    tree.pack(pady=10, padx=10, expand=True, fill="both")

    # Set up columns and headings
    for col in columns:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, anchor="center", width=250)

    # Style for Treeview
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 12), rowheight=25, background="#f1f8e9", fieldbackground="#f1f8e9")  # Light background for treeview rows
    style.configure("Treeview.Heading", font=("Arial", 14, "bold"), background="#b3e5fc", foreground="black")  # Lighter blue for headings

    # Insert documents into the treeview
    for doc in documents:
        tree.insert("", "end", values=doc)

    # Button Section
    button_frame = tk.Frame(root, bg="#e3f2fd")  # Changed button frame color to match new light blue theme
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Request Document",font=("Arial", 14, "bold"),bg="#42a5f5",  fg="white",
        activebackground="#1e88e5",command=request_document_page
    ).pack(ipadx=20, ipady=5)

    root.mainloop()

# Run the application
# document_list_window()
