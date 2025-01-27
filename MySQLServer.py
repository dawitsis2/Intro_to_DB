import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server (without selecting a database)
        connection = mysql.connector.connect(
            host='localhost',        # Change if your MySQL server is hosted elsewhere
            user='your_username',    # Replace with your MySQL username
            password='your_password' # Replace with your MySQL password
        )
        
        if connection.is_connected():
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            # Close the cursor and connection
            cursor.close()
            connection.close()
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

if __name__ == "__main__":
    create_database()
