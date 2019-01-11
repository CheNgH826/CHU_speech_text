import sqlite3
from pprint import pprint

sqlite_connection = sqlite3.connect('sqlite/log.db')
sqlite_cursor = sqlite_connection.cursor()

print("Retrieving entries (limited to 5) from SQLite log...")
sqlite_cursor.execute('''SELECT * FROM user_answers LIMIT 5;''')
pprint(sqlite_cursor.fetchall())

sqlite_connection.close()