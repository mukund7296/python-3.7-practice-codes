#To insert multiple records dynamically from keyboard
import cx_Oracle

try:

    con=cx_Oracle.connect("system/SYS@localhost")
    cursor=con.cursor()
    while True:
        EMPLOYEEID=int(input("Enter your Emploeeid :"))
        FIRSTNAME=input("Enter your First Name :")
        LASTNAME=input("Enter your Last Name :")
        EMAIL=input("Enter your email id :")
        ADDRESSLINE=input("Enter your address :")
        CITY=input("Enter your City name :")
        query="insert into employee values(%d,'%s','%s','%s','%s','%s')"
        cursor.execute(query %(EMPLOYEEID,FIRSTNAME,LASTNAME,EMAIL,ADDRESSLINE,CITY))
        con.commit()
        print("Row inserted succesfully !!!!" )
        options=input("Do you want to insert one more record (Yes/No) :")
        if options=='No' or options=='no':
            break

except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
    print("Row not inserted \t Database error",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()