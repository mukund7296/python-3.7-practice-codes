import cx_Oracle

try:
    query="CREATE TABLE STUDENTS (ID int NOT NULL,NAME VARCHAR(20)NOT NULL,AGE INT,ADDRESS CHAR(25),PRIMARY KEY (ID))"
    con=cx_Oracle.connect('system/SYS@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    print("Table is created")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("there is problem ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()