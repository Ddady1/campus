def my_mp4_playlist(file_path, new_song):
    '''Get's file with lines. Each line contains sond name, singer and song lenght
    info in each line divided with ';'
    example: Tudo Bom;Static and Ben El Tavori;5:13;
    if there are less than 3 lines only add song name at the thord line'''


    with open(file_path, 'r') as f_read:
        data = f_read.readlines()
        print(data)
        f_read.close()

        num = len(data)
        if num < 3:
            data.append((3 - num) * '\n')
            data.append(new_song)
        else:
            line2 = data[2]
            f_data = data[2].split(';')
            f_data.pop(0)
            f_data.insert(0, new_song)
            f_data = ';'.join(f_data)
            data.remove(line2)
            data.insert(2, f_data)

    with open(file_path, 'w') as f_write:
        for line in data:
            f_write.write(line)



        ''' Need to convert data to string in order to write to file
or run loop through data and write each line to file'''



        print(num)
        print(data[2])
        print(len(data[2]))
        #print(f_data)
        print(data)







my_mp4_playlist(r"c:\campus\songs.txt", "Python Love Story")