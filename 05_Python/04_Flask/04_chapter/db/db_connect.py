import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='schooldb',
            port=3307
        )

        if connection.is_connected():
            print('MySQL Database Connected Successfully')

        return connection

    except Error as e:
        print(f'MySQL Connection Error: {e}')
        return None


conn = get_connection()