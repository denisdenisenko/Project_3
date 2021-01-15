import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1111",
    database="Project_3"
)

mycursor = mydb.cursor()

mycursor.execute("")


