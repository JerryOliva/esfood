import databases
import sqlite3

def insertUser():
    connection=sqlite3.connect('data_food.db')
    cursor=connection.cursor()
    cursor.execute(' INSERT INTO es_lovers VALUES ()')