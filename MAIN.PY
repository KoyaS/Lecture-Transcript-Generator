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
import speechRecognition

def moveFromDownloads():
	"""
	searches downloads for .m4a files and moves them to Unconverted_Audio
	returns: list of files it moved
	"""
	usedAudio = []
	print("Searching downloads...")
	downloads = "/Users/koya/Downloads" # Path to downloads
	for root,dirs,files in os.walk(downloads): 
		for file in files:                      
			if not file.startswith('.') and file.endswith('.m4a'):
				if input("Move " + file + " from downloads to be used?[y/n]  |  ") == 'y':

					os.rename(downloads + '/' + file, 'Unconverted_Audio/' + file)
					usedAudio.append(file)
	return(usedAudio)

def searchUnconvertedAudio():
	"""
	Compiling list of convertable files in Unconnverted_Audio
	"""
	usedAudio = []
	print("Searching Unconverted_Audio...")
	for root,dirs,files in os.walk('Unconverted_Audio'):
		for file in files:
			if file.endswith('.m4a'):
				usedAudio.append(file)
	return(usedAudio)

moveFromDownloads()
toConvert = searchUnconvertedAudio()
print("Files to be converted: \n", toConvert)
for audioFile in toConvert:
	print('-'*25,'\nAUDIOFILE:',audioFile, '\n' + '-'*25)
	convertAudio.convert(audioFile, 'wav')
	speechRecognition.recognize(audioFile[:-4]+'.wav')
	os.rename('Unconverted_Audio/' + audioFile, 'Processed_Audio/' + audioFile)




