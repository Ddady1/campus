"""Changes the content of a playlist, read from a given file. The changed playlist is writen back to the same file.
:param: file_name: the path of the file contains the playlist
:param: new_song: a new name, to cjange the name of a song from the list
:type: strings
"""
def my_mp4_playlist(file_path, new_song):
	fid = open(file_path, "r")
	lines = fid.readlines()
	fid.close()
	if len(lines) >= 3:
		lines[2] = new_song + lines[2][lines[2].find(';'):]
		#open(file_path, "w").writelines(lines)
	else:
		for n in range(2 - len(lines)):
			lines.append("\n")
		lines.append(new_song+ ";")
		#open(file_path, "w").writelines(lines)
	#print(open(file_path, "r").read())
	text=''
	for i in range(len(lines)):
		text=text+lines[i]
	print(text)