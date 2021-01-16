import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1111",
    database="Project_3"
)

mycursor = mydb.cursor()

mycursor.execute('Select * from Doctor')

for x in mycursor :
    print(x)
