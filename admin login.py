import tkinter as tk 
from tkinter import messagebox
import pymysql
import admindash  # Import the admin dashboard module

# Database connection setup
def connect_to_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='admin@123',  # Replace with your MySQL password
        database='admin'  # Replace with your database name
    )

# Admin Login Function
def admin_login():
    admin_id = entry_admin_id.get()
    admin_password = entry_admin_password.get()

    # Check if fields are filled
    if not admin_id or not admin_password:
        messagebox.showerror("Error", "Both fields are required!")
        return

    # Verify admin credentials
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE admin_id = %s AND password = %s", (admin_id, admin_password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        window_login.destroy()  # Close the login window
        admindash.open_admin_dashboard()  # Open the admin dashboard
    else:
        messagebox.showerror("Error", "Invalid admin credentials!")

    conn.close()

# Main UI for Admin Login
window_login = tk.Tk()
window_login.title("Admin Login")
window_login.geometry("500x550")  # Increased height for better spacing

# Set light background color and general window styling
window_login.configure(bg="#F0F4F8")  # Light grayish-blue background

# Header Label
header_label = tk.Label(window_login, text="Welcome Admin", font=("Helvetica", 24, "bold"), fg="#1E88E5", bg="#F0F4F8")
header_label.pack(pady=20)

# Admin ID field label
label_admin_id = tk.Label(window_login, text="Admin ID:", font=("Arial", 14), fg="#333333", bg="#F0F4F8")
label_admin_id.pack(anchor="w", padx=50, pady=10)

# Admin ID input field
entry_admin_id = tk.Entry(window_login, font=("Arial", 14), bg="#FFFFFF", fg="#555555", relief="solid", bd=2, highlightthickness=1, highlightcolor="#42A5F5", highlightbackground="#B0BEC5")
entry_admin_id.pack(padx=50, pady=10, ipady=5, fill="x")

# Admin Password field label
label_admin_password = tk.Label(window_login, text="Admin Password:", font=("Arial", 14), fg="#333333", bg="#F0F4F8")
label_admin_password.pack(anchor="w", padx=50, pady=10)

# Admin Password input field
entry_admin_password = tk.Entry(window_login, font=("Arial", 14), bg="#FFFFFF", fg="#555555", relief="solid", bd=2, show="*", highlightthickness=1, highlightcolor="#42A5F5", highlightbackground="#B0BEC5")
entry_admin_password.pack(padx=50, pady=10, ipady=5, fill="x")

# Login Button
login_button = tk.Button(window_login, text="Login", command=admin_login, font=("Helvetica", 16, "bold"), bg="#42A5F5", fg="white", activebackground="#1E88E5", relief="raised", bd=4)
login_button.pack(pady=30)

window_login.mainloop()
