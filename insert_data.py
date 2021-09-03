import cx_Oracle

try:
    query="insert into employee values(2,'mukund','biradar','mukund2015@outlook.com','c-88 ozone villa wagholi','Pune')"
    con=cx_Oracle.connect("system/SYS@localhost")
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print("Row inserted sucessfully ")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
    print("Database error ")
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()