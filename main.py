import mysql.connector
from mysql.connector import Error


def get_connection():
    my_connection = mysql.connector.connect(host="localhost", user="root", password="1111", database="Project_3")
    return my_connection


def close_connection(some_connection):
    if some_connection:
        some_connection.close()


def read_database_version():
    global new_connection, my_cursor
    try:
        new_connection = get_connection()
        my_cursor = new_connection.cursor()
        my_cursor.execute('SELECT @@version;')
        print("The version is: ")
        for x in my_cursor:
            print(x)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if new_connection.is_connected():
            my_cursor.close()
            new_connection.close()
            print("MySQL connection is closed")


def get_hospital_detail(hospital_id):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = 'select * from Hospital where Hospital_ID = %s'
        cursor.execute(sql_select_query, (hospital_id,))
        record = cursor.fetchall()

        for row in record:
            print("Hospital_ID = ", row[0], )
            print("Hospital_Name = ", row[1])
            print("Bed_count = ", row[2], "\n")
        close_connection(connection)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


get_hospital_detail(2)
