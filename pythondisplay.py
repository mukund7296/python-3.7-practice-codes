import sqlite3 as It
import sys

con=It.connect('Employe.db')
with con:
    cur=con.cursor()
    #cur.execute('CREATE TABLE Employee(EmployeeID NOT NULL,FirstName varchar(255) NOT NULL,LastName varchar(255),City varchar(255),PRIMARY KEY (EmployeeID))')
   # cur.execute('INSERT INTO Employee (EmployeeID,FirstName,LastName,City) VALUES(6, "Mukund", "Biradar", "Beijing")')
    #cur.execute('INSERT INTO Employee (EmployeeID,FirstName,LastName,City) VALUES(7, "Shaurya", "Biradar", "Shanghai")')
    #cur.execute('INSERT INTO Employee (EmployeeID,FirstName,LastName,City) VALUES(8, "Hansraj", "Biradar", "Beijing")')
    #cur.execute('INSERT INTO Employee (EmployeeID,FirstName,LastName,City) VALUES(9, "Anand", "Biradar", "NYC")')
    #cur.execute('INSERT INTO Employee (EmployeeID,FirstName,LastName,City) VALUES(10, "Soniya", "Biradar", "Beijing")')
    cur.execute("Select * from Employee")
    rows=cur.fetchall()

    for i in rows:
        print(i)

con.close()
print("Display rows")