import mysql.connector
from mysql.connector import Error


def get_connection():
    my_connection = mysql.connector.connect(
        host="localhost", user="root", password="1111", database="Project_3")
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


def get_doctor_detail(doctor_id):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = 'select * from Doctor where Doctor_ID = %s'
        cursor.execute(sql_select_query, (doctor_id,))
        record = cursor.fetchall()

        for row in record:
            print("Doctor_ID = ", row[0], )
            print("Doctor_Name = ", row[1])
            print("Hospital_ID = ", row[2])
            print("Joining_Date = ", row[3])
            print("Speciality = ", row[4])
            print("Salary = ", row[5])
            print("Experience = ", row[6], "\n")

        close_connection(connection)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def get_specialist_doctors_list(speciality, salary):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = 'select * from Doctor where Speciality = %s and Salary = %s;'
        cursor.execute(sql_select_query, (speciality, salary,))
        record = cursor.fetchall()

        for row in record:
            print("Doctor_ID = ", row[0], )
            print("Doctor_Name = ", row[1])
            print("Hospital_ID = ", row[2])
            print("Joining_Date = ", row[3])
            print("Speciality = ", row[4])
            print("Salary = ", row[5])
            print("Experience = ", row[6], "\n")

        close_connection(connection)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def get_doctors(hospital_id):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = 'select * from Doctor where Hospital_ID = %s'
        cursor.execute(sql_select_query, (hospital_id,))
        record = cursor.fetchall()

        for row in record:
            print("Doctor_ID = ", row[0], )
            print("Doctor_Name = ", row[1])
            print("Hospital_ID = ", row[2])
            print("Joining_Date = ", row[3])
            print("Speciality = ", row[4])
            print("Salary = ", row[5])
            print("Experience = ", row[6], "\n")

        close_connection(connection)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def update_doctor_experience(exp, doctor_id):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = 'UPDATE Doctor SET Experience = %s WHERE Doctor_ID =  %s;'
        cursor.execute(sql_select_query, (exp, doctor_id,))

        sql_select_query = 'Select * From Doctor Where Doctor_ID = %s'
        cursor.execute(sql_select_query, (doctor_id,))

        record = cursor.fetchall()

        for row in record:
            print("Doctor_ID = ", row[0], )
            print("Doctor_Name = ", row[1])
            print("Hospital_ID = ", row[2])
            print("Joining_Date = ", row[3])
            print("Speciality = ", row[4])
            print("Salary = ", row[5])
            print("Experience = ", row[6], "\n")

        close_connection(connection)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


update_doctor_experience(13, 102)

def doctors_in_hospital (hospital_name):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = 'UPDATE Doctor SET Experience = %s WHERE Doctor_ID =  %s;'
        cursor.execute(sql_select_query, (hospital_name,))

        sql_select_query = 'Select * From Doctor Where Doctor_ID = %s'
        cursor.execute(sql_select_query, (hospital_name,))

        record = cursor.fetchall()

        for row in record:
            print("Doctor_ID = ", row[0], )
            print("Doctor_Name = ", row[1])
            print("Hospital_ID = ", row[2])
            print("Joining_Date = ", row[3])
            print("Speciality = ", row[4])
            print("Salary = ", row[5])
            print("Experience = ", row[6], "\n")

        close_connection(connection)
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
