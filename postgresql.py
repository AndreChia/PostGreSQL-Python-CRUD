#!/usr/bin/python

import psycopg2
from config import config

def connect():
    # Connect to the PostGreSQL Database Server
    connection = None
    try:
        # read connection paramteres
        params = config()

        # connect to the PostGreSQL Server
        print('Connecting to the PostGreSQL Database Server...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        # Creating a table
        create_table_query = '''CREATE TABLE mobile
              (ID INT PRIMARY KEY     NOT NULL,
              MODEL           TEXT    NOT NULL,
              PRICE         REAL); '''


        # Inserting a row
        cursor.execute('INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)',
                       (42, 'ASUS ROG', 1300)
                       )

        # Reading from the table
        postgres_read_query = "SELECT * FROM mobile"
        cursor.execute(postgres_read_query)

        # Update the table
        postgres_update_query = "UPDATE mobile SET price = %s WHERE id = %s"
        cursor.execute(postgres_update_query, (1200, 39))

        # Delete a row from the table
        postgres_delete_query = "DELETE from mobile WHERE id = %s"
        cursor.execute(postgres_delete_query, (39, ))

        # Reading from the table
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")

        for row in mobile_records:
            print("ID =", row[0])
            print("Model =", row[1])
            print("Price =", row[2], "\n")

        # Commit the connection and change into the database
        connection.commit()

        # Close the connection
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()

