from pyodbc import *


def connect_to_db():
    # Dictionary, containing the connection details.
    details = {
        'server': 'water-measurements.database.windows.net',
        'database': 'water-measurements',
        'username': 'bossman@water-measurements',
        'password': 'Itu2019!'
    }

    # Connection string is made up using the '.format' method and the details from the dictionary
    connect_string = 'Driver={{ODBC Driver 13 for SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};'.format(
        **details)
    global connection
    connection = connect(connect_string)


def get_records():
    connect_to_db()
    cursor = connection.cursor()
    return cursor.execute('SELECT * FROM Measurements_raw')


def save_record(record):
    connect_to_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Measurements_raw (Json_value) VALUES(?)", record)
    connection.commit()
