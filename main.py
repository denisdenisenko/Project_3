import mysql.connector
from mysql.connector import Error


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1111",
        database="Project_3")
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def read_database_version():
    try:
        connection = get_connection()
        mycursor = connection.cursor()
        mycursor.execute("SELECT * from Hospital")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")


read_database_version()
