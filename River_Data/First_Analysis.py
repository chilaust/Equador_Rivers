import csv
import sqlite3 as sql
import os

conn = sql.connect("River_Data.db")
cursor = conn.cursor()



folder_path = './River_Data'
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

for file in csv_files:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    date_time TEXT,
    low_range REAL,
    temp REAL
            )
    ''')

    conn.commit()

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            cursor.execute('''
            INSERT INTO data (date_time, low_range, temp)
            VALUES (?, ?, ?)
        ''', row)
    conn.commit()
    