from utility.utility import *
from module.spotify import *

r = sr.Recognizer()

def getMode():
	print("Please speak the mode")
	vox = ""
	while vox == "":
		vox = getVoiceInput()
	print("You chose mode: " + vox)
	if vox == "spotify":
		print("Run spotify")
		return vox
	else:
		print("Other mode")
		return vox
	return -1


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

def getPlaylist(search):
	playlistName = "Let's Dance".lower()
	playlistName = search.lower()
	j = 0
	while j < 100:
		results = sp.current_user_playlists(limit=50, offset=j*50)
		for i, item in enumerate(results['items']):
			if item['name'].lower() == playlistName:
				return item['uri']
		j += 1
	print("No playlist found of that name, please try again")
	return -1

def main():
	print("Hello")
	#While True:
	vox = getVoiceInput()
	print("vox: " + vox)
	voxSplit = vox.split(" ")
	print("vox split: ")
	print(voxSplit)
	if (voxSplit[0] == "delete" and voxSplit[1] == "history"):
		clearVoiceCommandCache()
	if (voxSplit[0] == "Spotify"):
		spotifyMain(voxSplit)

main()



