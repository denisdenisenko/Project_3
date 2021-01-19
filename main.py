import mysql.connector
from mysql.connector import Error


def get_connection():
    """
    function to establish connection with database
    :return:
    """
    my_connection = mysql.connector.connect(
        host="localhost", user="root", password="1111", database="Project_3")
    return my_connection


def close_connection(some_connection):
    """
    function to close the connection with database
    :param some_connection:
    :return:
    """
    if some_connection:
        some_connection.close()


def read_database_version():
    """
    this function prints the database version
    :return:
    """
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


def new_table_doctors_in_hospital(hospital_name):
    global connection, cursor
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = ' select hospital_ID from hospital  where hospital_name = %s;'
        cursor.execute(sql_select_query, (hospital_name,))

        # Extracting Hospital_ID from the given name
        record = cursor._fetch_row()
        fetched_hospital_id = record[0]
        print(fetched_hospital_id)

        # Choose different table name
        sql_select_query = 'CREATE TABLE new_table ' \
                           'SELECT Doctor_ID, Doctor_Name, Hospital_ID,Joining_Date,Speciality,Salary,Experience ' \
                           'FROM Doctor ' \
                           'WHERE Hospital_ID = %s'
        cursor.execute(sql_select_query, (fetched_hospital_id,))

        sql_select_query = 'Select * From new_table'
        cursor.execute(sql_select_query)

        record = cursor.fetchall()

        print("Doctors of new table are " + "\n")
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


new_table_doctors_in_hospital("Cleveland Clinic")
