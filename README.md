# Doc Sharing Platform - Tkinter + MySQL Project

This is a simple Tkinter-based document sharing platform connected to a MySQL database. This project demonstrates backend skills using Python and MySQL. It allows users to log in/sign in, view, request, and download documents. The admin has additional features to add new documents and delete them by entering their document ID.

---

## Features

### User Features:
- **Register/Login**: Users can create an account and log in.
- **View Documents**: After logging in, users can view a list of available documents.
- **Request Documents**: Users can request documents and download them locally.

### Admin Features:
- **Admin Login**: Admin can log in with credentials.
- **Add Documents**: Admin can add new documents to the platform.
- **Delete Documents**: Admin can delete documents by entering the document ID.

---

Prerequisites
Before you begin, ensure you have the following installed:

Python (check installation by running python --version)

MySQL (to host the databases)

Git (to clone the repository)

Step 1: Clone the Repository
Open a terminal or command prompt.

Run the following command to clone the repository:
git clone https://github.com/Vicky8472/doc-sharing-platform.git

Navigate to the project directory:
cd doc-sharing-platform

Step 2: Install Required Libraries
Install the pymysql library using pip:
pip install pymysql

Step 3: Set Up MySQL Database
Open MySQL and create two databases:

admin

userdb

Create the required tables in each database:

----
For the admin database:
   CREATE TABLE docs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT
);
---

For the userdb database:
----
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255)
);
-----

Step 4: Configure Database Connection
1.Open the following Python files in your project:

index.py (previously registerlogin.py)

adminlogin.py

admin dash.py

userdash.py

ud2.py

ud3.py

2.Update the database connection details in each file with your MySQL credentials. Here’s an example:
 --------
 connection = pymysql.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="userdb"  # Use "admin" for admin database connection
)
---------
Step 5: Run the Application
To start the user interface, run:
python index.py

To access the admin dashboard, run:
python adminlogin.py

For other functionalities (e.g., user dashboard, admin actions), run the respective files:

python userdash.py

python admin dash.py

python ud2.py

python ud3.py

Step 6: Interact with the Application
For Users:
Register a new account.

Log in using your credentials.

View or download documents.

For Admin:
Log in with admin credentials.

Add new documents or delete existing ones by entering the document ID.

Troubleshooting
Ensure MySQL is running and the databases/tables are correctly set up.

Double-check the database connection details in all Python files.

Make sure all required libraries are installed.




