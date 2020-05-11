''' Speech recognition from an audio file '''

import speech_recognition as sr
from os import path
import sys

def recognize(fileName):

    AUDIO = 'Converted_Audio/' + fileName

    r = sr.Recognizer()

    print('speechRecognition.py: ')
    print('Opening ' + fileName + '...')

    with sr.AudioFile(AUDIO) as source:
        f = open('Transcripts/' + fileName[:-4] + ".txt", "w+")
        r.adjust_for_ambient_noise(source)
        print("Listening")

        for i in range(int(source.DURATION/5)):
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio, show_all=False) # Can set show_all=True for alternative readings
                f.write(transcript+'\n')
            except Exception as e:
                print(e)

    f.close()
    print('\n'*3)

if __name__ == '__main__':
    recognize(sys.argv[1])
