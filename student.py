from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE FUNCTIONS ----------------

def add_student():

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students(name,age,gender,course,email,phone,address)
    VALUES(?,?,?,?,?,?,?)
    """,(
        name_entry.get(),
        age_entry.get(),
        gender_entry.get(),
        course_entry.get(),
        email_entry.get(),
        phone_entry.get(),
        address_entry.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success","Student Added Successfully")

    show_students()
    clear()

def clear():
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    gender_entry.delete(0,END)
    course_entry.delete(0,END)
    email_entry.delete(0,END)
    phone_entry.delete(0,END)
    address_entry.delete(0,END)

def show_students():

    conn=sqlite3.connect("student.db")
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM students")

    rows=cursor.fetchall()

    student_table.delete(*student_table.get_children())

    for row in rows:
        student_table.insert("",END,values=row)

    conn.close()

# ---------------- WINDOW ----------------
selected_id = None

def get_cursor(event):
    global selected_id

    row = student_table.focus()

    data = student_table.item(row)

    values = data["values"]

    if values:

        selected_id = values[0]

        clear()

        name_entry.insert(0, values[1])
        age_entry.insert(0, values[2])
        gender_entry.insert(0, values[3])
        course_entry.insert(0, values[4])
        email_entry.insert(0, values[5])
        phone_entry.insert(0, values[6])
        address_entry.insert(0, values[7])

def update_student():

    if selected_id is None:
        messagebox.showerror("Error", "Select a student first")
        return

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, gender=?, course=?, email=?, phone=?, address=?
    WHERE id=?
    """,(
        name_entry.get(),
        age_entry.get(),
        gender_entry.get(),
        course_entry.get(),
        email_entry.get(),
        phone_entry.get(),
        address_entry.get(),
        selected_id
    ))

    conn.commit()
    conn.close()

    show_students()
    clear()

def delete_student():

    if selected_id is None:
        messagebox.showerror("Error", "Select a student first")
        return

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (selected_id,))

    conn.commit()
    conn.close()

    show_students()
    clear()

def search_student():

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ?",
        ('%' + name_entry.get() + '%',)
    )

    rows = cursor.fetchall()

    student_table.delete(*student_table.get_children())

    for row in rows:
        student_table.insert("", END, values=row)

    conn.close()

root=Tk()

root.title("Student Management System")
root.geometry("1100x600")
root.configure(bg="lightblue")

Label(root,text="Student Management System",
      font=("Arial",20,"bold"),
      bg="lightblue",
      fg="blue").pack(pady=10)

Label(root,text="Name").place(x=20,y=70)
name_entry=Entry(root,width=25)
name_entry.place(x=120,y=70)

Label(root,text="Age").place(x=20,y=110)
age_entry=Entry(root,width=25)
age_entry.place(x=120,y=110)

Label(root,text="Gender").place(x=20,y=150)
gender_entry=Entry(root,width=25)
gender_entry.place(x=120,y=150)

Label(root,text="Course").place(x=20,y=190)
course_entry=Entry(root,width=25)
course_entry.place(x=120,y=190)

Label(root,text="Email").place(x=20,y=230)
email_entry=Entry(root,width=25)
email_entry.place(x=120,y=230)

Label(root,text="Phone").place(x=20,y=270)
phone_entry=Entry(root,width=25)
phone_entry.place(x=120,y=270)

Label(root,text="Address").place(x=20,y=310)
address_entry=Entry(root,width=25)
address_entry.place(x=120,y=310)

Button(root,text="Add",width=15,bg="green",fg="white",
command=add_student).place(x=40,y=370)

Button(root,text="Clear",width=15,
command=clear).place(x=200,y=370)

Button(root, text="Update", width=15, bg="blue", fg="white",
       command=update_student).place(x=40, y=420)

Button(root, text="Delete", width=15, bg="red", fg="white",
       command=delete_student).place(x=200, y=420)

Button(root, text="Search", width=15, bg="orange", fg="white",
       command=search_student).place(x=40, y=470)

Button(root, text="Exit", width=15,
       command=root.destroy).place(x=200, y=470)

# ---------------- TABLE ----------------

columns=("ID","Name","Age","Gender","Course","Email","Phone","Address")

student_table=ttk.Treeview(root,columns=columns,show="headings")

for col in columns:
    student_table.heading(col,text=col)
    student_table.column(col,width=100)

student_table.place(x=420,y=70,width=650,height=450)
student_table.bind("<ButtonRelease-1>", get_cursor)


show_students()

root.mainloop()
