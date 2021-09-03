import cx_Oracle

try:
    query="drop table school"
    con=cx_Oracle.connect("system/SYS@localhost")
    cursor=con.cursor()
    cursor.execute(query)
    print("Table Drop succesfully")
except cx_Oracle.DatabaseError as e:
    if con:
        con.rollback()
        print("Table not drop becoz of database error",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()