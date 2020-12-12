#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


#============================METHODS=====================================

def Database():
    conn = sqlite3.connect("studentdata.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `student` (student_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, email TEXT UNIQUE, course TEXT, username TEXT, address TEXT, contact TEXT)")
    cursor.execute("SELECT * FROM `student` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or EMAIL.get() == "" or COURSE.get() == "" or USERNAME.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("studentdata.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `student` (firstname, lastname, gender, age,email, course, username, address, contact) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(EMAIL.get()), str(COURSE.get()),str(USERNAME.get()),str(ADDRESS.get()), str(CONTACT.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `student` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        EMAIL.set("")
        COURSE.set("")
        USERNAME.set("")
        ADDRESS.set("")
        CONTACT.set("")
        

def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("studentdata.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `student` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?, `email` = ?, `course` = ?, `username` = ?, `address` = ?, `contact` = ? WHERE `student_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(EMAIL.get()), str(COURSE.get()),str(USERNAME.get()), str(ADDRESS.get()), str(CONTACT.get()), int(student_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `student` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        EMAIL.set("")
        COURSE.set("")
        USERNAME.set("")
        ADDRESS.set("")
        CONTACT.set("")
        
    
def StudentSelected(event):
    global student_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    student_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    EMAIL.set("")
    COURSE.set("")
    USERNAME.set("")
    ADDRESS.set("")
    CONTACT.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[4])
    EMAIL.set(selecteditem[5])
    COURSE.set(selecteditem[6])
    USERNAME.set(selecteditem[7])
    ADDRESS.set(selecteditem[8])
    CONTACT.set(selecteditem[9])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Student List")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
        
    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    StudentForm = Frame(UpdateWindow)
    StudentForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(StudentForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text= "Updating Student Data", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(StudentForm, text="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(StudentForm, text="Lastname", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(StudentForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(StudentForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_email = Label(StudentForm, text="Email", font=('arial', 14), bd=5)
    lbl_email.grid(row=4, sticky=W)
    lbl_course = Label(StudentForm, text="Course", font=('arial', 14), bd=5)
    lbl_course.grid(row=5, sticky=W)
    lbl_username = Label(StudentForm, text="Username", font=('arial', 14), bd=5)
    lbl_username.grid(row=6, sticky=W)
    lbl_address = Label(StudentForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=7, sticky=W)
    lbl_contact = Label(StudentForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=8, sticky=W)

    #===================ENTRY===============================
    firstname = Entry(StudentForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(StudentForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(StudentForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    email = Entry(StudentForm, textvariable=EMAIL,  font=('arial', 14))
    email.grid(row=4, column=1)
    course = Entry(StudentForm, textvariable=COURSE,  font=('arial', 14))
    course.grid(row=5, column=1)
    username = Entry(StudentForm, textvariable=USERNAME,  font=('arial', 14))
    username.grid(row=6, column=1)
    address = Entry(StudentForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=7, column=1)
    contact = Entry(StudentForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=8, column=1)
    

    #==================BUTTONS==============================#
    btn_updatecon = Button(StudentForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=9, columnspan=2, pady=10)
    btn_addstu = Button(StudentForm, text="Close", width=50, command=exit)
    btn_addstu.grid(row=11, columnspan=2, pady=5)
    
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select a Data First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("studentdata.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `student` WHERE `student_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    
def AddNewWindow():
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    EMAIL.set("")
    COURSE.set("")
    USERNAME.set("")
    ADDRESS.set("")
    CONTACT.set("")
    NewWindow = Toplevel()
    NewWindow.title("Student List")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    StudentForm = Frame(NewWindow)
    StudentForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(StudentForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Student", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(StudentForm, text="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(StudentForm, text="Lastname", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(StudentForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(StudentForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_email = Label(StudentForm, text="Email", font=('arial', 14), bd=5)
    lbl_email.grid(row=4, sticky=W)
    lbl_course = Label(StudentForm, text="Course", font=('arial', 14), bd=5)
    lbl_course.grid(row=5, sticky=W)
    lbl_username = Label(StudentForm, text="Username", font=('arial', 14), bd=5)
    lbl_username.grid(row=6, sticky=W)
    lbl_address = Label(StudentForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=7, sticky=W)
    lbl_contact = Label(StudentForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=8, sticky=W)

    #===================ENTRY===============================
    firstname = Entry(StudentForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(StudentForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(StudentForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    email = Entry(StudentForm, textvariable=EMAIL,  font=('arial', 14))
    email.grid(row=4, column=1)
    course = Entry(StudentForm, textvariable=COURSE,  font=('arial', 14))
    course.grid(row=5, column=1)
    username = Entry(StudentForm, textvariable=USERNAME,  font=('arial', 14))
    username.grid(row=6, column=1)
    address = Entry(StudentForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=7, column=1)
    contact = Entry(StudentForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=8, column=1)
    

    #==================BUTTONS==============================
    btn_addstu = Button(StudentForm, text="Save", width=50, command=SubmitData)
    btn_addstu.grid(row=10, columnspan=2, pady=10)

    btn_addstu = Button(StudentForm, text="Close", width=50, command=exit)
    btn_addstu.grid(row=11, columnspan=2, pady=5)


# In[ ]:





# In[ ]:




