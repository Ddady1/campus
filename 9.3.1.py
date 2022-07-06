def my_mp3_playlist(file_path):

    with open(file_path, 'r') as f:
        content = f.read()
        items = content.split('\n')
        print(items)
        #print(items[0])
        songs = []
        for item in items:
            item = item.rstrip(';')
            item = item.replace(':', '.')
            print(item)
            songs.append(item.split(';'))
        tup = ()
        a = 0
        for song in songs:
            if float(song[len(song) - 1]) > a:
                a = float(song[len(song) - 1])
                song_len = song[0]
        b = len(songs)


        band_str = []
        for n in songs:
            band_str.append(n[1])
        c = 0
        for fl in range(len(band_str)):
            num = band_str.count(band_str[fl])
            if num > c:
                band_name = band_str[fl]
                c = num
            fl += 1


    tup = (song_len, b, band_name)
    return tup










print(my_mp3_playlist(r"c:\campus\songs.txt"))