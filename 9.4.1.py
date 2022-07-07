def choose_word(file_path, index):

    with open(file_path, 'r') as file_con:
        content = file_con.read()
        items = content.split(' ')
        num = len(items)
        solid = []
        for n in items:
            if n in solid:
                pass
            else:
                solid.append(n)
        solid_num = len(solid)
        if index / 2 >= len(items):
            index = (index / 2 - len(items)) + 0.5
            word = items[int(index) - 1]
        elif index > len(items):
            index = index - len(items)
            word = items[index - 1]
        else:
            word = items[index - 1]

        mytup = (solid_num, word)
        return mytup





print(choose_word(r"c:\campus\words.txt", 9))
#choose_word(r"c:\campus\words.txt", 15)