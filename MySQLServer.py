import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (update user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # set your MySQL root password if needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
                connection.close()
    except Error as e:
        print(f"except mysql.connector.Error")

if __name__ == "__main__":
    create_database()
