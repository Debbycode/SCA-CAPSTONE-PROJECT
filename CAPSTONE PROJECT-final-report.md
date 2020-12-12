## __Capstone Project - USER MANAGMENT SYSTEM (UMS)__

### STUDENT MANAGEMENT SYSTEM USING SQLITE IN PYTHON

### __INTRODUCTION__

A highly efficient method for handling multiple type of data in an organisation or business, is the Database management system. For example, in an educational organistion, the institution administration keeps record of all students in the institution. The User Management System is a simple system developed for managing user details and for easy management of user records. 

This project aims at developing a user management system using the SQLite in python as it's database. The project enables an educational organization to maintain student's information. The system contains an administrative side from where the admin can maintain the student records easily. For example, in order to add student records, various information such as the his/her first name, last name, age, email, course, username is provided. Thereafter, the user can easily manage the user’s record and can update, delete records if he/she wants.

Furthermore, the project file contains the python scripts (main.py(database_student.py), master.py and test.py). The scripts utilizes the standard GUI library for Python - Tkinter - that creates a pretty and simple user framework. Users will find the framework easy to navigate ad will not find any difficulty working on it. Moreover, the application uses basic Python functions to generate menu options, title boxes, input message boxes, list and print text on the screen. 

### __DATA__

In order to program the User management system using SQLite3 database in python, the first step is to import the sqlite3 module. Following this, is to create a table in SQLite. In this projeect, We created a table student having the following attributes:

student (first_name, last_name, gender, age, email, course, username, address, contact)
(The step by step method is explained in the methodology section). To check if the table is created, We used the DB browser for SQLite to view the table. We downloaded the _studentdata.db_ file and Open file with the DB program. The table is given:

<img src ="Student_table.PNG">

## __METHODOLOGY__

### __Create Connection__

To create a connection with SQLite which will connect us to the database for executing the SQL statements, We used the connect()function (after importing sqlite module

            import sqlite3
            conn = sqlite3.connect("studentdata.db")_
            

### __SQLite Cursor__

To execute SQLite statements in Python, we need a cursor object. We created it using the cursor() method. The SQLite3 cursor is a method of the connection object. To execute the SQLite3 statements, we should establish a connection at first and then create an object of the cursor using the connection object as follows:

            cursor = conn.cursor()
            

### __Create Database and Table__

To create a connection with SQLite that will create a database file automatically if it doesn’t already exist and create an exception if it exists. We used the follwing code:

           cursor.execute("CREATE TABLE IF NOT EXISTS `student` (student_id 
           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname 
           TEXT, gender TEXT, age TEXT, email TEXT UNIQUE, course TEXT, username 
           TEXT,address TEXT, contact TEXT)")cursor.execute("SELECT * FROM `student` 
           ORDER BY `lastname` ASC")

The general function is as follows:

<img src ="Database_table.PNG">


### __Insert in Table__

To insert data in a table, we used the _INSERT INTO_ student. We passed values/arguments to an INSERT statement in the execute() method. We used the question mark (?) as a placeholder for each value. The syntax of the _INSERT_ is found in the entire _SubmitData_ class as follows:

<img src ="Insert_table.PNG">


### __Update Table__

To update the table, we simply used the _UPDATE_ statement in the execute() method. Suppose that we want to update the gender of the student whose ID is 2. For updating, we will use the _UPDATE_ statement and for the student whose ID equals 2. We will use the _WHERE_ clause as a condition to select this student. The general _UpdateData_ class is given:

<img src ="Update_table.PNG">


### __Delete Table__

We used the _DeleteData_ function to delete a table using the _DELETE_ statement. The syntax of the _DELETE_ statement is as follows:

<img src ="Delete_table.PNG">


### __Close Connection__

Once we are done with our database, we deemed it good practice to close the connection. Therefore, we closed our connection by using the close() method. To close a connection, use the connection object and call the close() method as follows:


### __Other Python Functions (Tkinter)__

Inoder to make program user friend, the the Tkinker GUI interface.We used _StudentSelected_ and _AddNewWindow_ to enable users make selections on the tkinker window user interface. For example, the _Addnewwindow_ command is the _Add New button_ on the user GUI(As can be seen in the result section). Moreover, we imported the the tkinter module before calling these functions.

            from tkinter import *
            import tkinter.ttk as ttk
            import tkinter.messagebox as tkMessageBox


### __How To Run Project Script__

To run this script, user must have installed Python on their PC. Then download the python scripts. After downloading the project, follow the steps below:

Step1: Extract/Unzip the file

Step2: Locate the the project folder,

Step3: open cmd then type main.py and enter to start the system.

OR

Step3: double click the main.py file and the script is run automatically

### __RESULT__

The result of the code after running are as follows:

__Image 1:__
The Image GUI show that a database has been created. The GUI interface shows a student table with the required information as attributes. All student data are shown in the window(if student data have been recorded previously).

__Image 2:__
The image of the getting student information and inserting data into table. The GUI show a new window (Adding New Student) containing input information for new student.

__Image 3:__
The image show the Update Window interface used for adding/updating existing student record. By double-clicking the selected student record, the update window pops-up.

__Image 4:__
In the image, the _DELETE_ button on the user interface is for removing a student record from the database. A confirmation promptis seen confirm delete option.

__Image 5:__
The image show the database for five students using the Student management System GUI. The list shows student's information.

Summarily, the results, as is shown in Images 1 through 4, shows that the code for the User Management System was successfully run. The application created new student record, obtained or submited new student data, updated student account and deleted a student account. 

<img src ="Image1.PNG">

<img src ="Image2.PNG">

<img src ="Image3.PNG">

<img src ="Image4.PNG">

<img src ="student_list.PNG">

### __DISCUSSION__

Creating a User Management System may have different programming structures and methods but similar result is obtained. That is, the program can CREATE, GET, UPDATE and DELETE record. The result obtained in this project is as presented and the results are quite satisfying.

### __CONCLUSION__

To sum up, this User Management System design can be used in an educational organisation to keep the record of student in the institution. Admin can create a student database and store information for each student. Each student can be updated and deleted(for example if the student is no longer in the institution. The program is user friendly and easy to use.


```python

```


```python

```
