from utility.utility import *
from module.spotify import *

r = sr.Recognizer()

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



