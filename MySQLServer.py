import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Attempt to connect to MySQL without a password
        connection = mysql.connector.connect(
            host='localhost',        # MySQL server host
            user='root'              # MySQL username
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
            cursor.close()
            connection.close()
    
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == "__main__":
    create_database()
