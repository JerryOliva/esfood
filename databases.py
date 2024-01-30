import sqlite3

#create databases required to administrate start up data 

#customer buy database
connection= sqlite3.connect('data_food.db')
cursor= connection.cursor()
cursor.execute('''CREATE TABLE customer_buy(name TEXT NOT NULL,
                            l_name TEXT NOT NULL, number_articles INTEGER , description_article TEXT NOT NULL, total REAL)''')
connection.close()

#inventory administration database
connection=sqlite3.connect('data_food.db')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE inventory(description_article TEXT NOT NULL,
                         quantity INT, unitary_cost REAL, 
                         brand TEXT NOT NULL, price REAL,
                        date_in TEXT NOT NULL, date_out TEXT NOT NULL)''')
connection.close()

#registrants database
connection=sqlite3.connect('data_food.db')
c=connection.cursor()
c.execute('''CREATE TABLE es_lovers(name TEXT NOT NULL,
                    l_name TEXT NOT NULL, ocupation TEXT NOT NULL,
                    town TEXT NOT NULL, estate TEXT NOT NULL,
                    email TEXT NOT NULL, telephone TEXT NOT NULL)''')
connection.close()



