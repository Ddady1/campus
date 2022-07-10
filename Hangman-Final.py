def hang_photos(photo_num):
    HANGMAN_PHOTOS = {6: '''    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |''', 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 1: '''    x-------x''', 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    return HANGMAN_PHOTOS[photo_num]

def choose_word(file_path, index):

    with open(file_path, 'r') as word_read:
        content = word_read.read()
        items = content.split(' ')
        return items[int(index) - 1]

def hangma_main_pic():
    pic = '''Welcome to the game Hangman

     _    _
    | |  | |
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |
                        |___/ \n'''

    return pic


def main():
    MAX_TRIES = 6
    print(hangma_main_pic(), MAX_TRIES)
    print(hang_photos(3))
    f_path = input('Please enter file path: ')
    word_num = input('Please enter a num: ')
    print(secret_word=(choose_word(f_path, word_num)))










if __name__ == "__main__":
    main()