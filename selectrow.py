import cx_Oracle

"""Select rows"""

try:
    query="select * from employee"
    con=cx_Oracle.connect("system/SYS@localhost")
    cursor=con.cursor()
    cursor.execute(query)
    #row=cursor.fetchmany()
    row=cursor.fetchall()

    for i in row:
        print(i)
    """row=cursor.fetchone()
    for i in row:
        print(i,end=" ")"""



except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
    print("Database error ")
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()