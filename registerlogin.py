import tkinter as tk
from tkinter import messagebox
import pymysql


# Database connection
def connect_to_db():
    return pymysql.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="admin@123",  # Replace with your MySQL password
        database="userdb"  # Your database name
    )


# Insert the user data into the 'user' table
def register_user():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    if not username or not password or not email:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Username already exists!")
        conn.close()
        return

    query = "INSERT INTO user (username, password, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, password, email))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Registration successful!")
    clear_fields()
    show_login_widgets()


# Login User Function
def login_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))

    result = cursor.fetchone()

    print(f"🔍 Query Result: {result}")  # Debugging line

    if result:
        import userdash
        userdash.document_list_window()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

    conn.close()


# Show Register Widgets
def show_register_widgets():
    label_action.config(text="Register")
    entry_email_label.pack(pady=5)
    entry_email.pack(pady=5)
    register_button.pack(pady=10)
    login_button.pack_forget()


# Show Login Widgets
def show_login_widgets():
    label_action.config(text="Login")
    entry_email_label.pack_forget()
    entry_email.pack_forget()
    register_button.pack_forget()
    login_button.pack(pady=10)


# Clear Input Fields
def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_email.delete(0, tk.END)


# Main UI
window = tk.Tk()
window.title("Login / Register")
window.geometry("400x500")
window.configure(bg="#4B4376")  # Light blue background

# Main frame with a casual look
frame = tk.Frame(window, bg="#FFFFFF", pady=30, padx=30, relief="flat")
frame.pack(expand=True, pady=20, padx=20)

label_action = tk.Label(frame, text="Login", font=("Arial Black", 20, "bold"), fg="#6256CA")
label_action.pack(pady=10)

# Username Field
tk.Label(frame, text="Username:", font=("Arial Black", 12), bg="#FFFFFF", fg="#0B192C").pack(pady=5)
entry_username = tk.Entry(frame, font=("Arial Black", 12), width=30, relief="solid", bd=1, borderwidth=3)
entry_username.pack(pady=5)

# Password Field
tk.Label(frame, text="Password:", font=("Arial Black", 12), bg="#FFFFFF", fg="#0B192C").pack(pady=5)
entry_password = tk.Entry(frame, font=("Arial Black", 12), show="*", width=30, relief="solid", bd=1, borderwidth=3)
entry_password.pack(pady=5)

# Email Field (For Register)
entry_email_label = tk.Label(frame, text="Email ID:", font=("Arial Black", 12), bg="#FFFFFF", fg="#00796B")
entry_email = tk.Entry(frame, font=("Arial Black", 12), width=30, relief="solid", bd=1, borderwidth=3)

# Buttons with rounded edges and casual style
register_button = tk.Button(
    frame, text="Register", command=register_user,
    font=("Arial Black", 12, "bold"), bg="#9EDF9C", fg="#004D40",
    activebackground="#004D40", activeforeground="white", relief="raised", bd=3, width=20
)
login_button = tk.Button(
    frame, text="Login", command=login_user,
    font=("Arial Black", 12, "bold"), bg="#9EDF9C", fg="white",
    activebackground="#004D40", activeforeground="white", relief="raised", bd=3, width=20
)

# Default view is login
show_login_widgets()

# Switch between Register and Login view
switch_to_register = tk.Button(
    frame, text="New user? Register", command=show_register_widgets,
    bg="#424242",fg="#F7F7F8", font=("Arial Black", 10,), borderwidth=0
)
switch_to_register.pack(pady=5)

switch_to_login = tk.Button(
    frame, text="Back to Login", command=show_login_widgets,
    bg="#FFFFFF", fg="#2A3663", font=("Arial Black", 10,), borderwidth=0
)
switch_to_login.pack(pady=5)

window.mainloop()
