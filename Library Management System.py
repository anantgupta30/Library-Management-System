from tkinter import *
from tkinter import messagebox
import os
import mysql.connector as db
from tkinter import ttk


def One_submit_button_stu():
    try:
        global d_name
        global tv
        global One_entry
        global adminno_entry
        global adminno
        global stu_tv
        global ref_entry

        ID = One_entry.get()
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="672526", database=d_name)
        cursor = mydb.cursor()
        cursor.execute("select * from student_data where  Reference_no=%s" % ID)
        one = cursor.fetchall()
        if one == []:
            messagebox.showerror("Error", "No row with entered reference no. exist..")

        for i in one:
            stu_tv.insert("", 'end', values=i)

    except:
        messagebox.showerror("ERROR", """1. Please make sure you have entered and integer value.
        2. student_Library table exist in your database """)


def show_stu_one():
    global stu
    global stu_tv
    global One_entry

    showone_win = Toplevel(stu)
    showone_win.title("ONE RECORD")
    showone_win.geometry("1300x250")
    # frame_one= LabelFrame(showone_win)
    # frame_one.grid()
    Label(showone_win, text="Enter exact Reference No. below to display the Particular record:-",
          font=("lucida grande", "14")).grid(row=0, column=0, padx=50)
    One_entry = Entry(showone_win, width=20, borderwidth=3)
    One_entry.grid(row=1, column=0, pady=10)

    One_submit_btn = Button(showone_win, text="submit", command=One_submit_button_stu, bg="RosyBrown1")
    One_submit_btn.grid(row=2, column=0, pady=10)

    stu_tv = ttk.Treeview(showone_win, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show="headings", height="5")
    stu_tv.grid(row=3, pady=30)

    stu_tv.heading(1, text='Reference_No')
    stu_tv.column(1, width=100)
    stu_tv.heading(2, text='Admission_No')
    stu_tv.column(2, width=100)
    stu_tv.heading(3, text='student_name')
    stu_tv.column(3, width=130)
    stu_tv.heading(4, text='class_sec')
    stu_tv.column(4, width=70)
    stu_tv.heading(5, text='stream')
    stu_tv.column(5, width=70)
    stu_tv.heading(6, text='Book_borrowed')
    stu_tv.column(6, width=140)
    stu_tv.heading(7, text='bookID')
    stu_tv.column(7, width=70)
    stu_tv.heading(8, text='Author_name')
    stu_tv.column(8, width=140)
    stu_tv.heading(9, text='bookMRP')
    stu_tv.column(9, width=70)
    stu_tv.heading(10, text='Date_borrowed')
    stu_tv.column(10, width=100)
    stu_tv.heading(11, text='Due_Date')
    stu_tv.column(11, width=80)
    stu_tv.heading(12, text='State')
    stu_tv.column(12, width=100)
    stu_tv.heading(13, text='Phone_No')
    stu_tv.column(13, width=110)

    # scrollbar vertical
    scroll_v = ttk.Scrollbar(showone_win, orient="vertical", command=stu_tv.yview)
    stu_tv.configure(yscroll=scroll_v.set)
    scroll_v.grid(row=3, column=12, sticky="ns")


def show_one_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno

        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=show_stu_one)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def showone_win():
    global stu
    global stu_add
    global database_name
    global adminno_entry

    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-UPDATE")
    stu_add.geometry("250x400")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=show_one_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def show_stu_all():
    global stu
    global d_name
    global stu_tv

    showall_win = Toplevel(stu)
    showall_win.title("ALL RECORDS")
    showall_win.geometry("1300x550")
    show_frame = LabelFrame(showall_win)
    show_frame.grid()

    Label(show_frame, text="ALL RECORDS", font=("lucida grande", "20")).grid()
    stu_tv = ttk.Treeview(showall_win, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show="headings",
                          height="15")
    stu_tv.grid()

    stu_tv.heading(1, text='Reference_No')
    stu_tv.column(1, width=100)
    stu_tv.heading(2, text='Admission_No')
    stu_tv.column(2, width=100)
    stu_tv.heading(3, text='student_name')
    stu_tv.column(3, width=130)
    stu_tv.heading(4, text='class_sec')
    stu_tv.column(4, width=70)
    stu_tv.heading(5, text='stream')
    stu_tv.column(5, width=70)
    stu_tv.heading(6, text='Book_borrowed')
    stu_tv.column(6, width=140)
    stu_tv.heading(7, text='bookID')
    stu_tv.column(7, width=70)
    stu_tv.heading(8, text='Author_name')
    stu_tv.column(8, width=140)
    stu_tv.heading(9, text='bookMRP')
    stu_tv.column(9, width=70)
    stu_tv.heading(10, text='Date_borrowed')
    stu_tv.column(10, width=100)
    stu_tv.heading(11, text='Due_Date')
    stu_tv.column(11, width=80)
    stu_tv.heading(12, text='State')
    stu_tv.column(12, width=100)
    stu_tv.heading(13, text='Phone_No')
    stu_tv.column(13, width=110)
    # scrollbar vertical

    scroll_v = ttk.Scrollbar(showall_win, orient="vertical", command=stu_tv.yview)
    stu_tv.configure(yscroll=scroll_v.set)
    scroll_v.grid(row=0, column=13, sticky="ns")

    d_name = database_name.get()
    mydb = db.connect(host="localhost", user="root", password="root1234", database=d_name)
    cursor = mydb.cursor()
    cursor.execute("select * from student_data")
    result = cursor.fetchall()

    for i in result:
        stu_tv.insert("", 'end', values=i)


def show_all_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno

        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=show_stu_all)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def show_allstu_submit():
    global stu
    global stu_add
    global database_name
    global adminno_entry

    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-UPDATE")
    stu_add.geometry("250x400")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=show_all_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def save_updated_data():
    global frame_Dbase
    global stu
    global stu_add
    global d_name
    global database_name_entry
    global database_name
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global ref_entry
    global state_entry

    dname = database_name.get()

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get()
    P_no = Phoneno_entry.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    add = "update student_data set admission_no=%s,student_name=%s,class_section=%s,stream=%s,book_borrowed=%s,bookID=%s,author_name=%s,bookMRP=%s,date_borrowed=%s,Due_date=%s,state=%s,phoneNo=%s where Reference_no =%s"
    data = (
    adminno, studentname, class_sec, stu_stream, borrowB, B_ID, Author_name, mrp, borrow_D, D_date, state_stu, P_no,
    ref_no)
    cursor.execute(add, data)
    mydb.commit()
    messagebox.showinfo("UPDATED", "DATA UPDATED SUCCESSFULLY")

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", state=DISABLED)
    save.grid(pady=10, sticky=NSEW, row=13, column=1)


def Save_stu_Rec():
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global delete_stu_win
    global stu
    global dname
    global frame_Dbase
    global adminno
    global ref_entry
    global state_entry

    dname = database_name.get()

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get
    P_no = Phoneno_entry.get()

    mydb = db.connect(host="localhost", password="root1234", user="", database=dname)
    cursor = mydb.cursor()
    cursor.execute("select * from student_data where reference_no=%s" % ref_no)
    all = cursor.fetchall()

    for result in all:
        adminno_entry.insert(0, result[1])
        stuname_entry.insert(0, result[2])
        classec_entry.insert(0, result[3])
        stream_entry.insert(0, result[4])
        Bookborrow_entry.insert(0, result[5])
        bookid_entry.insert(0, result[6])
        Author_entry.insert(0, result[7])
        MRP_entry.insert(0, result[8])
        Dateborrwed_entry.insert(0, result[9])
        Duedate_entry.insert(0, result[10])
        state_entry.insert(0, result[11])
        Phoneno_entry.insert(0, result[12])

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", command=save_updated_data,
                  state=ACTIVE)
    save.grid(pady=10, sticky=NSEW, row=13, column=1)


def update_win():
    global frame_Dbase
    global stu
    global stu_add
    global d_name
    global stu_update
    global database_name_entry
    global database_name
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global ref_entry
    global state_entry

    stu_update = Toplevel(stu)
    stu_update.geometry("600x700")
    stu_update.title("UPDATE RECORD")

    frame_Dbase = LabelFrame(stu_update, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    Label(stu_update, text="Only enter Reference no. and rest fields program will fill on its own. ",
          font=("lucida grande", "10")).grid()
    Label(stu_update,
          text="Note:- 1.only one record is going to update at once and you can not change the reference no. ",
          font=("lucida grande", "10")).grid()
    Label(stu_update, text="    2.You have to entered exact reference no. otherwise it will not fill the entry fields ",
          font=("lucida grande", "10")).grid()

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="Done", borderwidth=2, padx=14, bg="RosyBrown1", command=Save_stu_Rec)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=upd_destroy)
    back_btn.grid(pady=10, row=13, column=0)


def upd_destroy():
    global stu_update
    stu_update.withdraw()


def stu_update_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno
        global ref_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=update_win)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def update_stu():
    global stu
    global stu_add
    global database_name
    global adminno_entry
    global ref_entry
    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-UPDATE")
    stu_add.geometry("250x400")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=stu_update_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def student_Delete():
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global delete_stu_win
    global stu
    global dname
    global frame_Dbase
    global adminno
    global ref_entry
    global state_entry

    dname = database_name.get()

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry
    P_no = Phoneno_entry.get()

    mydb = db.connect(host="localhost", password="root1234", user="root", database=dname)
    cursor = mydb.cursor()
    cursor.execute("select * from student_data where reference_no=%s" % ref_no)
    all = cursor.fetchall()

    # ref_entry.delete(0, END)
    # adminno_entry.delete(0, END)
    # stuname_entry.delete(0, END)
    # classec_entry.delete(0, END)
    # stream_entry.delete(0, END)
    # Bookborrow_entry.delete(0, END)
    # Author_entry.delete(0, END)
    # bookid_entry.delete(0, END)
    # Dateborrwed_entry.delete(0, END)
    # Duedate_entry.delete(0, END)
    # MRP_entry.delete(0, END)
    # state_entry.delete(0,END)
    # Phoneno_entry.delete(0, END)

    for result in all:
        # ref_entry.insert(0,result[0])
        adminno_entry.insert(0, result[1])
        stuname_entry.insert(0, result[2])
        classec_entry.insert(0, result[3])
        stream_entry.insert(0, result[4])
        Bookborrow_entry.insert(0, result[5])
        bookid_entry.insert(0, result[6])
        Author_entry.insert(0, result[7])
        MRP_entry.insert(0, result[8])
        Dateborrwed_entry.insert(0, result[9])
        Duedate_entry.insert(0, result[10])
        state_entry.insert(0, result[11])
        Phoneno_entry.insert(0, result[12])

    a = messagebox.askquestion("choice", "Do you want to Delete the entered information")
    if a == "yes":
        cursor.execute("delete from student_data where reference_no= %s" % ref_no)
        mydb.commit()
        messagebox.showinfo("DELETED", "DATA DELETED SUCCESSFULLY")

        ref_entry.delete(0, END)
        adminno_entry.delete(0, END)
        stuname_entry.delete(0, END)
        classec_entry.delete(0, END)
        stream_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        Author_entry.delete(0, END)
        bookid_entry.delete(0, END)
        Dateborrwed_entry.delete(0, END)
        Duedate_entry.delete(0, END)
        MRP_entry.delete(0, END)
        state_entry.delete(0, END)
        Phoneno_entry.delete(0, END)


def del_destroy():
    global delete_stu_win
    delete_stu_win.withdraw()


def delete_stu_rec():
    global delete_stu_win
    global stu
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global adminno
    global ref_entry
    global state_entry
    delete_stu_win = Toplevel(stu)
    delete_stu_win.geometry("600x550")
    delete_stu_win.title("DELETE RECORD")

    frame_Dbase = LabelFrame(delete_stu_win, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    stu_add.withdraw()

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="Done", borderwidth=2, padx=14, bg="RosyBrown1", command=student_Delete)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=del_destroy)
    back_btn.grid(pady=10, row=13, column=0)


def stu_database_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=delete_stu_rec)
        next_add_button.grid(row=2, column=1)
    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def stu_database_delete():
    global stu
    global stu_add
    global database_name
    global adminno_entry
    global ref_entry
    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-DELETE")
    stu_add.geometry("600x450")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=stu_database_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def add_back_btn():
    global stu_add_new
    stu_add_new.withdraw()


def add_recto_table():
    global stu_add_new
    global database_name_entry
    global frame_Dbase
    global stu
    global bookID1
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global d_name
    global stu_add_new
    global adminno
    global ref_entry
    global state_entry

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get()
    P_no = Phoneno_entry.get()

    # frame_Dbase = LabelFrame(stu_add_new, borderwidth=5, height=5)
    # frame_Dbase.grid(padx=80, pady=10)

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        add = cursor.execute(
            "insert into student_data values({},{},'{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',{})".format(ref_no,
                                                                                                             adminno,
                                                                                                             studentname,
                                                                                                             class_sec,
                                                                                                             stu_stream,
                                                                                                             borrowB,
                                                                                                             B_ID,
                                                                                                             Author_name,
                                                                                                             mrp,
                                                                                                             borrow_D,
                                                                                                             D_date,
                                                                                                             state_stu,
                                                                                                             P_no))
        # data = (bookID, bookname, authorname, purdate, publishername, bookMRP, state, rackno)
        cursor.execute(add)
        messagebox.showinfo("", "data inserted!!!")

        mydb.commit()
        ref_entry.delete(0, END)
        adminno_entry.delete(0, END)
        stuname_entry.delete(0, END)
        classec_entry.delete(0, END)
        stream_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        Author_entry.delete(0, END)
        bookid_entry.delete(0, END)
        Dateborrwed_entry.delete(0, END)
        Duedate_entry.delete(0, END)
        MRP_entry.delete(0, END)
        state_entry.delete(0, END)
        Phoneno_entry.delete(0, END)

    except:
        messagebox.showerror("", """Error in some Entry feild.......Data not inserted.Try again!!!!.
            Note: please make sure you have enter values according to correct datatype of respective fields or you have left entry field blank""")


def add_rec():
    global adminno
    global stu
    global stu_add
    global d_name
    global database_name_entry
    global database_name
    global stu_add_new
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global ref_entry
    global state_entry

    stu_add_new = Toplevel(stu_add)
    stu_add_new.geometry("600x600")
    stu_add_new.title("ADD RECORDS")

    Label(stu_add_new, text="Reference No. need to be unique everytime Otherwise you will get an Error",
          font=("lucida grande", "10")).grid()

    frame_Dbase = LabelFrame(stu_add_new, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    stu_add.withdraw()

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    Duedate_entry.insert(0, "YYYY-MM-DD")
    Dateborrwed_entry.insert(0, "YYYY-MM-DD")

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=add_recto_table)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=add_back_btn)
    back_btn.grid(pady=10, row=13, column=0)


def sub_add_rec():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=add_rec)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def stu_add_record():
    global stu
    global stu_add
    global database_name
    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-ADD")
    stu_add.geometry("600x450")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=sub_add_rec, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def add_rec_for_stu():
    global database_name_entry
    global frame_Dbase
    global stu
    global bookID1
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global d_name
    global adminno
    global ref_entry
    global state_entry

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get()
    P_no = Phoneno_entry.get()

    frame_Dbase = LabelFrame(database_name_entry, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    d_name = database_name.get()
    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    add = cursor.execute(
        "insert into student_data values({},{},'{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',{})".format(ref_no,
                                                                                                         adminno,
                                                                                                         studentname,
                                                                                                         class_sec,
                                                                                                         stu_stream,
                                                                                                         borrowB, B_ID,
                                                                                                         Author_name,
                                                                                                         mrp, borrow_D,
                                                                                                         D_date,
                                                                                                         state_stu,
                                                                                                         P_no))
    # data = (bookID, bookname, authorname, purdate, publishername, bookMRP, state, rackno)
    cursor.execute(add)
    messagebox.showinfo("", "data inserted!!!")
    mydb.commit()

    ref_entry.delete(0, END)
    adminno_entry.delete(0, END)
    stuname_entry.delete(0, END)
    classec_entry.delete(0, END)
    stream_entry.delete(0, END)
    Bookborrow_entry.delete(0, END)
    Author_entry.delete(0, END)
    bookid_entry.delete(0, END)
    Dateborrwed_entry.delete(0, END)
    Duedate_entry.delete(0, END)
    MRP_entry.delete(0, END)
    state_entry.delete(0, END)
    Phoneno_entry.delete(0, END)

    # except:
    #     messagebox.showerror("", """Error in some Entry feild.......Data not inserted.Try again!!!!.
    #     Note: please make sure you have enter values according to correct datatype of respective fields or you have left entry field blank""")


def submit_stu_base():
    global d_name
    global database_name
    global database_name_entry
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global adminno
    global ref_entry
    global state_entry

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        cursor.execute("""CREATE TABLE student_data(Reference_no int(30) primary key not null,
            Admission_no int(20) not null,
            student_name varchar(30),
            class_section  varchar(20)  not null ,
            stream  char(15) default "NONE" ,
            Book_borrowed varchar(35) not null,
            bookID int(10) not null,
            author_name char(40),
            bookMRP decimal(10) default "0.00",
            Date_borrowed DATE not null,
            Due_date DATE not null,
            state char(20) ,
            PhoneNo bigint(18))""")
        messagebox.showinfo("", "Table created sucessfully")
        mydb.commit()

    except:
        messagebox.showerror("Unknown!!!!",
                             "Unknown database or Table with name student_data already exist in this database")
        database_name_entry.withdraw()

    frame_Dbase = LabelFrame(database_name_entry, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    Duedate_entry.insert(0, "YYYY-MM-DD")
    Dateborrwed_entry.insert(0, "YYYY-MM-DD")

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=add_rec_for_stu)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)
    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back)
    back_btn.grid(pady=10, row=13, column=0)


def crea_stu_table():
    global stu
    global d_name
    global database_name
    global database_name_entry
    global submit_button
    a = messagebox.askquestion("DataBase", "Do you have any database in which you want to create Student table?")
    if a == "yes":
        database_name_entry = Toplevel(stu)
        database_name_entry.geometry("600x650")
        database_label = Label(database_name_entry, text="Enter  Database  name :-")
        database_label.grid()

        database_name = Entry(database_name_entry, width=20, borderwidth=2)
        database_name.grid()

        submit_button = Button(database_name_entry, text="submit", command=submit_stu_base, bg="RosyBrown1")
        submit_button.grid(pady=5)

    else:
        b = messagebox.askquestion("Choice", "Would you like to create one")

        if b == "yes":
            database_name_entry = Toplevel(stu)
            database_name_entry.geometry("600x450")
            database_label = Label(database_name_entry, text="Enter  Database  name :-")
            database_label.grid()

            database_name = Entry(database_name_entry, width=20, borderwidth=2)
            database_name.grid()

            submit_button = Button(database_name_entry, text="submit", command=submit_dname, bg="RosyBrown1")
            submit_button.grid(pady=5)


def window_for_stu_system():
    global stu
    stu = Tk()
    stu.geometry("550x400")
    stu.title("STUDENT WINDOW")
    # first heading
    name = Label(stu, text="LIBRARY MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(stu, text="PLATO PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(stu, padx=50, pady=50)
    frame.grid(row=3, column=0)
    add_record = Button(frame, text="Add record", padx=20, pady=2, command=stu_add_record)
    delete_record = Button(frame, text="Delete record", padx=20, pady=2, command=stu_database_delete)
    update_record = Button(frame, text="Update record", padx=11, pady=2, command=update_stu)
    showall_record = Button(frame, text="Show All record", padx=11, pady=2, command=show_allstu_submit)
    showone_record = Button(frame, text="Show One record", padx=7, pady=2, command=showone_win)
    stu_table = Button(frame, text="Create student table", padx=2, pady=2, command=crea_stu_table)

    add_record.grid(row=0, column=0, padx=30, pady=9)
    delete_record.grid(row=0, column=1, padx=15, pady=9)
    update_record.grid(row=1, column=0, pady=9, padx=30)
    showall_record.grid(row=1, column=1, padx=15, pady=9)
    showone_record.grid(row=2, column=0, pady=9)
    stu_table.grid(row=2, column=1, padx=30)

    stu.mainloop()


def One_submit_button():
    try:
        global d_name
        global tv
        global One_entry
        global show_one_window
        ID = One_entry.get()
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=d_name)
        cursor = mydb.cursor()
        cursor.execute("select * from library_system where  bookID=%s" % ID)
        one = cursor.fetchone()
        tv.insert("", 'end', values=one)

    except:
        messagebox.showerror("ERROR!!", "Invalid datatype entered or record with entered ID not exist...")


def show_one():
    global d_name
    global tv
    global One_entry
    global show_one_window

    show_one_window = Toplevel(root)
    show_one_window.geometry("1050x250")
    show_one_window.resizable(False, False)
    show_one_window.title("ONE RECORDS")
    frame_all = Frame(show_one_window)
    frame_all.grid(row=2)

    One_label = Label(show_one_window, text="Enter BookID of the record which you want to display:-",
                      font=("lucida grade", "12"), fg="coral")
    One_label.grid(row=0, column=0)

    One_entry = Entry(show_one_window, width=20, borderwidth=3)
    One_entry.grid(row=1, column=0)

    One_submit_btn = Button(show_one_window, text="submit", command=One_submit_button, bg="RosyBrown1")
    One_submit_btn.grid(row=2, column=0)

    tv = ttk.Treeview(frame_all, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="15")
    tv.grid(pady=20)

    tv.heading(1, text="bookID")
    tv.column(1, width=130)
    tv.heading(2, text="book_name")
    tv.column(2, width=130)
    tv.heading(3, text="author_name")
    tv.column(3, width=130)
    tv.heading(4, text="purcahse_date")
    tv.column(4, width=130)
    tv.heading(5, text="publisher_name")
    tv.column(5, width=130)
    tv.heading(6, text="bookMRP")
    tv.column(6, width=130)
    tv.heading(7, text="state")
    tv.column(7, width=130)
    tv.heading(8, text="Rackno")
    tv.column(8, width=100)


def submit_one_rec():
    try:
        global d_name
        global database_name_entry
        global d_name
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE, command=show_one)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def show_one_rec():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=submit_one_rec, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def show_all():
    global d_name

    show_all_window = Toplevel(root)
    show_all_window.geometry("1050x550")
    # show_all_window.resizable(False,False)
    show_all_window.title("ALL RECORDS")
    frame_all = Frame(show_all_window)
    frame_all.grid()
    # scroll_frame= LabelFrame(frame_all)
    # scroll_frame.grid(column=10,sticky="ns")

    Label(show_all_window, text="All Records ", font=("lucida grade", "30")).grid(sticky=N, row=0, column=0)

    tv = ttk.Treeview(frame_all, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="15")
    tv.grid(pady=80)
    # #scrollbar
    scrollbar_view = ttk.Scrollbar(frame_all, orient="vertical", command=tv.yview)
    tv.configure(yscroll=scrollbar_view.set)
    scrollbar_view.grid(row=0, column=9, sticky="ns")

    tv.heading(1, text="bookID")
    tv.column(1, width=130)
    tv.heading(2, text="book_name")
    tv.column(2, width=130)
    tv.heading(3, text="author_name")
    tv.column(3, width=130)
    tv.heading(4, text="purcahse_date")
    tv.column(4, width=130)
    tv.heading(5, text="publisher_name")
    tv.column(5, width=130)
    tv.heading(6, text="bookMRP")
    tv.column(6, width=130)
    tv.heading(7, text="state")
    tv.column(7, width=130)
    tv.heading(8, text="Rackno")
    tv.column(8, width=100)

    d_name = database_name.get()
    mydb = db.connect(host="localhost", user="root", password="root1234", database=d_name)
    cursor = mydb.cursor()
    cursor.execute("select * from library_system")
    result = cursor.fetchall()

    for i in result:
        tv.insert("", 'end', values=i)


def submit_show_all():
    try:
        global d_name
        global database_name_entry
        global d_name
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE, command=show_all)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def show_all_submit():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=submit_show_all, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def save_record():
    global bookID1
    global bookname
    global authorname
    global purdate
    global publishername
    global bookMRP
    global state
    global rackno

    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    d_name = database_name.get()
    bookID1 = bookID_entry.get()

    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    add = "update library_system set  book_name=%s,author_name=%s,purchase_date=%s,publisher_name=%s,book_MRP=%s,state=%s,rack_no=%s where bookID =%s"
    data = (bookname, authorname, purdate, publishername, bookMRP, state, rackno, bookID1)
    cursor.execute(add, data)
    mydb.commit()
    messagebox.showinfo("UPDATED", "ROW UPDATED SUCCESSFULLY")

    bookID_entry.delete(0, END)
    bookname_entry.delete(0, END)
    authorname_entry.delete(0, END)
    purdate_entry.delete(0, END)
    Bookborrow_entry.delete(0, END)
    bookMRP_entry.delete(0, END)
    state_entry.delete(0, END)
    rackno_entry.delete(0, END)

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", state=DISABLED)
    save.grid(pady=10, sticky=NSEW, row=8, column=1)


def done_record():
    global frame_Dbase
    global delete_record_window
    global database_name
    global d_name
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    global bookID1
    global bookname
    global authorname
    global purdate
    global publishername
    global bookMRP
    global state
    global rackno

    bookID1 = bookID_entry.get()
    d_name = database_name.get()

    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    a = cursor.execute("select * from library_system where bookID= %s" % bookID1)
    result = cursor.fetchall()

    for result in result:
        # bookID_entry.insert(0,result[0])
        bookname_entry.insert(0, result[1])
        authorname_entry.insert(0, result[2])
        purdate_entry.insert(0, result[3])
        Bookborrow_entry.insert(0, result[4])
        bookMRP_entry.insert(0, result[5])
        state_entry.insert(0, result[6])
        rackno_entry.insert(0, result[7])

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", command=save_record,
                  state=ACTIVE)
    save.grid(pady=10, sticky=NSEW, row=8, column=1)


def submit_update():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=sub_update, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def update_record_window():
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry
    global frame_Dbase
    global update_record_window
    update_record_window = Toplevel(root)
    update_record_window.geometry("600x450")
    update_record_window.title("UPDATE RECORD")
    Label(update_record_window, text="Only enter BookID and rest fields program will fill on its own ",
          font=("lucida grande", "10")).grid()
    Label(update_record_window,
          text="Only One record at a time. To update again click on 'back' and open this window again ",
          font=("lucida grande", "10")).grid()
    frame_Dbase = LabelFrame(update_record_window, text="", borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=20)
    # Label(update_record_window, text="", font=("lucida grande", "15")).grid()
    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    # purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="Done", borderwidth=2, padx=14, bg="RosyBrown1", command=done_record)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)
    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back_update)
    back_btn.grid(pady=10, row=8, column=0)


def back_update():
    global update_record_window
    update_record_window.withdraw()


def delete_rec():
    global delete_record_window
    global database_name
    global d_name
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    bookname_entry.delete(0, END)
    authorname_entry.delete(0, END)
    purdate_entry.delete(0, END)
    Bookborrow_entry.delete(0, END)
    bookMRP_entry.delete(0, END)
    state_entry.delete(0, END)
    rackno_entry.delete(0, END)

    global bookID1
    global bookname
    global bookname
    global purdate
    global publishername
    global bookMRP
    global state
    global rackno

    bookID1 = bookID_entry.get()
    bookname = bookname_entry.get()
    bookname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    d_name = database_name.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    a = cursor.execute("select * from library_system where bookID= %s" % bookID1)
    result = cursor.fetchall()

    for result in result:
        # bookID_entry.insert(0,result[0])
        bookname_entry.insert(0, result[1])
        authorname_entry.insert(0, result[2])
        purdate_entry.insert(0, result[3])
        Bookborrow_entry.insert(0, result[4])
        bookMRP_entry.insert(0, result[5])
        state_entry.insert(0, result[6])
        rackno_entry.insert(0, result[7])

    a = messagebox.askquestion("choice", "Do you want to Delete the entered information")
    if a == "yes":
        cursor.execute("delete from library_system where bookID = %s" % bookID1)
        mydb.commit()
        messagebox.showinfo("DELETED", "DATA DELETED SUCCESSFULLY")

        bookID_entry.delete(0, END)
        bookname_entry.delete(0, END)
        authorname_entry.delete(0, END)
        purdate_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        bookMRP_entry.delete(0, END)
        state_entry.delete(0, END)
        rackno_entry.delete(0, END)


def delete_rec_form():
    # messagebox.showinfo("Successfull","Database Found")
    global delete_record_window
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry
    delete_record_window = Toplevel(root)
    delete_record_window.geometry("600x450")
    delete_record_window.title("DELETE RECORD")
    frame_Dbase = LabelFrame(delete_record_window, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=20)
    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    # purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=delete_rec)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)
    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back_delete)
    back_btn.grid(pady=10, row=8, column=0)


def submit_delete():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=sub_delete, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def add_next():
    global add_window
    global database_name_entry
    global d_name
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    database_name_entry.withdraw()

    d_name = database_name.get()

    add_window = Toplevel(root)
    add_window.geometry("600x450")

    Label(add_window, text="Make sure to enter BookID unique every time.Otherwise it will give an Error!!",
          font=("lucida grande", "10")).grid(row=0)

    frame_Dbase = LabelFrame(add_window, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=20)

    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=Done_Dframe)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back_add)
    back_btn.grid(pady=10, row=8, column=0)


def sub_update():
    try:
        global d_name
        global database_name_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE,
                                 command=update_record_window)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def sub_delete():
    try:
        global d_name
        global database_name_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE,
                                 command=delete_rec_form)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def submit_add():
    try:
        global d_name
        global database_name_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE, command=add_next)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def back_delete():
    global delete_record_window
    delete_record_window.withdraw()


def back_add():
    global add_window

    add_window.withdraw()


def database_add():
    global add_window
    global d_name
    global database_name
    global database_name_entry
    a = messagebox.askquestion("Add", """In next window enter your database name in which you have created your Library table.
    Do you have Lib table.if you want to create new database you can do it by going on 'create Lib table' button""")

    if a == "yes":
        database_name_entry = Toplevel(root)
        database_name_entry.geometry("200x150")
        database_label = Label(database_name_entry, text="Enter  Database  name :-")
        database_label.grid()

        database_name = Entry(database_name_entry, width=20, borderwidth=2)
        database_name.grid()

        submit_button = Button(database_name_entry, text="submit", command=submit_add, bg="RosyBrown1")
        submit_button.grid(pady=5)

        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
        next_add_button.grid(row=2, column=1)


def submit_dname():
    global database_name
    global d_name
    global database_name_entry
    d_name = database_name.get()
    mydb = db.connect(host="localhost", password="root1234", user="root")
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % d_name)

    mydb.commit()
    messagebox.showinfo("", "Database created Successfully.")
    database_name_entry.destroy()


def back():
    global database_name_entry
    database_name_entry.withdraw()


def Done_Dframe():
    global bookID1
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry
    global d_name

    bookID1 = bookID_entry.get()
    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        add = cursor.execute(
            "insert into library_system values({},'{}','{}','{}','{}',{},'{}',{})".format(bookID1, bookname, authorname,
                                                                                          purdate, publishername,
                                                                                          bookMRP, state, rackno))
        # data = (bookID, bookname, authorname, purdate, publishername, bookMRP, state, rackno)
        cursor.execute(add)
        messagebox.showinfo("", "data inserted!!!")

        mydb.commit()

        bookID_entry.delete(0, END)
        bookname_entry.delete(0, END)
        authorname_entry.delete(0, END)
        purdate_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        bookMRP_entry.delete(0, END)
        state_entry.delete(0, END)
        rackno_entry.delete(0, END)

    except:
        messagebox.showerror("", """Error in some Entry feild.......Data not inserted.Try again!!!!.
    Note: please make sure you have enter values according to correct datatype of respective fields or you have left entry field blank""")


def submit():
    global d_name
    global database_name
    global database_name_entry
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        cursor.execute("""CREATE TABLE library_system(bookID  varchar(15)  primary key  not null,
        book_name varchar(30),
        Author_name  char(20)  not null ,
        Purchase_date  DATE ,
        Publisher_name varchar(30),
        book_MRP decimal ,
        state char(10),
        Rack_no int(4))""")
        messagebox.showinfo("", "Table created sucessfully")
        mydb.commit()

    except:
        messagebox.showerror("Unknown!!!!",
                             "Unknown database or Table with name library_system already exist in this database")
        database_name_entry.withdraw()

    frame_Dbase = LabelFrame(database_name_entry, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=Done_Dframe)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back)
    back_btn.grid(pady=10, row=8, column=0)


# function for creating table
def create_table():
    global d_name
    global database_name
    global database_name_entry
    a = messagebox.askquestion("DataBase", "Do you have any database in which you want to create Library table?")
    if a == "yes":
        database_name_entry = Toplevel(root)
        database_name_entry.geometry("600x450")
        database_label = Label(database_name_entry, text="Enter  Database  name :-")
        database_label.grid()

        database_name = Entry(database_name_entry, width=20, borderwidth=2)
        database_name.grid()

        submit_button = Button(database_name_entry, text="submit", command=submit, bg="RosyBrown1")
        submit_button.grid(pady=5)

    else:
        b = messagebox.askquestion("Choice", "Would you like to create one")

        if b == "yes":
            database_name_entry = Toplevel(root)
            database_name_entry.geometry("600x450")
            database_label = Label(database_name_entry, text="Enter  Database  name :-")
            database_label.grid()

            database_name = Entry(database_name_entry, width=20, borderwidth=2)
            database_name.grid()

            submit_button = Button(database_name_entry, text="submit", command=submit_dname, bg="RosyBrown1")
            submit_button.grid(pady=5)

        # d_name =database_name.get()

    # mydb = db.connect(host= "loclahost",user= "root",password="")
    # cursor= mydb.cursor()
    # cursor.execute("")


def choice_before_datas():
    global choice_window
    choice_window = Tk()
    choice_window.geometry("550x400")
    choice_window.title("Choose Here!!")
    choice_window.resizable(False, False)

    name = Label(choice_window, text="LIBRARY MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(choice_window, text="PLATO PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(choice_window, padx=50, pady=50)
    frame.grid()

    lib_btn = Button(frame, text="Library Window", bg="RosyBrown1", command=database_start)
    lib_btn.grid(row=0, column=1, pady=10, padx=15)
    stu_btn = Button(frame, text="Student Window", bg="RosyBrown1", command=window_for_stu_system)
    stu_btn.grid(row=0, column=2, pady=10, padx=15)

    choice_window.mainloop()


def database_start():
    global root
    root = Tk()
    root.geometry("550x400")
    root.title("LIBRARY WINDOW")
    # first heading
    name = Label(root, text="LIBRARY MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(root, text="PLATO PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(root, padx=50, pady=50)
    frame.grid(row=3, column=0)
    add_record = Button(frame, text="Add record", padx=20, pady=2, command=database_add)
    delete_record = Button(frame, text="Delete record", padx=20, pady=2, command=submit_delete)
    update_record = Button(frame, text="Update record", padx=11, pady=2, command=submit_update)
    showall_record = Button(frame, text="Show All record", padx=11, pady=2, command=show_all_submit)
    showone_record = Button(frame, text="Show One record", padx=7, pady=2, command=show_one_rec)
    Lib_table = Button(frame, text="Create Lib table", padx=11, pady=2, command=create_table)

    add_record.grid(row=0, column=0, padx=30, pady=9)
    delete_record.grid(row=0, column=1, padx=15, pady=9)
    update_record.grid(row=1, column=0, pady=9, padx=30)
    showall_record.grid(row=1, column=1, padx=15, pady=9)
    showone_record.grid(row=2, column=0, pady=9)
    Lib_table.grid(row=2, column=1, padx=30)

    root.mainloop()


def login_info():
    global login_screen
    global root
    global user_entry
    global password_entry
    global main
    global login_screen

    username1 = user_entry.get()
    password1 = password_entry.get()

    user_entry.delete(0, END)
    password_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 + ".txt" in list_of_files:
        file = open(username1 + ".txt", "r")
        verify1 = file.readline()
        verify2 = file.readline()

        if password1 == verify2:
            messagebox.showinfo("Done", "Login Successfull")
            main.withdraw()
            login_screen.withdraw()
            choice_before_datas()

        else:
            messagebox.showerror("Error", "Wrong Password!!!!")
            login_screen.destroy()

    else:
        messagebox.showerror("Not found", "USER NOT FOUND!!!!")
        login_screen.destroy()


def login():
    global login_screen
    global username
    global password
    global user_entry
    global password_entry
    global main
    # global user_verify
    # global password_verify

    login_screen = Toplevel(main)
    login_screen.title("LOGIN")
    login_screen.geometry("300x400")

    # user_verify = StringVar
    # password_verify = StringVar

    Label(login_screen, text="Enter your Login info. below:-", font=("lucida grande", "17")).grid()
    Label(login_screen, text="Username-", font=("lucida grande", "10")).grid()
    user_entry = Entry(login_screen, borderwidth=2)
    user_entry.grid()

    Label(login_screen, text=" ").grid()

    Label(login_screen, text="password-", font=("lucida grande", "10")).grid()
    password_entry = Entry(login_screen, borderwidth=2)
    password_entry.grid()

    Label(login_screen, text=" ").grid()

    login = Button(login_screen, text="Login", padx=10, command=login_info)
    login.grid()


def register_info():
    global username
    global password
    global user_entry
    global password_entry

    user_info = user_entry.get()
    password_info = password_entry.get()

    file = open(user_info + ".txt", "w")
    file.write(user_info + "\n")
    file.write(password_info)

    user_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Succesfull", "Registry successful")


def register():
    global username
    global password
    global user_entry
    global password_entry

    register_screen = Toplevel(main)
    register_screen.title("REGISTER HERE")
    register_screen.geometry("300x400")
    username = StringVar
    password = StringVar
    Label(register_screen, text="Enter your details below :-", font=("lucida grande", "19")).grid()

    Label(register_screen, text="Username-", font=("lucida grande", "10")).grid()
    user_entry = Entry(register_screen, textvariable=username, borderwidth=2)
    user_entry.grid()

    Label(register_screen, text="password-", font=("lucida grande", "10")).grid()
    password_entry = Entry(register_screen, textvariable=password, borderwidth=2)
    password_entry.grid()

    register_in = Button(register_screen, text="Register Info", command=register_info)

    register_in.grid()

    register_screen.mainloop()


def quit_main():
    global main
    main.quit()


def main_screen():
    global main
    main = Tk()
    main.title("LIBRARY MANAGEMENT SYSTEM")
    main.geometry("300x400")
    main.configure(background="misty rose")
    heading_main = Label(main, text="LOGIN", font=("Helvetica", "40"), anchor="center", bg="misty rose", padx=10)
    heading_main.grid(row=0, column=0, padx=65)

    login_button = Button(main, text="Login", padx=40, pady=3, command=login)
    login_button.grid(pady=25)

    register_button = Button(main, text="register", padx=35, pady=3, command=register)
    register_button.grid(pady=15)

    exit_button = Button(main, text="Exit", padx=45, pady=3, command=quit_main)
    exit_button.grid(pady=25)

    main.mainloop()


main_screen()

from tkinter import *
from tkinter import messagebox
import os
import mysql.connector as db
from tkinter import ttk


def One_submit_button_stu():
    try:
        global d_name
        global tv
        global One_entry
        global adminno_entry
        global adminno
        global stu_tv
        global ref_entry

        ID = One_entry.get()
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="672526", database=d_name)
        cursor = mydb.cursor()
        cursor.execute("select * from student_data where  Reference_no=%s" % ID)
        one = cursor.fetchall()
        if one == []:
            messagebox.showerror("Error", "No row with entered reference no. exist..")

        for i in one:
            stu_tv.insert("", 'end', values=i)

    except:
        messagebox.showerror("ERROR", """1. Please make sure you have entered and integer value.
        2. student_Library table exist in your database """)


def show_stu_one():
    global stu
    global stu_tv
    global One_entry

    showone_win = Toplevel(stu)
    showone_win.title("ONE RECORD")
    showone_win.geometry("1300x250")
    # frame_one= LabelFrame(showone_win)
    # frame_one.grid()
    Label(showone_win, text="Enter exact Reference No. below to display the Particular record:-",
          font=("lucida grande", "14")).grid(row=0, column=0, padx=50)
    One_entry = Entry(showone_win, width=20, borderwidth=3)
    One_entry.grid(row=1, column=0, pady=10)

    One_submit_btn = Button(showone_win, text="submit", command=One_submit_button_stu, bg="RosyBrown1")
    One_submit_btn.grid(row=2, column=0, pady=10)

    stu_tv = ttk.Treeview(showone_win, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show="headings", height="5")
    stu_tv.grid(row=3, pady=30)

    stu_tv.heading(1, text='Reference_No')
    stu_tv.column(1, width=100)
    stu_tv.heading(2, text='Admission_No')
    stu_tv.column(2, width=100)
    stu_tv.heading(3, text='student_name')
    stu_tv.column(3, width=130)
    stu_tv.heading(4, text='class_sec')
    stu_tv.column(4, width=70)
    stu_tv.heading(5, text='stream')
    stu_tv.column(5, width=70)
    stu_tv.heading(6, text='Book_borrowed')
    stu_tv.column(6, width=140)
    stu_tv.heading(7, text='bookID')
    stu_tv.column(7, width=70)
    stu_tv.heading(8, text='Author_name')
    stu_tv.column(8, width=140)
    stu_tv.heading(9, text='bookMRP')
    stu_tv.column(9, width=70)
    stu_tv.heading(10, text='Date_borrowed')
    stu_tv.column(10, width=100)
    stu_tv.heading(11, text='Due_Date')
    stu_tv.column(11, width=80)
    stu_tv.heading(12, text='State')
    stu_tv.column(12, width=100)
    stu_tv.heading(13, text='Phone_No')
    stu_tv.column(13, width=110)

    # scrollbar vertical
    scroll_v = ttk.Scrollbar(showone_win, orient="vertical", command=stu_tv.yview)
    stu_tv.configure(yscroll=scroll_v.set)
    scroll_v.grid(row=3, column=12, sticky="ns")


def show_one_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno

        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=show_stu_one)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def showone_win():
    global stu
    global stu_add
    global database_name
    global adminno_entry

    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-UPDATE")
    stu_add.geometry("250x400")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=show_one_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def show_stu_all():
    global stu
    global d_name
    global stu_tv

    showall_win = Toplevel(stu)
    showall_win.title("ALL RECORDS")
    showall_win.geometry("1300x550")
    show_frame = LabelFrame(showall_win)
    show_frame.grid()

    Label(show_frame, text="ALL RECORDS", font=("lucida grande", "20")).grid()
    stu_tv = ttk.Treeview(showall_win, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13), show="headings",
                          height="15")
    stu_tv.grid()

    stu_tv.heading(1, text='Reference_No')
    stu_tv.column(1, width=100)
    stu_tv.heading(2, text='Admission_No')
    stu_tv.column(2, width=100)
    stu_tv.heading(3, text='student_name')
    stu_tv.column(3, width=130)
    stu_tv.heading(4, text='class_sec')
    stu_tv.column(4, width=70)
    stu_tv.heading(5, text='stream')
    stu_tv.column(5, width=70)
    stu_tv.heading(6, text='Book_borrowed')
    stu_tv.column(6, width=140)
    stu_tv.heading(7, text='bookID')
    stu_tv.column(7, width=70)
    stu_tv.heading(8, text='Author_name')
    stu_tv.column(8, width=140)
    stu_tv.heading(9, text='bookMRP')
    stu_tv.column(9, width=70)
    stu_tv.heading(10, text='Date_borrowed')
    stu_tv.column(10, width=100)
    stu_tv.heading(11, text='Due_Date')
    stu_tv.column(11, width=80)
    stu_tv.heading(12, text='State')
    stu_tv.column(12, width=100)
    stu_tv.heading(13, text='Phone_No')
    stu_tv.column(13, width=110)
    # scrollbar vertical

    scroll_v = ttk.Scrollbar(showall_win, orient="vertical", command=stu_tv.yview)
    stu_tv.configure(yscroll=scroll_v.set)
    scroll_v.grid(row=0, column=13, sticky="ns")

    d_name = database_name.get()
    mydb = db.connect(host="localhost", user="root", password="root1234", database=d_name)
    cursor = mydb.cursor()
    cursor.execute("select * from student_data")
    result = cursor.fetchall()

    for i in result:
        stu_tv.insert("", 'end', values=i)


def show_all_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno

        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=show_stu_all)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def show_allstu_submit():
    global stu
    global stu_add
    global database_name
    global adminno_entry

    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-UPDATE")
    stu_add.geometry("250x400")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=show_all_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def save_updated_data():
    global frame_Dbase
    global stu
    global stu_add
    global d_name
    global database_name_entry
    global database_name
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global ref_entry
    global state_entry

    dname = database_name.get()

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get()
    P_no = Phoneno_entry.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    add = "update student_data set admission_no=%s,student_name=%s,class_section=%s,stream=%s,book_borrowed=%s,bookID=%s,author_name=%s,bookMRP=%s,date_borrowed=%s,Due_date=%s,state=%s,phoneNo=%s where Reference_no =%s"
    data = (
    adminno, studentname, class_sec, stu_stream, borrowB, B_ID, Author_name, mrp, borrow_D, D_date, state_stu, P_no,
    ref_no)
    cursor.execute(add, data)
    mydb.commit()
    messagebox.showinfo("UPDATED", "DATA UPDATED SUCCESSFULLY")

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", state=DISABLED)
    save.grid(pady=10, sticky=NSEW, row=13, column=1)


def Save_stu_Rec():
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global delete_stu_win
    global stu
    global dname
    global frame_Dbase
    global adminno
    global ref_entry
    global state_entry

    dname = database_name.get()

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get
    P_no = Phoneno_entry.get()

    mydb = db.connect(host="localhost", password="root1234", user="", database=dname)
    cursor = mydb.cursor()
    cursor.execute("select * from student_data where reference_no=%s" % ref_no)
    all = cursor.fetchall()

    for result in all:
        adminno_entry.insert(0, result[1])
        stuname_entry.insert(0, result[2])
        classec_entry.insert(0, result[3])
        stream_entry.insert(0, result[4])
        Bookborrow_entry.insert(0, result[5])
        bookid_entry.insert(0, result[6])
        Author_entry.insert(0, result[7])
        MRP_entry.insert(0, result[8])
        Dateborrwed_entry.insert(0, result[9])
        Duedate_entry.insert(0, result[10])
        state_entry.insert(0, result[11])
        Phoneno_entry.insert(0, result[12])

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", command=save_updated_data,
                  state=ACTIVE)
    save.grid(pady=10, sticky=NSEW, row=13, column=1)


def update_win():
    global frame_Dbase
    global stu
    global stu_add
    global d_name
    global stu_update
    global database_name_entry
    global database_name
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global ref_entry
    global state_entry

    stu_update = Toplevel(stu)
    stu_update.geometry("600x700")
    stu_update.title("UPDATE RECORD")

    frame_Dbase = LabelFrame(stu_update, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    Label(stu_update, text="Only enter Reference no. and rest fields program will fill on its own. ",
          font=("lucida grande", "10")).grid()
    Label(stu_update,
          text="Note:- 1.only one record is going to update at once and you can not change the reference no. ",
          font=("lucida grande", "10")).grid()
    Label(stu_update, text="    2.You have to entered exact reference no. otherwise it will not fill the entry fields ",
          font=("lucida grande", "10")).grid()

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="Done", borderwidth=2, padx=14, bg="RosyBrown1", command=Save_stu_Rec)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=upd_destroy)
    back_btn.grid(pady=10, row=13, column=0)


def upd_destroy():
    global stu_update
    stu_update.withdraw()


def stu_update_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno
        global ref_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=update_win)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def update_stu():
    global stu
    global stu_add
    global database_name
    global adminno_entry
    global ref_entry
    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-UPDATE")
    stu_add.geometry("250x400")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=stu_update_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def student_Delete():
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global delete_stu_win
    global stu
    global dname
    global frame_Dbase
    global adminno
    global ref_entry
    global state_entry

    dname = database_name.get()

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry
    P_no = Phoneno_entry.get()

    mydb = db.connect(host="localhost", password="root1234", user="root", database=dname)
    cursor = mydb.cursor()
    cursor.execute("select * from student_data where reference_no=%s" % ref_no)
    all = cursor.fetchall()

    # ref_entry.delete(0, END)
    # adminno_entry.delete(0, END)
    # stuname_entry.delete(0, END)
    # classec_entry.delete(0, END)
    # stream_entry.delete(0, END)
    # Bookborrow_entry.delete(0, END)
    # Author_entry.delete(0, END)
    # bookid_entry.delete(0, END)
    # Dateborrwed_entry.delete(0, END)
    # Duedate_entry.delete(0, END)
    # MRP_entry.delete(0, END)
    # state_entry.delete(0,END)
    # Phoneno_entry.delete(0, END)

    for result in all:
        # ref_entry.insert(0,result[0])
        adminno_entry.insert(0, result[1])
        stuname_entry.insert(0, result[2])
        classec_entry.insert(0, result[3])
        stream_entry.insert(0, result[4])
        Bookborrow_entry.insert(0, result[5])
        bookid_entry.insert(0, result[6])
        Author_entry.insert(0, result[7])
        MRP_entry.insert(0, result[8])
        Dateborrwed_entry.insert(0, result[9])
        Duedate_entry.insert(0, result[10])
        state_entry.insert(0, result[11])
        Phoneno_entry.insert(0, result[12])

    a = messagebox.askquestion("choice", "Do you want to Delete the entered information")
    if a == "yes":
        cursor.execute("delete from student_data where reference_no= %s" % ref_no)
        mydb.commit()
        messagebox.showinfo("DELETED", "DATA DELETED SUCCESSFULLY")

        ref_entry.delete(0, END)
        adminno_entry.delete(0, END)
        stuname_entry.delete(0, END)
        classec_entry.delete(0, END)
        stream_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        Author_entry.delete(0, END)
        bookid_entry.delete(0, END)
        Dateborrwed_entry.delete(0, END)
        Duedate_entry.delete(0, END)
        MRP_entry.delete(0, END)
        state_entry.delete(0, END)
        Phoneno_entry.delete(0, END)


def del_destroy():
    global delete_stu_win
    delete_stu_win.withdraw()


def delete_stu_rec():
    global delete_stu_win
    global stu
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global adminno
    global ref_entry
    global state_entry
    delete_stu_win = Toplevel(stu)
    delete_stu_win.geometry("600x550")
    delete_stu_win.title("DELETE RECORD")

    frame_Dbase = LabelFrame(delete_stu_win, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    stu_add.withdraw()

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="Done", borderwidth=2, padx=14, bg="RosyBrown1", command=student_Delete)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=del_destroy)
    back_btn.grid(pady=10, row=13, column=0)


def stu_database_connect():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        global adminno_entry
        global adminno
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=delete_stu_rec)
        next_add_button.grid(row=2, column=1)
    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create student Table'")


def stu_database_delete():
    global stu
    global stu_add
    global database_name
    global adminno_entry
    global ref_entry
    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-DELETE")
    stu_add.geometry("600x450")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=stu_database_connect, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def add_back_btn():
    global stu_add_new
    stu_add_new.withdraw()


def add_recto_table():
    global stu_add_new
    global database_name_entry
    global frame_Dbase
    global stu
    global bookID1
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global d_name
    global stu_add_new
    global adminno
    global ref_entry
    global state_entry

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get()
    P_no = Phoneno_entry.get()

    # frame_Dbase = LabelFrame(stu_add_new, borderwidth=5, height=5)
    # frame_Dbase.grid(padx=80, pady=10)

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        add = cursor.execute(
            "insert into student_data values({},{},'{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',{})".format(ref_no,
                                                                                                             adminno,
                                                                                                             studentname,
                                                                                                             class_sec,
                                                                                                             stu_stream,
                                                                                                             borrowB,
                                                                                                             B_ID,
                                                                                                             Author_name,
                                                                                                             mrp,
                                                                                                             borrow_D,
                                                                                                             D_date,
                                                                                                             state_stu,
                                                                                                             P_no))
        # data = (bookID, bookname, authorname, purdate, publishername, bookMRP, state, rackno)
        cursor.execute(add)
        messagebox.showinfo("", "data inserted!!!")

        mydb.commit()
        ref_entry.delete(0, END)
        adminno_entry.delete(0, END)
        stuname_entry.delete(0, END)
        classec_entry.delete(0, END)
        stream_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        Author_entry.delete(0, END)
        bookid_entry.delete(0, END)
        Dateborrwed_entry.delete(0, END)
        Duedate_entry.delete(0, END)
        MRP_entry.delete(0, END)
        state_entry.delete(0, END)
        Phoneno_entry.delete(0, END)

    except:
        messagebox.showerror("", """Error in some Entry feild.......Data not inserted.Try again!!!!.
            Note: please make sure you have enter values according to correct datatype of respective fields or you have left entry field blank""")


def add_rec():
    global adminno
    global stu
    global stu_add
    global d_name
    global database_name_entry
    global database_name
    global stu_add_new
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global ref_entry
    global state_entry

    stu_add_new = Toplevel(stu_add)
    stu_add_new.geometry("600x600")
    stu_add_new.title("ADD RECORDS")

    Label(stu_add_new, text="Reference No. need to be unique everytime Otherwise you will get an Error",
          font=("lucida grande", "10")).grid()

    frame_Dbase = LabelFrame(stu_add_new, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    stu_add.withdraw()

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    Duedate_entry.insert(0, "YYYY-MM-DD")
    Dateborrwed_entry.insert(0, "YYYY-MM-DD")

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=add_recto_table)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=add_back_btn)
    back_btn.grid(pady=10, row=13, column=0)


def sub_add_rec():
    try:
        global stu
        global stu_add
        global d_name
        global database_name_entry
        global database_name
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=ACTIVE, command=add_rec)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def stu_add_record():
    global stu
    global stu_add
    global database_name
    stu_add = Toplevel(stu)
    stu_add.title("STUDENT WINDOW-ADD")
    stu_add.geometry("600x450")
    database_label = Label(stu_add, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(stu_add, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(stu_add, text="submit", command=sub_add_rec, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(stu_add, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def add_rec_for_stu():
    global database_name_entry
    global frame_Dbase
    global stu
    global bookID1
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global d_name
    global adminno
    global ref_entry
    global state_entry

    ref_no = ref_entry.get()
    adminno = adminno_entry.get()
    studentname = stuname_entry.get()
    class_sec = classec_entry.get()
    stu_stream = stream_entry.get()
    borrowB = Bookborrow_entry.get()
    B_ID = bookid_entry.get()
    Author_name = Author_entry.get()
    mrp = MRP_entry.get()
    borrow_D = Dateborrwed_entry.get()
    D_date = Duedate_entry.get()
    state_stu = state_entry.get()
    P_no = Phoneno_entry.get()

    frame_Dbase = LabelFrame(database_name_entry, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    d_name = database_name.get()
    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    add = cursor.execute(
        "insert into student_data values({},{},'{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',{})".format(ref_no,
                                                                                                         adminno,
                                                                                                         studentname,
                                                                                                         class_sec,
                                                                                                         stu_stream,
                                                                                                         borrowB, B_ID,
                                                                                                         Author_name,
                                                                                                         mrp, borrow_D,
                                                                                                         D_date,
                                                                                                         state_stu,
                                                                                                         P_no))
    # data = (bookID, bookname, authorname, purdate, publishername, bookMRP, state, rackno)
    cursor.execute(add)
    messagebox.showinfo("", "data inserted!!!")
    mydb.commit()

    ref_entry.delete(0, END)
    adminno_entry.delete(0, END)
    stuname_entry.delete(0, END)
    classec_entry.delete(0, END)
    stream_entry.delete(0, END)
    Bookborrow_entry.delete(0, END)
    Author_entry.delete(0, END)
    bookid_entry.delete(0, END)
    Dateborrwed_entry.delete(0, END)
    Duedate_entry.delete(0, END)
    MRP_entry.delete(0, END)
    state_entry.delete(0, END)
    Phoneno_entry.delete(0, END)

    # except:
    #     messagebox.showerror("", """Error in some Entry feild.......Data not inserted.Try again!!!!.
    #     Note: please make sure you have enter values according to correct datatype of respective fields or you have left entry field blank""")


def submit_stu_base():
    global d_name
    global database_name
    global database_name_entry
    global adminno_entry
    global stuname_entry
    global classec_entry
    global stream_entry
    global Bookborrow_entry
    global Author_entry
    global bookid_entry
    global Dateborrwed_entry
    global Duedate_entry
    global MRP_entry
    global Phoneno_entry
    global adminno
    global ref_entry
    global state_entry

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        cursor.execute("""CREATE TABLE student_data(Reference_no int(30) primary key not null,
            Admission_no int(20) not null,
            student_name varchar(30),
            class_section  varchar(20)  not null ,
            stream  char(15) default "NONE" ,
            Book_borrowed varchar(35) not null,
            bookID int(10) not null,
            author_name char(40),
            bookMRP decimal(10) default "0.00",
            Date_borrowed DATE not null,
            Due_date DATE not null,
            state char(20) ,
            PhoneNo bigint(18))""")
        messagebox.showinfo("", "Table created sucessfully")
        mydb.commit()

    except:
        messagebox.showerror("Unknown!!!!",
                             "Unknown database or Table with name student_data already exist in this database")
        database_name_entry.withdraw()

    frame_Dbase = LabelFrame(database_name_entry, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    ref_label = Label(frame_Dbase, text="Reference No :-", font=("lucida grande", "15"))
    adminno_label = Label(frame_Dbase, text="Admission No :-", font=("lucida grande", "15"))
    stuname_label = Label(frame_Dbase, text="Student Name :-", font=("lucida grande", "15"))
    classec_label = Label(frame_Dbase, text="Class & sec :-", font=("lucida grande", "15"))
    stream_label = Label(frame_Dbase, text="Stream :-", font=("lucida grande", "15"))
    Bookborrow_label = Label(frame_Dbase, text="Book Borrowed :-", font=("lucida grande", "15"))
    bookid_label = Label(frame_Dbase, text="Book ID :-", font=("lucida grande", "15"), anchor=W)
    Author_label = Label(frame_Dbase, text="Author Name :-", font=("lucida grande", "15"))
    MRP_label = Label(frame_Dbase, text="BookMRP :-", font=("lucida grande", "15"))
    Dateborrwed_label = Label(frame_Dbase, text="Date Borrowed :-", font=("lucida grande", "15"))
    Duedate_label = Label(frame_Dbase, text="Due Date :-", font=("lucida grande", "15"))
    state_label = Label(frame_Dbase, text="State (returend/Not returned) :-", font=("lucida grande", "15"))
    Phoneno_label = Label(frame_Dbase, text="Phone No. :-", font=("lucida grande", "15"))

    ref_label.grid(sticky=W, pady=4)
    adminno_label.grid(sticky=W, pady=4)
    stuname_label.grid(sticky=W, pady=4)
    classec_label.grid(sticky=W, pady=4)
    stream_label.grid(sticky=W, pady=4)
    Bookborrow_label.grid(sticky=W, pady=4)
    bookid_label.grid(sticky=W, pady=4)
    Author_label.grid(sticky=W, pady=4)
    MRP_label.grid(sticky=W, pady=4)
    Dateborrwed_label.grid(sticky=W, pady=4)
    Duedate_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    Phoneno_label.grid(sticky=W, pady=4)

    ref_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    adminno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stuname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    classec_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    stream_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookid_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Author_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    MRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Dateborrwed_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Duedate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Phoneno_entry = Entry(frame_Dbase, width=25, borderwidth=2)

    Duedate_entry.insert(0, "YYYY-MM-DD")
    Dateborrwed_entry.insert(0, "YYYY-MM-DD")

    ref_entry.grid(row=0, column=1, padx=10, pady=4)
    adminno_entry.grid(row=1, column=1, padx=10, pady=4)
    stuname_entry.grid(row=2, column=1, padx=10, pady=4)
    classec_entry.grid(row=3, column=1, padx=10, pady=4)
    stream_entry.grid(row=4, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=5, column=1, padx=10, pady=4)
    bookid_entry.grid(row=6, column=1, padx=10, pady=4)
    Author_entry.grid(row=7, column=1, padx=10, pady=4)
    MRP_entry.grid(row=8, column=1, padx=10, pady=4)
    Dateborrwed_entry.grid(row=9, column=1, padx=10, pady=4)
    Duedate_entry.grid(row=10, column=1, padx=10, pady=4)
    state_entry.grid(row=11, column=1, padx=10, pady=4)
    Phoneno_entry.grid(row=12, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=add_rec_for_stu)
    done.grid(pady=10, sticky=NSEW, row=13, column=1)
    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back)
    back_btn.grid(pady=10, row=13, column=0)


def crea_stu_table():
    global stu
    global d_name
    global database_name
    global database_name_entry
    global submit_button
    a = messagebox.askquestion("DataBase", "Do you have any database in which you want to create Student table?")
    if a == "yes":
        database_name_entry = Toplevel(stu)
        database_name_entry.geometry("600x650")
        database_label = Label(database_name_entry, text="Enter  Database  name :-")
        database_label.grid()

        database_name = Entry(database_name_entry, width=20, borderwidth=2)
        database_name.grid()

        submit_button = Button(database_name_entry, text="submit", command=submit_stu_base, bg="RosyBrown1")
        submit_button.grid(pady=5)

    else:
        b = messagebox.askquestion("Choice", "Would you like to create one")

        if b == "yes":
            database_name_entry = Toplevel(stu)
            database_name_entry.geometry("600x450")
            database_label = Label(database_name_entry, text="Enter  Database  name :-")
            database_label.grid()

            database_name = Entry(database_name_entry, width=20, borderwidth=2)
            database_name.grid()

            submit_button = Button(database_name_entry, text="submit", command=submit_dname, bg="RosyBrown1")
            submit_button.grid(pady=5)


def window_for_stu_system():
    global stu
    stu = Tk()
    stu.geometry("550x400")
    stu.title("STUDENT WINDOW")
    # first heading
    name = Label(stu, text="LIBRARY MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(stu, text="PLATO PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(stu, padx=50, pady=50)
    frame.grid(row=3, column=0)
    add_record = Button(frame, text="Add record", padx=20, pady=2, command=stu_add_record)
    delete_record = Button(frame, text="Delete record", padx=20, pady=2, command=stu_database_delete)
    update_record = Button(frame, text="Update record", padx=11, pady=2, command=update_stu)
    showall_record = Button(frame, text="Show All record", padx=11, pady=2, command=show_allstu_submit)
    showone_record = Button(frame, text="Show One record", padx=7, pady=2, command=showone_win)
    stu_table = Button(frame, text="Create student table", padx=2, pady=2, command=crea_stu_table)

    add_record.grid(row=0, column=0, padx=30, pady=9)
    delete_record.grid(row=0, column=1, padx=15, pady=9)
    update_record.grid(row=1, column=0, pady=9, padx=30)
    showall_record.grid(row=1, column=1, padx=15, pady=9)
    showone_record.grid(row=2, column=0, pady=9)
    stu_table.grid(row=2, column=1, padx=30)

    stu.mainloop()


def One_submit_button():
    try:
        global d_name
        global tv
        global One_entry
        global show_one_window
        ID = One_entry.get()
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=d_name)
        cursor = mydb.cursor()
        cursor.execute("select * from library_system where  bookID=%s" % ID)
        one = cursor.fetchone()
        tv.insert("", 'end', values=one)

    except:
        messagebox.showerror("ERROR!!", "Invalid datatype entered or record with entered ID not exist...")


def show_one():
    global d_name
    global tv
    global One_entry
    global show_one_window

    show_one_window = Toplevel(root)
    show_one_window.geometry("1050x250")
    show_one_window.resizable(False, False)
    show_one_window.title("ONE RECORDS")
    frame_all = Frame(show_one_window)
    frame_all.grid(row=2)

    One_label = Label(show_one_window, text="Enter BookID of the record which you want to display:-",
                      font=("lucida grade", "12"), fg="coral")
    One_label.grid(row=0, column=0)

    One_entry = Entry(show_one_window, width=20, borderwidth=3)
    One_entry.grid(row=1, column=0)

    One_submit_btn = Button(show_one_window, text="submit", command=One_submit_button, bg="RosyBrown1")
    One_submit_btn.grid(row=2, column=0)

    tv = ttk.Treeview(frame_all, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="15")
    tv.grid(pady=20)

    tv.heading(1, text="bookID")
    tv.column(1, width=130)
    tv.heading(2, text="book_name")
    tv.column(2, width=130)
    tv.heading(3, text="author_name")
    tv.column(3, width=130)
    tv.heading(4, text="purcahse_date")
    tv.column(4, width=130)
    tv.heading(5, text="publisher_name")
    tv.column(5, width=130)
    tv.heading(6, text="bookMRP")
    tv.column(6, width=130)
    tv.heading(7, text="state")
    tv.column(7, width=130)
    tv.heading(8, text="Rackno")
    tv.column(8, width=100)


def submit_one_rec():
    try:
        global d_name
        global database_name_entry
        global d_name
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE, command=show_one)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def show_one_rec():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=submit_one_rec, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def show_all():
    global d_name

    show_all_window = Toplevel(root)
    show_all_window.geometry("1050x550")
    # show_all_window.resizable(False,False)
    show_all_window.title("ALL RECORDS")
    frame_all = Frame(show_all_window)
    frame_all.grid()
    # scroll_frame= LabelFrame(frame_all)
    # scroll_frame.grid(column=10,sticky="ns")

    Label(show_all_window, text="All Records ", font=("lucida grade", "30")).grid(sticky=N, row=0, column=0)

    tv = ttk.Treeview(frame_all, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="15")
    tv.grid(pady=80)
    # #scrollbar
    scrollbar_view = ttk.Scrollbar(frame_all, orient="vertical", command=tv.yview)
    tv.configure(yscroll=scrollbar_view.set)
    scrollbar_view.grid(row=0, column=9, sticky="ns")

    tv.heading(1, text="bookID")
    tv.column(1, width=130)
    tv.heading(2, text="book_name")
    tv.column(2, width=130)
    tv.heading(3, text="author_name")
    tv.column(3, width=130)
    tv.heading(4, text="purcahse_date")
    tv.column(4, width=130)
    tv.heading(5, text="publisher_name")
    tv.column(5, width=130)
    tv.heading(6, text="bookMRP")
    tv.column(6, width=130)
    tv.heading(7, text="state")
    tv.column(7, width=130)
    tv.heading(8, text="Rackno")
    tv.column(8, width=100)

    d_name = database_name.get()
    mydb = db.connect(host="localhost", user="root", password="root1234", database=d_name)
    cursor = mydb.cursor()
    cursor.execute("select * from library_system")
    result = cursor.fetchall()

    for i in result:
        tv.insert("", 'end', values=i)


def submit_show_all():
    try:
        global d_name
        global database_name_entry
        global d_name
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE, command=show_all)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def show_all_submit():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=submit_show_all, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def save_record():
    global bookID1
    global bookname
    global authorname
    global purdate
    global publishername
    global bookMRP
    global state
    global rackno

    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    d_name = database_name.get()
    bookID1 = bookID_entry.get()

    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    add = "update library_system set  book_name=%s,author_name=%s,purchase_date=%s,publisher_name=%s,book_MRP=%s,state=%s,rack_no=%s where bookID =%s"
    data = (bookname, authorname, purdate, publishername, bookMRP, state, rackno, bookID1)
    cursor.execute(add, data)
    mydb.commit()
    messagebox.showinfo("UPDATED", "ROW UPDATED SUCCESSFULLY")

    bookID_entry.delete(0, END)
    bookname_entry.delete(0, END)
    authorname_entry.delete(0, END)
    purdate_entry.delete(0, END)
    Bookborrow_entry.delete(0, END)
    bookMRP_entry.delete(0, END)
    state_entry.delete(0, END)
    rackno_entry.delete(0, END)

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", state=DISABLED)
    save.grid(pady=10, sticky=NSEW, row=8, column=1)


def done_record():
    global frame_Dbase
    global delete_record_window
    global database_name
    global d_name
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    global bookID1
    global bookname
    global authorname
    global purdate
    global publishername
    global bookMRP
    global state
    global rackno

    bookID1 = bookID_entry.get()
    d_name = database_name.get()

    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    a = cursor.execute("select * from library_system where bookID= %s" % bookID1)
    result = cursor.fetchall()

    for result in result:
        # bookID_entry.insert(0,result[0])
        bookname_entry.insert(0, result[1])
        authorname_entry.insert(0, result[2])
        purdate_entry.insert(0, result[3])
        Bookborrow_entry.insert(0, result[4])
        bookMRP_entry.insert(0, result[5])
        state_entry.insert(0, result[6])
        rackno_entry.insert(0, result[7])

    save = Button(frame_Dbase, text="SAVE RECORD", borderwidth=2, padx=14, bg="RosyBrown1", command=save_record,
                  state=ACTIVE)
    save.grid(pady=10, sticky=NSEW, row=8, column=1)


def submit_update():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=sub_update, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def update_record_window():
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry
    global frame_Dbase
    global update_record_window
    update_record_window = Toplevel(root)
    update_record_window.geometry("600x450")
    update_record_window.title("UPDATE RECORD")
    Label(update_record_window, text="Only enter BookID and rest fields program will fill on its own ",
          font=("lucida grande", "10")).grid()
    Label(update_record_window,
          text="Only One record at a time. To update again click on 'back' and open this window again ",
          font=("lucida grande", "10")).grid()
    frame_Dbase = LabelFrame(update_record_window, text="", borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=20)
    # Label(update_record_window, text="", font=("lucida grande", "15")).grid()
    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    # purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="Done", borderwidth=2, padx=14, bg="RosyBrown1", command=done_record)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)
    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back_update)
    back_btn.grid(pady=10, row=8, column=0)


def back_update():
    global update_record_window
    update_record_window.withdraw()


def delete_rec():
    global delete_record_window
    global database_name
    global d_name
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    bookname_entry.delete(0, END)
    authorname_entry.delete(0, END)
    purdate_entry.delete(0, END)
    Bookborrow_entry.delete(0, END)
    bookMRP_entry.delete(0, END)
    state_entry.delete(0, END)
    rackno_entry.delete(0, END)

    global bookID1
    global bookname
    global bookname
    global purdate
    global publishername
    global bookMRP
    global state
    global rackno

    bookID1 = bookID_entry.get()
    bookname = bookname_entry.get()
    bookname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    d_name = database_name.get()

    mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
    cursor = mydb.cursor()
    a = cursor.execute("select * from library_system where bookID= %s" % bookID1)
    result = cursor.fetchall()

    for result in result:
        # bookID_entry.insert(0,result[0])
        bookname_entry.insert(0, result[1])
        authorname_entry.insert(0, result[2])
        purdate_entry.insert(0, result[3])
        Bookborrow_entry.insert(0, result[4])
        bookMRP_entry.insert(0, result[5])
        state_entry.insert(0, result[6])
        rackno_entry.insert(0, result[7])

    a = messagebox.askquestion("choice", "Do you want to Delete the entered information")
    if a == "yes":
        cursor.execute("delete from library_system where bookID = %s" % bookID1)
        mydb.commit()
        messagebox.showinfo("DELETED", "DATA DELETED SUCCESSFULLY")

        bookID_entry.delete(0, END)
        bookname_entry.delete(0, END)
        authorname_entry.delete(0, END)
        purdate_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        bookMRP_entry.delete(0, END)
        state_entry.delete(0, END)
        rackno_entry.delete(0, END)


def delete_rec_form():
    # messagebox.showinfo("Successfull","Database Found")
    global delete_record_window
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry
    delete_record_window = Toplevel(root)
    delete_record_window.geometry("600x450")
    delete_record_window.title("DELETE RECORD")
    frame_Dbase = LabelFrame(delete_record_window, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=20)
    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    # purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=delete_rec)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)
    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back_delete)
    back_btn.grid(pady=10, row=8, column=0)


def submit_delete():
    global database_name_entry
    global database_name
    database_name_entry = Toplevel(root)
    database_name_entry.geometry("200x150")
    database_label = Label(database_name_entry, text="Enter  Database  name :-")
    database_label.grid()

    database_name = Entry(database_name_entry, width=20, borderwidth=2)
    database_name.grid()

    submit_button = Button(database_name_entry, text="submit", command=sub_delete, bg="RosyBrown1")
    submit_button.grid(pady=5)

    next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
    next_add_button.grid(row=2, column=1)


def add_next():
    global add_window
    global database_name_entry
    global d_name
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    database_name_entry.withdraw()

    d_name = database_name.get()

    add_window = Toplevel(root)
    add_window.geometry("600x450")

    Label(add_window, text="Make sure to enter BookID unique every time.Otherwise it will give an Error!!",
          font=("lucida grande", "10")).grid(row=0)

    frame_Dbase = LabelFrame(add_window, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=20)

    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=Done_Dframe)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back_add)
    back_btn.grid(pady=10, row=8, column=0)


def sub_update():
    try:
        global d_name
        global database_name_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE,
                                 command=update_record_window)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def sub_delete():
    try:
        global d_name
        global database_name_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE,
                                 command=delete_rec_form)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def submit_add():
    try:
        global d_name
        global database_name_entry
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234")
        cursor = mydb.cursor()
        cursor.execute("use %s" % d_name)
        messagebox.showinfo("", "Database connected succesfully")
        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=ACTIVE, command=add_next)
        next_add_button.grid(row=2, column=1)

    except:
        messagebox.showerror("Database ERROR 1049 ",
                             "No such database found.please check spelling or make one from 'create Lib Button'")


def back_delete():
    global delete_record_window
    delete_record_window.withdraw()


def back_add():
    global add_window

    add_window.withdraw()


def database_add():
    global add_window
    global d_name
    global database_name
    global database_name_entry
    a = messagebox.askquestion("Add", """In next window enter your database name in which you have created your Library table.
    Do you have Lib table.if you want to create new database you can do it by going on 'create Lib table' button""")

    if a == "yes":
        database_name_entry = Toplevel(root)
        database_name_entry.geometry("200x150")
        database_label = Label(database_name_entry, text="Enter  Database  name :-")
        database_label.grid()

        database_name = Entry(database_name_entry, width=20, borderwidth=2)
        database_name.grid()

        submit_button = Button(database_name_entry, text="submit", command=submit_add, bg="RosyBrown1")
        submit_button.grid(pady=5)

        next_add_button = Button(database_name_entry, text="next", bg="RosyBrown1", state=DISABLED)
        next_add_button.grid(row=2, column=1)


def submit_dname():
    global database_name
    global d_name
    global database_name_entry
    d_name = database_name.get()
    mydb = db.connect(host="localhost", password="root1234", user="root")
    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS %s" % d_name)

    mydb.commit()
    messagebox.showinfo("", "Database created Successfully.")
    database_name_entry.destroy()


def back():
    global database_name_entry
    database_name_entry.withdraw()


def Done_Dframe():
    global bookID1
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry
    global d_name

    bookID1 = bookID_entry.get()
    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    purdate = purdate_entry.get()
    publishername = Bookborrow_entry.get()
    bookMRP = bookMRP_entry.get()
    state = state_entry.get()
    rackno = rackno_entry.get()

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        add = cursor.execute(
            "insert into library_system values({},'{}','{}','{}','{}',{},'{}',{})".format(bookID1, bookname, authorname,
                                                                                          purdate, publishername,
                                                                                          bookMRP, state, rackno))
        # data = (bookID, bookname, authorname, purdate, publishername, bookMRP, state, rackno)
        cursor.execute(add)
        messagebox.showinfo("", "data inserted!!!")

        mydb.commit()

        bookID_entry.delete(0, END)
        bookname_entry.delete(0, END)
        authorname_entry.delete(0, END)
        purdate_entry.delete(0, END)
        Bookborrow_entry.delete(0, END)
        bookMRP_entry.delete(0, END)
        state_entry.delete(0, END)
        rackno_entry.delete(0, END)

    except:
        messagebox.showerror("", """Error in some Entry feild.......Data not inserted.Try again!!!!.
    Note: please make sure you have enter values according to correct datatype of respective fields or you have left entry field blank""")


def submit():
    global d_name
    global database_name
    global database_name_entry
    global bookID_entry
    global bookname_entry
    global authorname_entry
    global purdate_entry
    global Bookborrow_entry
    global bookMRP_entry
    global state_entry
    global rackno_entry

    try:
        d_name = database_name.get()
        mydb = db.connect(host="localhost", user="root", password="root1234", database=str(d_name))
        cursor = mydb.cursor()
        cursor.execute("""CREATE TABLE library_system(bookID  varchar(15)  primary key  not null,
        book_name varchar(30),
        Author_name  char(20)  not null ,
        Purchase_date  DATE ,
        Publisher_name varchar(30),
        book_MRP decimal ,
        state char(10),
        Rack_no int(4))""")
        messagebox.showinfo("", "Table created sucessfully")
        mydb.commit()

    except:
        messagebox.showerror("Unknown!!!!",
                             "Unknown database or Table with name library_system already exist in this database")
        database_name_entry.withdraw()

    frame_Dbase = LabelFrame(database_name_entry, borderwidth=5, height=5)
    frame_Dbase.grid(padx=80, pady=10)

    bookID_label = Label(frame_Dbase, text="BookID :-", font=("lucida grande", "15"))
    bookname_label = Label(frame_Dbase, text="Bookname :-", font=("lucida grande", "15"))
    authorname_label = Label(frame_Dbase, text="Author name :-", font=("lucida grande", "15"))
    purdate_label = Label(frame_Dbase, text="purchase date :-", font=("lucida grande", "15"))
    publishername_label = Label(frame_Dbase, text="Publisher name:-", font=("lucida grande", "15"))
    bookMRP_label = Label(frame_Dbase, text="Book MRP :-", font=("lucida grande", "15"), anchor=W)
    state_label = Label(frame_Dbase, text="State(issued/available):-", font=("lucida grande", "15"))
    rackno_label = Label(frame_Dbase, text="Rackno :-", font=("lucida grande", "15"))

    bookID_label.grid(sticky=W, pady=4)
    bookname_label.grid(sticky=W, pady=4)
    authorname_label.grid(sticky=W, pady=4)
    purdate_label.grid(sticky=W, pady=4)
    publishername_label.grid(sticky=W, pady=4)
    bookMRP_label.grid(sticky=W, pady=4)
    state_label.grid(sticky=W, pady=4)
    rackno_label.grid(sticky=W, pady=4)

    bookID_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    authorname_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    Bookborrow_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    bookMRP_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    state_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    rackno_entry = Entry(frame_Dbase, width=25, borderwidth=2)
    purdate_entry.insert(0, "YYYY-MM-DD")

    bookID_entry.grid(row=0, column=1, padx=10, pady=4)
    bookname_entry.grid(row=1, column=1, padx=10, pady=4)
    authorname_entry.grid(row=2, column=1, padx=10, pady=4)
    purdate_entry.grid(row=3, column=1, padx=10, pady=4)
    Bookborrow_entry.grid(row=4, column=1, padx=10, pady=4)
    bookMRP_entry.grid(row=5, column=1, padx=10, pady=4)
    state_entry.grid(row=6, column=1, padx=10, pady=4)
    rackno_entry.grid(row=7, column=1, padx=10, pady=4)

    done = Button(frame_Dbase, text="DONE", borderwidth=2, padx=14, bg="RosyBrown1", command=Done_Dframe)
    done.grid(pady=10, sticky=NSEW, row=8, column=1)

    back_btn = Button(frame_Dbase, text="Back", borderwidth=2, padx=14, bg="RosyBrown1", command=back)
    back_btn.grid(pady=10, row=8, column=0)


# function for creating table
def create_table():
    global d_name
    global database_name
    global database_name_entry
    a = messagebox.askquestion("DataBase", "Do you have any database in which you want to create Library table?")
    if a == "yes":
        database_name_entry = Toplevel(root)
        database_name_entry.geometry("600x450")
        database_label = Label(database_name_entry, text="Enter  Database  name :-")
        database_label.grid()

        database_name = Entry(database_name_entry, width=20, borderwidth=2)
        database_name.grid()

        submit_button = Button(database_name_entry, text="submit", command=submit, bg="RosyBrown1")
        submit_button.grid(pady=5)

    else:
        b = messagebox.askquestion("Choice", "Would you like to create one")

        if b == "yes":
            database_name_entry = Toplevel(root)
            database_name_entry.geometry("600x450")
            database_label = Label(database_name_entry, text="Enter  Database  name :-")
            database_label.grid()

            database_name = Entry(database_name_entry, width=20, borderwidth=2)
            database_name.grid()

            submit_button = Button(database_name_entry, text="submit", command=submit_dname, bg="RosyBrown1")
            submit_button.grid(pady=5)

def choice_before_datas():
    global choice_window
    choice_window = Tk()
    choice_window.geometry("550x400")
    choice_window.title("Choose Here!!")
    choice_window.resizable(False, False)

    name = Label(choice_window, text="LIBRARY MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(choice_window, text="PLATO PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(choice_window, padx=50, pady=50)
    frame.grid()

    lib_btn = Button(frame, text="Library Window", bg="RosyBrown1", command=database_start)
    lib_btn.grid(row=0, column=1, pady=10, padx=15)
    stu_btn = Button(frame, text="Student Window", bg="RosyBrown1", command=window_for_stu_system)
    stu_btn.grid(row=0, column=2, pady=10, padx=15)

    choice_window.mainloop()


def database_start():
    global root
    root = Tk()
    root.geometry("550x400")
    root.title("LIBRARY WINDOW")
    # first heading
    name = Label(root, text="LIBRARY MANAGEMENT SYSTEM", font=("lucida grande", "25"), anchor="center")
    name.grid(row=0, column=0)
    # second heading
    s_name = Label(root, text="PLATO PUBLIC SCHOOL", font=("lucida grande", "15"), anchor="center")
    s_name.grid()

    frame = LabelFrame(root, padx=50, pady=50)
    frame.grid(row=3, column=0)
    add_record = Button(frame, text="Add record", padx=20, pady=2, command=database_add)
    delete_record = Button(frame, text="Delete record", padx=20, pady=2, command=submit_delete)
    update_record = Button(frame, text="Update record", padx=11, pady=2, command=submit_update)
    showall_record = Button(frame, text="Show All record", padx=11, pady=2, command=show_all_submit)
    showone_record = Button(frame, text="Show One record", padx=7, pady=2, command=show_one_rec)
    Lib_table = Button(frame, text="Create Lib table", padx=11, pady=2, command=create_table)

    add_record.grid(row=0, column=0, padx=30, pady=9)
    delete_record.grid(row=0, column=1, padx=15, pady=9)
    update_record.grid(row=1, column=0, pady=9, padx=30)
    showall_record.grid(row=1, column=1, padx=15, pady=9)
    showone_record.grid(row=2, column=0, pady=9)
    Lib_table.grid(row=2, column=1, padx=30)

    root.mainloop()


def login_info():
    global login_screen
    global root
    global user_entry
    global password_entry
    global main
    global login_screen

    username1 = user_entry.get()
    password1 = password_entry.get()

    user_entry.delete(0, END)
    password_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 + ".txt" in list_of_files:
        file = open(username1 + ".txt", "r")
        verify1 = file.readline()
        verify2 = file.readline()

        if password1 == verify2:
            messagebox.showinfo("Done", "Login Successfull")
            main.withdraw()
            login_screen.withdraw()
            choice_before_datas()

        else:
            messagebox.showerror("Error", "Wrong Password!!!!")
            login_screen.destroy()

    else:
        messagebox.showerror("Not found", "USER NOT FOUND!!!!")
        login_screen.destroy()


def login():
    global login_screen
    global username
    global password
    global user_entry
    global password_entry
    global main
    login_screen = Toplevel(main)
    login_screen.title("LOGIN")
    login_screen.geometry("300x400")
    Label(login_screen, text="Enter your Login info. below:-", font=("lucida grande", "17")).grid()
    Label(login_screen, text="Username-", font=("lucida grande", "10")).grid()
    user_entry = Entry(login_screen, borderwidth=2)
    user_entry.grid()

    Label(login_screen, text=" ").grid()

    Label(login_screen, text="password-", font=("lucida grande", "10")).grid()
    password_entry = Entry(login_screen, borderwidth=2)
    password_entry.grid()

    Label(login_screen, text=" ").grid()

    login = Button(login_screen, text="Login", padx=10, command=login_info)
    login.grid()


def register_info():
    global username
    global password
    global user_entry
    global password_entry

    user_info = user_entry.get()
    password_info = password_entry.get()

    file = open(user_info + ".txt", "w")
    file.write(user_info + "\n")
    file.write(password_info)

    user_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Succesfull", "Registry successful")


def register():
    global username
    global password
    global user_entry
    global password_entry

    register_screen = Toplevel(main)
    register_screen.title("REGISTER HERE")
    register_screen.geometry("300x400")
    username = StringVar
    password = StringVar
    Label(register_screen, text="Enter your details below :-", font=("lucida grande", "19")).grid()

    Label(register_screen, text="Username-", font=("lucida grande", "10")).grid()
    user_entry = Entry(register_screen, textvariable=username, borderwidth=2)
    user_entry.grid()

    Label(register_screen, text="password-", font=("lucida grande", "10")).grid()
    password_entry = Entry(register_screen, textvariable=password, borderwidth=2)
    password_entry.grid()

    register_in = Button(register_screen, text="Register Info", command=register_info)

    register_in.grid()

    register_screen.mainloop()


def quit_main():
    global main
    main.quit()


def main_screen():
    global main
    main = Tk()
    main.title("LIBRARY MANAGEMENT SYSTEM")
    main.geometry("300x400")
    main.configure(background="misty rose")
    heading_main = Label(main, text="LOGIN", font=("Helvetica", "40"), anchor="center", bg="misty rose", padx=10)
    heading_main.grid(row=0, column=0, padx=65)

    login_button = Button(main, text="Login", padx=40, pady=3, command=login)
    login_button.grid(pady=25)

    register_button = Button(main, text="register", padx=35, pady=3, command=register)
    register_button.grid(pady=15)

    exit_button = Button(main, text="Exit", padx=45, pady=3, command=quit_main)
    exit_button.grid(pady=25)
    main.mainloop()


main_screen()

