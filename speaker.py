import os, requests, time
import json
# import pyaudio, wave

class Speaker(object):
    def __init__(self):

        with open('config.json', 'r') as f:
            config  = json.load(f)
        
        # self.__API_KEY  = config['tts']['api_key']
        self.__API_KEY  = config['api_key']
        print()
        # self.__RESOURCE_NAME = config['tts']['resource_name']
        self.__RESOURCE_NAME = config['resource_name']
        self.__REGION   = 'westus'
        # self.__MODE     = 'interactive' 
        self.__LANG     = 'en-US'#'zh-TW'
        # self.__FORMAT   = 'simple'
        self.__AT_URL   = f'https://{self.__REGION}.api.cognitive.microsoft.com/sts/v1.0/issueToken'
        self.__get_token()

    def __get_token(self):
        headers = {'Ocp-Apim-Subscription-Key': self.__API_KEY}
        response =  requests.post(self.__AT_URL, headers=headers)
        self.__TOKEN = str(response.text)
        
    def __text2wav(self, text):
        url  =f'https://{self.__REGION}.tts.speech.microsoft.com/cognitiveservices/v1'
        headers = {
                'Authorization': 'Bearer ' + self.__TOKEN,
                'Content-Type': 'application/ssml+xml',
                'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
                'User-Agent': self.__RESOURCE_NAME,
                'cache-control': 'no-cache'
                }

        body = "<speak version='1.0' xml:lang='en-US'><voice xml:lang='en-US' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)'>" + text + "</voice></speak>"

        response = requests.post(url, headers=headers, data=body)

        if response.status_code == 200:
            with open('sample.wav', 'wb') as audio:
                audio.write(response.content)
                # print("\nStatus code: " + str(response.status_code) + "\nYour TTS is ready for playback.\n")
        else:
            print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

    def __play_wav(self):
        os.system('aplay sample.wav -q')

    def speak(self, text):
        self.__text2wav(text)
        self.__play_wav()

if __name__ == '__main__':
    s = Speaker()
    s.speak('hello world')