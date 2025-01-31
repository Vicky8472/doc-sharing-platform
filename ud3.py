import tkinter as tk
from tkinter import filedialog, messagebox
import pymysql

def open_document_window(doc_id):
    # Database connection
    def connect_db():
        return pymysql.connect(
            host="localhost",
            user="root",
            password="admin@123",  # Replace with your MySQL password
            database="admin"
        )

    # Fetch document content by ID
    def fetch_document_by_id(doc_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT title, content FROM docs WHERE id = %s", (doc_id,))
        document = cursor.fetchone()
        conn.close()
        return document

    document = fetch_document_by_id(doc_id)
    if document:
        title, content = document
        content = content.decode("utf-8") if isinstance(content, bytes) else content

        # Create a new window to display the document
        doc_window = tk.Toplevel()
        doc_window.title(f"Document - {title}")
        doc_window.geometry("600x400")
        doc_window.configure(bg="#f4f5f7")  # Light background for a modern look

        # Header section
        header_frame = tk.Frame(doc_window, bg="#4B89DC", height=50)
        header_frame.pack(fill="x")
        header_label = tk.Label(
            header_frame,
            text=title,
            font=("Helvetica", 18, "bold"),
            bg="#4B89DC",
            fg="white"
        )
        header_label.pack(pady=10)

        # Content section
        content_frame = tk.Frame(doc_window, bg="#ffffff", relief="solid", bd=2)
        content_frame.pack(padx=20, pady=20, expand=True, fill="both")

        text_widget = tk.Text(content_frame, wrap="word", font=("Courier New", 12), bg="#fdfdfd", relief="flat")
        text_widget.insert("1.0", content)
        text_widget.configure(state="disabled")  # Make content read-only
        text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        # Footer section
        footer_frame = tk.Frame(doc_window, bg="#f4f5f7")
        footer_frame.pack(fill="x", pady=10)

        # Download button (always visible)
        def download_document():
            save_path = filedialog.asksaveasfilename(
                title="Save File",
                initialfile=f"{title}.txt",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")]
            )
            if save_path:
                with open(save_path, "w", encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo("Success", f"Document saved to {save_path}")

        download_button = tk.Button(
            footer_frame,
            text="Download",
            font=("Helvetica", 14, "bold"),
            bg="#4B89DC",
            fg="white",
            activebackground="#3A78C4",
            activeforeground="white",
            command=download_document
        )
        download_button.pack(pady=10, ipadx=20, ipady=5)
    else:
        messagebox.showerror("Error", "Document not found!")
