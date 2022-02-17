import sys
import speech_recognition as sr
import os

import spotipy
import sys
import pprint
from time import sleep
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import speech_recognition as sr

r = sr.Recognizer()

def writeToFile(theFile, toWrite):
	f = open(theFile, "a")
	f.write(toWrite)
	f.write("\n")
	return 1

def readFromFile(theFile):
	f = open(theFile, "r")
	return f.read()

def copyFile(aFile, bFile):
	# Copies contents from aFile to bFile
	writeToFile(bFile, readFromFile(aFile))
	return 1

def cacheVoiceCommand(command):
	f = "voiceCommandCache.txt"
	writeToFile(f, command)
	return 1

def clearVoiceCommandCache():
	os.remove("./voiceCommandCache.txt")

def getVerify():
	vox = ""
	while vox == "":
		vox = getVoiceInput()
	if vox == "yes":
		print("You said yes")
		return 1
	elif vox == "no":
		print("You said no")
		return 0
	else:
		print("I'm not sure what you said..")
	getVerify()
	return -1

def getVoiceInput():
	try:
		#sp.volume(0)
		#r = sr.Recognizer()
		with sr.Microphone() as source:
			audio = r.listen(source, phrase_time_limit=5)
			#print("done listening")
			returnString = r.recognize_google(audio)
			#sp.volume(100)
		if returnString == "exit":
			cacheVoiceCommand("exit")
			sys.exit("Spoken Exit")
		cacheVoiceCommand(returnString)
		return returnString
	except:
		print("No input received")
		return ""

