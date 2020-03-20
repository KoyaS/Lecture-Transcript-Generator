''' Speech recognition from an audio file '''

import speech_recognition as sr
from os import path
import sys

# directory = path.dirname(path.realpath(__file__))
directory = "/Users/koya/Desktop/Projects/Speech-Recognition"

# try:
#     AUDIO = directory + '/Converted_Audio/' + sys.argv[1] # Takes name of file as parameter (converted .wav)
# except:
#     print("NO FILENAME GIVEN, PASS AS PARAMETER TO PY FILE")
#     AUDIO = 'newAudio.wav'

def recognize(fileName):

    AUDIO = directory + '/Converted_Audio/' + fileName

    r = sr.Recognizer()

    with sr.AudioFile(AUDIO) as source:
        f = open('Transcripts/' + fileName[:-4] + ".txt","w+")
        r.adjust_for_ambient_noise(source)
        print("Listening")

        for i in range(int(source.DURATION/5)):
            try:
                audio = r.listen(source)
                transcript = r.recognize_google(audio, show_all=False) # Can set show_all=True for alternative readings
                f.write(transcript+'\n')
            except Exception as e:
                print(e)

        # r = sr.Recognizer()
        # r.pause_threshold = 2
        # audio = r.listen(source)
        # f.write(r.recognize_google(audio, show_all=False))

    f.close()

recognize('unconverted.wav')
