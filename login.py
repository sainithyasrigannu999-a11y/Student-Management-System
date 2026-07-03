from tkinter import *
from tkinter import messagebox
import sqlite3

def login():

    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM login WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


root = Tk()

root.title("Login")
root.geometry("400x300")
root.configure(bg="lightblue")

Label(root,
      text="Student Management System",
      font=("Arial",16,"bold"),
      bg="lightblue").pack(pady=20)

Label(root,text="Username",bg="lightblue").pack()

username_entry = Entry(root,width=30)
username_entry.pack()

Label(root,text="Password",bg="lightblue").pack(pady=10)

password_entry = Entry(root,width=30,show="*")
password_entry.pack()

Button(root,
       text="Login",
       width=15,
       command=login).pack(pady=20)

root.mainloop()
