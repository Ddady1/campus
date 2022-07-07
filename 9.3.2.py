def my_mp4_playlist(file_path, new_song):


    with open(file_path, 'r') as f_read:
        data = f_read.readlines()

    #with open(file_path, 'w') as f_write:
        num = len(data)
        f_data = data[num - 1].split(';')
        f_data.pop(0)
        f_data.insert(0, new_song)
        f_data = ';'.join(f_data)

        if num < 3:
            data.append( (3 - num) * '\n')
            data.append(new_song)
        else:
            data.append(f_data)

    with open( file_path, 'w') as f_write:
        f_write.write(data)

        print(len(data))
        print(data[2])
        print(len(data[2]))
        print(f_data)
        print(data)







my_mp4_playlist(r"c:\campus\songs.txt", "Python Love Story")