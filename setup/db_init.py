import sqlite3, os

# SQLite
sqlite_dir = '/dock/database/sqlite'
if not os.path.exists(sqlite_dir):
    os.makedirs(sqlite_dir)
sqlite_connection = sqlite3.connect('{}/log.db'.format(sqlite_dir))
sqlite_cursor = sqlite_connection.cursor()

sqlite_cursor.execute('''CREATE TABLE IF NOT EXISTS user_answers
						(time TEXT, correct INTEGER, user_input TEXT, real_answer TEXT)''')

sqlite_connection.commit()
sqlite_connection.close()

# MongoDB
mongodb_dir = '/dock/database/mongodb'
if not os.path.exists(mongodb_dir):
    os.makedirs(mongodb_dir)