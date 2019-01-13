from microphone import Microphone
import json

class Recorder(object):
    def __init__(self):
        self.mic = Microphone()
        self.__setup()

    def __setup(self):
        with open('config.json', 'r') as f:
            config  = json.load(f)
        api_key = config['api_key']
        if api_key == "":
            print("NO API KEY PROVIDED!!!")
            exit(-1)
        # host    = config['host']
        # port    = config['port']
        
        self.mic.set_api_key(api_key)

    def listen_to_command(self, mode='auto', duration=None):
        return self.mic.get_command(mode, duration)

    def parse_response(self, response):
        # returns the decoded text if speech is detected
        # else returns None 
        try:
            cmd = response.pop('DisplayText')
            cmd = cmd.replace('.', '')
            cmd = cmd.lower()
            return cmd
        except KeyError:
            return None

if __name__=='__main__':
    rec = Recorder()
    while True:
        print('Press ENTER to start recording: ')
        input()
        response = rec.listen_to_command()
        result = rec.parse_response(response)
        print(result)