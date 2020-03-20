""" 

The job of this file is to take audio from iPhone Memos and create a transcript 
This file will:
    1. Pull .m4a files from downloads and place them in 'Unconverted_Audio'
    2. Call convertAudio.py to convert .m4a files in 'Unconverted_Audio' and place a copy into 'Converted_Audio'
    3. Call speechRecognition.py to create a transcript of the file

"""

import os
from os import path
import convertAudio

directory = path.dirname(path.realpath(__file__))   # This path
downloads = "/Users/koya/Downloads"                 # Path to downloads

usedAudio = []

for root,dirs,files in os.walk(directory + '/Unconverted_Audio'):
    for file in files:
        if not file.startswith('.'):
            usedAudio.append(file)

print("Searching downloads...")
for root,dirs,files in os.walk(downloads): 
    for file in files:                      
        if not file.startswith('.') and file.endswith('.m4a'):
            if input("Move " + file + "from downloads to be used?[y/n]  |  ") == 'y':
                newDir = directory + '/Unconverted_Audio/' + file

                os.rename(downloads + '/' + file, newDir)
                usedAudio.append(newDir)

for audioFile in usedAudio:
    print('-'*25,'\nAUDIOFILE:',audioFile, '\n' + '-'*25)
    convertAudio.convert(directory+'/Unconverted_Audio/'+audioFile, 'wav', audioFile[:-4])