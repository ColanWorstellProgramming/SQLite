#!/usr/bin/env python3
import sqlite3
import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Create an in-memory database

Mem_DB = ':memory:'
File_DB = 'image.db'


conn = sqlite3.connect(Mem_DB)
cursor = conn.cursor()

# Create the table to store real-time data
cursor.execute("CREATE TABLE Analytics (timestamp TIMESTAMP, metric TEXT, value REAL)")

# Generate and insert random data every second
while True:
    # Generate a random metric and value
    metric = random.choice(["Visitors", "Sales", "Clicks"])
    value = random.randint(10, 100)

    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Insert the data into the database
    cursor.execute("INSERT INTO Analytics VALUES (?, ?, ?)", (timestamp, metric, value))
    conn.commit()

    # Retrieve the latest data for visualization
    cursor.execute("SELECT timestamp, metric, value FROM Analytics")
    data = cursor.fetchall()

    # Extract the timestamps and values for plotting
    timestamps = [row[0] for row in data]
    values = [row[2] for row in data]

    # Clear the previous plot and create a new one
    plt.clf()
    plt.plot(timestamps, values, marker="o")
    plt.title("Real-Time Analytics Dashboard")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("realtime_plot.png")  # Save the plot as an image file
    plt.close()

    time.sleep(1)  # Pause for 1 second before updating the plot

    # Fetch all records from Leaderboard Table
    cursor.execute('SELECT * FROM Analytics')
    rows = cursor.fetchall()

    # Print All Data In Table Visually
    df = pd.DataFrame(rows, columns=["Visitors", "Sales", "Clicks"])
    print("\nAll Data: Leaderboard\n{}\n".format(df))
