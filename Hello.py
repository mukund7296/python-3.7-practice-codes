x="""Steps to setup Database programming"""
print(x)

steps="""Activity to access database steps :
Step1 : Import Module 
        import cx_Oracle or pymysql
Step2 : Connection between python and Database
        con=cx_Oracle.connect(localhost,user,password,dbname)
        con=pymysql.connect(localhost,user,password,dbname)
        eg: con=cx_Oracle.connect('mukund/mukund?123@localhost')
Step3 :To execute or hold the query of result we need special object Cursor
        cursor=con.cursor()
Step4 : To run SQL query 
        cursor.execute(sqlquerye)--> Execute one sql Query 
        cursor.executescript(group_sql_query)-->To execute a string of sql queries seperated by ; \n(sql1;sql2;....)
        cursor.executemany(parameter_query)-->To execut Paramaterizedd query
Step5 : Fetch the Result
        cursor.fetchone()--> To fetch one single row result 
        cursor.fetchall()--> To fetch all rows as Result
        cursor.fetchmany()--> To fetch n rows.
Step6 : use commit then only it will reflect into database.
        commit() or Rollback()
Step7 : Close the connection
        cursor.close()
        con.close()
        """
print(steps)