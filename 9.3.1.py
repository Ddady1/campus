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
        for n in range(len(items) - 1):
            temp = items.count(song[2])
            if temp > c:
                c = temp
            n += 1

    print(a, b, c)










print(my_mp3_playlist(r"c:\campus\songs.txt"))