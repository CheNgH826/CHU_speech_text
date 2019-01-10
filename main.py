from recorder import Recorder
from speaker import Speaker
import string

conversation_path = 'conversation.txt'

with open(conversation_path) as f:
    dialog = [s[:-1] for s in list(f)]

def remove_punc(s):
    for c in string.punctuation:
        s = s.replace(c, '')
    return s

rec = Recorder()
speaker = Speaker()
for sentence in dialog:
    correct = False
    while not correct:
        print('please read this: '+sentence)
        # print('Press ENTER to start recording: ')
        # input()
        response = rec.listen_to_command()
        result = rec.parse_response(response)
        result = remove_punc(result.lower())

        print('What you read: '+result)
        if result == sentence:
            print('CORRECT! Let\'s move on.\n')
            correct = True
        elif result == 'please quit':
            exit(-1)
        else:
            print('INCORRECT! Please listen and try again.\n')
            speaker.speak(sentence)