import sqlite3

conn = sqlite3.connect('gorevler.db')

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE gorevler (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               baslik TEXT,
               aciklama TEXT,
               oncelik TEXT,
               durum INTEGER
               ) 
               """)

conn.commit()

conn.close()
