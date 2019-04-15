import sqlite3


connection = sqlite3.connect('menusection.db')
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS menusections (id INTEGER PRIMARY KEY, name text)"
cursor.execute(create_table)
connection.commit()
connection.close()
