#!/usr/bin/env python3
"""Imports"""
import sqlite3
from sqlite3 import Error as err
import pandas as pd


def SQL_In_Memory():
    """Create a Database In Memory Using SQLite"""
    try:

        # Creates connection to an in-memory database
        Mem_DB = ':memory:'
        File_DB = 'main.db'

        # Step 1 == Create A Connection



        # Step 2 == Create a cursor object that can execute SQL statements



        # Step 3 == Create Two Tables With Random Information



        # Step 4 == Commit changes










        #Prints Data
        Print_Data(cursor)








        # SQL Questions


        # Question 1: Retrieve all columns from the "Leaderboard" table.


        cursor.execute("") ## TO DO


        leaderboard_data = cursor.fetchall()
        print("\nQuestion 1: Retrieve all columns from the 'Leaderboard' table.")
        print(leaderboard_data)



        # Question 2: Find the unique values in the "Name" column of the "Leaderboard" table.


        cursor.execute("") ## TO DO


        unique_names = cursor.fetchall()
        print("\nQuestion 2: Find the unique values in the 'Name' column of the 'Leaderboard' table.")
        print(unique_names)



        # Question 3: Retrieve all records from the "Leaderboard" table where the "Score" column is greater than 80.


        cursor.execute("") ## TO DO


        high_score_players = cursor.fetchall()
        print("\nQuestion 3: Retrieve all records from the 'Leaderboard' table where the 'Score' column is greater than 80.")
        print(high_score_players)


        # Question 4: Sort the "Leaderboard" table in descending order based on the "Score" column.


        cursor.execute("") ## TO DO


        sorted_leaderboard = cursor.fetchall()
        print("\nQuestion 4: Sort the 'Leaderboard' table in descending order based on the 'Score' column.")
        print(sorted_leaderboard)


        # Question 5: Retrieve the top 3 records from the "Leaderboard" table.


        cursor.execute("") ## TO DO


        top_players = cursor.fetchall()
        print("\nQuestion 5: Retrieve the top 3 records from the 'Leaderboard' table.")
        print(top_players)


        # Question 6: Perform a UNION of two SELECT statements to combine the records from two tables.
        # (Replace "Winners" table with the appropriate table name)


        cursor.execute("") ## TO DO


        combined_records = cursor.fetchall()
        print("\nQuestion 6: Perform a UNION of two SELECT statements to combine the records from two tables.")
        print(combined_records)


        # Question 7: Find the players who have a score higher than the average score in the Leaderboard table and sort them in descending order of their scores.


        cursor.execute("") ## TO DO


        high_score_players = cursor.fetchall()
        print("\nQuestion 7: Find the players who have a score higher than the average score in the Leaderboard table and sort them in descending order of their scores.")
        print(high_score_players)

        print("\n\n")

    except err:
        print(err)


    finally:

        if cursor:
            cursor.close()
            print("Cursor closed.")

        if conn:
            conn.close()
            print("Connection closed.")


def Print_Data(cursor):
    # Fetch all records from Leaderboard Table
    cursor.execute('SELECT * FROM Leaderboard')
    rows = cursor.fetchall()

    # Print All Data In Table Visually
    df = pd.DataFrame(rows, columns=['id', 'name', 'score'])
    print("\nAll Data: Leaderboard\n{}\n".format(df))

    # Fetch all records from Winners Table
    cursor.execute('SELECT * FROM Winners')
    rowsX = cursor.fetchall()

    # Print All Data In Table Visually
    dfX = pd.DataFrame(rowsX, columns=['name'])
    print("\nAll Data: Winners\n{}\n".format(dfX))
