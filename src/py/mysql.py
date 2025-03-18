import pymysql

# Database connection details
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'port': 8080,
    'database': 'your_database_name'
}

connection=""

# Establishing the connection
try:
    connection = pymysql.connect(
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        database=config['database']
    )
    print("Successfully connected to the database")
except pymysql.MySQLError as err:
    print(f"Error: {err}")
finally:
    if connection:
        connection.close()
        print("Connection closed")