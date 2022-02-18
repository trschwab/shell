from sensitive.environment_variables import *
from utility.utility import *

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

res = sp.devices()
pprint(res)

def getVoiceInput():
	try:
		#sp.volume(0)
		#r = sr.Recognizer()
		with sr.Microphone() as source:
			audio = r.listen(source, phrase_time_limit=5)
			#print("done listening")
			returnString = r.recognize_google(audio)
			sp.volume(100)
		if returnString == "exit":
			cacheVoiceCommand("exit")
			sys.exit("Spoken Exit")
		cacheVoiceCommand(returnString)
		return returnString
	except:
		print("No input received")
		return ""

def getSpotifySearch(vox):
	if vox == "":
		print("No input received for getSpotifySearch(), return -1")
		return -1
	result = sp.search(vox)
	return result

def getSpotifyResults(search):
	if search == -1:
		print("No input offered, returning")
		return
	for i in range(len(search['tracks']['items'])):
		print("Result " + str(i) + ":")
		print("\tTrack: " + search['tracks']['items'][i]['name'])
		print("\tArtist: " + search['tracks']['items'][i]['artists'][0]['name'])
		print("\tURI for Track: " + search['tracks']['items'][i]['uri'])
		
		print("Is this the correct Track information? Say yes or no\n")
		verify_info = getVerify()	
		if verify_info == 1:
			print("Ok, I'll play that track...")
			sp.start_playback(uris=[search['tracks']['items'][i]['uri']])
			#sp.volume(100)
			break
		else:
			print("Ok, not correct... showing you the next result...")


def shuffleOn():
	sp.shuffle(True)
	return 1
	
def shuffleOff():
	sp.shuffle(False)
	return 1

def spotifyPlay(voxSplit):
	if voxSplit[2] == "song":
		print("spotify play song:")
		print(voxSplit[3:])
		print(" ".join(voxSplit[3:]))
		search = " ".join(voxSplit[3:])
		result = getSpotifySearch(search)
		getSpotifyResults(result)
	return 1

def spotifyAct(voxSplit):
	if voxSplit[1] == "play":
		spotifyPlay(voxSplit)
	if voxSplit[1] == "next":
		if voxSplit[2] == "track":
			print("Spotify play next song: ")
			sp.next_track()
	if voxSplit[1] == "last":
		if voxSplit[2] == "track":
			print("Spotify play last song: ")
			sp.previous_track()
	return 1

def spotifyMain(voxSplit):
	if voxSplit[0] == "Spotify":
		spotifyAct(voxSplit)
	print("end")
	return 1

