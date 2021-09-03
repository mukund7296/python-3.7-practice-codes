import cx_Oracle

try:
    query="CREATE TABLE Employee(EmployeeID number(10),FirstName varchar2(255),LastName varchar2(255),Email varchar2(255),AddressLine varchar2(255),City varchar2(255))"
    con=cx_Oracle.connect('system/SYS@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    print("Table is created succefully !!!!")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("There is problem in programm",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
