import sqlite3, os

# SQLite
sqlite_connection = sqlite3.connect('../database/sqlite/log.db')
sqlite_cursor = sqlite_connection.cursor()

sqlite_cursor.execute('''CREATE TABLE user_answers
						(time TEXT, correct INTEGER, user_input TEXT, real_answer TEXT)''')

sqlite_connection.commit()
sqlite_connection.close()

# MongoDB
mongodb_dir = '../database/mongodb'
if not os.path.exists(mongodb_dir):
    os.makedirs(mongodb_dir)