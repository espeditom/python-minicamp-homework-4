import sqlite3

connection = sqlite3.connect('database.db')
print ('Were connected') 

connection.execute( 'CREATE TABLE movies (movie TEXT, year INTEGER, genre TEXT)')
print ('Movie Table created!')

connection.close()
