from pyodbc import *

# Dictionary, containing the connection details.
details = {
    'server': 'water-measurements.database.windows.net',
    'database': 'water-measurements',
    'username': 'bossman@water-measurements',
    'password': 'Itu2019!'
}

# Connection string is made up using the '.format' method and the details from the dictionary
connect_string = 'Driver={{ODBC Driver 13 for SQL Server}};Server={server};Database={database};Uid={username};Pwd={password};'.format(**details)


connection = connect(connect_string)
print(connection)

cursor = connection.cursor()
cursor.execute('SELECT * FROM Measurements_raw')

for row in cursor:
    print(row)