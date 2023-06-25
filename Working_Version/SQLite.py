#!/usr/bin/env python3
"""Imports"""
import sqlite3
from sqlite3 import Error as err


def SQL_In_Memory():
    """Creates a Database In Memory Using SQLite"""
    try:

        # Creates connection to an in-memory database

        Mem_DB = ':memory:'
        File_DB = 'main.db'

        conn = sqlite3.connect(Mem_DB)
        print("Connected To Database In Memory.")

        # Creates a cursor object that can execute SQL statements
        cursor = conn.cursor()

        # Execute SQL Statements
        cursor.execute('CREATE TABLE Leaderboard (id INT, name TEXT, score INT)')
        print("Table Created.")

        cursor.execute("INSERT INTO Leaderboard VALUES (1, 'Gavin', 100)")
        cursor.execute("INSERT INTO Leaderboard VALUES (2, 'Nacho', 92)")
        cursor.execute("INSERT INTO Leaderboard VALUES (3, 'Colan', 73)")
        print("Data inserted.")

        # Commit changes
        conn.commit()
        print("Changes committed to Database.")

        # Fetch all records from Leaderboard Table
        cursor.execute('SELECT * FROM Leaderboard')
        rows = cursor.fetchall()

        # Print Records by Row
        print("Output:\n")
        for row in rows:
            print(row)

        print("\n")

    except err:
        print(err)


    finally:

        if cursor:
            cursor.close()
            print("Cursor closed.")

        if conn:
            conn.close()
            print("Connection closed.")
