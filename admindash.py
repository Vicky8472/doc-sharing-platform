import tkinter as tk
from tkinter import filedialog, messagebox
import pymysql

# Database connection setup
def connect_to_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='admin@123',  # Replace with your MySQL password
        database='admin'  # Replace with your database name
    )

# Admin Dashboard UI
def open_admin_dashboard():
    def add_document():
        add_window = tk.Toplevel(window_dashboard)
        add_window.title("Add Document")
        add_window.geometry("400x300")
        add_window.configure(bg="#E1F5FE")  # Light cyan background for Add Document window

        # Title and description fields
        tk.Label(add_window, text="Document Title:", font=("Helvetica", 12, "bold"), bg="#E1F5FE").pack(pady=5)
        title_entry = tk.Entry(add_window, width=30, font=("Helvetica", 12))
        title_entry.pack(pady=5)

        tk.Label(add_window, text="Description:", font=("Helvetica", 12, "bold"), bg="#E1F5FE").pack(pady=5)
        desc_entry = tk.Entry(add_window, width=30, font=("Helvetica", 12))
        desc_entry.pack(pady=5)

        # Upload file function
        def upload_file():
            file_path = filedialog.askopenfilename(title="Select a Document")
            if file_path:
                with open(file_path, 'rb') as file:
                    file_content = file.read()

                title = title_entry.get()
                desc = desc_entry.get()

                if not title or not desc:
                    messagebox.showerror("Error", "All fields are required!")
                    return

                conn = connect_to_db()
                cursor = conn.cursor()
                query = "INSERT INTO docs (title, description, content) VALUES (%s, %s, %s)"
                cursor.execute(query, (title, desc, file_content))
                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Document added successfully!")
                add_window.destroy()

        tk.Button(add_window, text="Upload and Save Document", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", command=upload_file).pack(pady=10)

    def delete_document():
        delete_window = tk.Toplevel(window_dashboard)
        delete_window.title("Delete Document")
        delete_window.geometry("300x200")
        delete_window.configure(bg="#FFEBEE")  # Light red-pink background for Delete Document window

        # Document ID input field
        tk.Label(delete_window, text="Document ID:", font=("Helvetica", 12, "bold"), bg="#FFEBEE").pack(pady=5)
        doc_id_entry = tk.Entry(delete_window, font=("Helvetica", 12))
        doc_id_entry.pack(pady=5)

        # Confirm deletion function
        def confirm_delete():
            doc_id = doc_id_entry.get()

            if not doc_id:
                messagebox.showerror("Error", "Document ID is required!")
                return

            conn = connect_to_db()
            cursor = conn.cursor()
            query = "DELETE FROM docs WHERE id = %s"
            cursor.execute(query, (doc_id,))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Document deleted successfully!")
            delete_window.destroy()

        tk.Button(delete_window, text="Delete", font=("Helvetica", 12, "bold"), bg="#F44336", fg="white", relief="raised", command=confirm_delete).pack(pady=10)

    # Main admin dashboard window
    window_dashboard = tk.Tk()
    window_dashboard.title("Admin Dashboard")
    window_dashboard.geometry("500x400")  # Adjusted size for a more spacious layout
    window_dashboard.configure(bg="#FFCDD2")  # Light pink background for the main window

    # Admin Dashboard header
    tk.Label(window_dashboard, text="Admin Dashboard", font=("Helvetica", 24, "bold"), fg="white", bg="#FFCDD2").pack(pady=20)

    # Buttons for Add and Delete Document
    tk.Button(window_dashboard, text="Add Document", width=20, font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", relief="raised", command=add_document).pack(pady=10)
    tk.Button(window_dashboard, text="Delete Document", width=20, font=("Helvetica", 14, "bold"), bg="#F44336", fg="white", relief="raised", command=delete_document).pack(pady=10)

    window_dashboard.mainloop()

# Call the function to open the admin dashboard
#open_admin_dashboard()
