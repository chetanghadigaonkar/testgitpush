import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",passwd="chetan1111",auth_plugin='mysql_native_password')
print(mydb)
cursor=mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())

