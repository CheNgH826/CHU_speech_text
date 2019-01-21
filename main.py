import string, sqlite3, datetime
from recorder import Recorder
from speaker import Speaker
from pymongo import MongoClient

conversation_path = 'conversation.txt'

with open(conversation_path) as f:
    dialog = [s[:-1] for s in list(f)]

def remove_punc(s):
    for c in string.punctuation:
        s = s.replace(c, '')
    return s

rec = Recorder()
speaker = Speaker()
# Connect with SQLite
sqlite_connection = sqlite3.connect('database/sqlite/log.db')
sqlite_cursor = sqlite_connection.cursor()
# Connect with MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')

for i, sentence in enumerate(dialog):
    correct = False
    while not correct:
        print('[{}/{}] please read this: '.format(i+1, len(dialog))+sentence)
        print('Press ENTER to start recording: ', end='')
        input()
        response = rec.listen_to_command(mode='manual', duration=3)
        print(response)
        result = rec.parse_response(response)
        result = remove_punc(result.lower())

        print('What you read: '+result)
        if result == sentence:
            print('CORRECT! Let\'s move on.\n')
            correct = True
        elif result == 'please quit':
            sqlite_connection.close()
            exit(-1)
        else:
            print('INCORRECT! Please listen and try again.\n')
            speaker.speak(sentence)

        # Insert into SQLite
        sqlite_cursor.execute("INSERT INTO user_answers VALUES (?,?,?,?)",(
                str(datetime.datetime.now()), # time
                int(correct), # correct
                result, # user_input
                sentence # real_answer
            )
        )
        sqlite_connection.commit()

        # Insert into MongoDB
        mongo_client.log.user_answers.insert_one({'time': datetime.datetime.now(), 'correct': correct,
                                                'user_input': result, 'real_answer': sentence})

sqlite_connection.close()
