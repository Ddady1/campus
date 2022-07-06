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
        b = len(songs)

        c = 0
        for n in songs:
            for nf in n:

    tup = (str(a), b, c)
    return tup










print(my_mp3_playlist(r"c:\campus\songs.txt"))