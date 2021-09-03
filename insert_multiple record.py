import cx_Oracle

"""Execute multiple records
"""

try:
    query="insert into employee values(:EMPLOYEEID,:FIRSTNAME,:LASTNAME,:EMAIL,:ADDRESSLINE,:CITY)"
    records=[(3,'Soniya','jadhav','soniya@outlook.com','chayogayang city','Beijing'),(4,'Soniya','kapoor','kapoor@outlook.com','kapoor city','Shanghai'),(5,'Rashmi','jadhav','rashmi@outlook.com','Wuhan city','daxing'),(6,'Soniya','Nair','soniya@outlook.com','chayogayang city','Beijing'),(7,'Akbar','ali','ali@outlook.com','ali city','Dubai')]
    con=cx_Oracle.connect("system/SYS@localhost")
    cursor=con.cursor()
    cursor.executemany(query,records)
    con.commit()
    print("Rows inserted sucessfully ")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
    print("Database error ")
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()