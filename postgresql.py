#!/usr/bin/python

import psycopg2
from config import config

def createTable(query):
    connection = None
    try:
        params = config()

        # connect to the PostGreSQL Server
        print('Connecting to the PostGreSQL Database Server...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        # Inserting a row into the mobile table
        cursor.execute(query)
        connection.commit()
        print('Table has been created')
        cursor.close()

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

def insertRow(id, name, price):
    connection = None

    try:
        params = config()

        # connect to the PostGreSQL Server
        print('Connecting to the PostGreSQL Database Server...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        # Inserting a row into the mobile table
        cursor.execute('INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)',
                       (id, name, price)
                       )
        connection.commit()
        print('Row with id', id, 'has been inserted')
        cursor.close()

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

def readTable(tableName):
    connection = None

    try:
        params = config()

        # connect to the PostGreSQL Server
        print('Connecting to the PostGreSQL Database Server...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        postgres_read_query = "SELECT * FROM " + tableName
        cursor.execute(postgres_read_query)

        # Reading from the table
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")

        for row in mobile_records:
            print("ID =", row[0])
            print("Model =", row[1])
            print("Price =", row[2], "\n")


        cursor.close()

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

def updateRow(id, price):
    connection = None

    try:
        params = config()
        # connect to the PostGreSQL Server
        print('Connecting to the PostGreSQL Database Server...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        # Update the table
        postgres_update_query = "UPDATE mobile SET price = %s WHERE id = %s"
        cursor.execute(postgres_update_query, (price, id))
        connection.commit()
        print('Row with id', id, 'has been updated')
        cursor.close()

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

def deleteRow(id):
    connection = None

    try:
        params = config()
        # connect to the PostGreSQL Server
        print('Connecting to the PostGreSQL Database Server...')
        connection = psycopg2.connect(**params)

        # Create a cursor
        cursor = connection.cursor()

        # Update the table
        postgres_delete_query = "DELETE from mobile WHERE id = %s"
        cursor.execute(postgres_delete_query, (id, ))
        connection.commit()
        print('Row with id', id, 'has been deleted')
        cursor.close()

    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')


if __name__ == '__main__':
    # createTable('''CREATE TABLE mobile
    #               (ID INT PRIMARY KEY     NOT NULL,
    #               MODEL           TEXT    NOT NULL,
    #               PRICE         REAL); ''')
    # insertRow(10, 'Google Pixel', 1000)
    # updateRow(10, 1100)
    # deleteRow(10)
    readTable("mobile")

