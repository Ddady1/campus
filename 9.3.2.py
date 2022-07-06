def my_mp4_playlist(file_path, new_song):


    with open(file_path, 'r') as f_read:
        data = f_read.readlines()

    #with open(file_path, 'w') as f_write:
        f_data = data[2].split(';')
        f_data.pop(0)
        f_data.insert(0, new_song)
        print(data[2])
        print(len(data[2]))
        print(f_data)






my_mp4_playlist(r"c:\campus\songs.txt", "Python Love Story")