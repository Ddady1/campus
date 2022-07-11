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

def check_win(secret_word, old_letters_guessed):

    answer = True
    for n in secret_word:

        if n in old_letters_guessed:
            answer = True
        else:
            answer = False
            return answer
    return answer

def show_hidden_word(secret_word, old_letters_guessed):

    new_lst = list(secret_word)
    l_str = ['_'] * len(secret_word)
    for n in old_letters_guessed:
        if n in new_lst:
            for i in range(secret_word.count(n)):
                pos = new_lst.index(n)
                l_str[pos] = n
                new_lst[pos] = '_'
    l_str = ' '.join(l_str)
    return l_str

def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    ''' Function check if input is valid and tries to update old_letters_guessed.
    :param letter_guessed: guessed letter value
    :param old_letters_guessed: old letters guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: result if input is valid
    :rtype: booelean
    '''

    letter_guessed = letter_guessed.lower()
    old_letters_guessed.sort()
    if letter_guessed in old_letters_guessed:
        print('X')
        print(' -> '.join(old_letters_guessed))
        #return ('X', ' -> '.join((old_letters_guessed)))
        return False
    elif len(letter_guessed) >= 2 or not letter_guessed.isalpha():
        print('X')
        print(' -> '.join(old_letters_guessed))
        return False
        #return ('X', ' -> '.join((old_letters_guessed)))

    elif letter_guessed in secret_word:
        old_letters_guessed.append(letter_guessed)
        result = check_win(secret_word, old_letters_guessed)
        if result is True:
            return True
        else:
            return False
    else:
        old_letters_guessed.append(letter_guessed)



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
    #print(hang_photos(3))
    f_path = input('Please enter file path: ')
    word_num = input('Please enter a num: ')
    secret_word = choose_word(f_path, word_num)
    #print(secret_word)
    #print(r'\n\n Let's Start!\n')
    print(hang_photos(1))
    print('_' * len(secret_word))
    old_letters_guessed = []
    num_of_tries = 0
    while num_of_tries <= MAX_TRIES:
        letter_guessed = input('Please guess a letter: ')
        result = try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word)
        #if result =


        num_of_tries += 1










if __name__ == "__main__":
    main()