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
    |""", 1: '''    x-------x
    ''', 2: """    x-------x
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

    '''function the gets a file and return a word from its content
    :param file_path: file path
    :param index: the index valuse of the word
    :type file_path: str
    :type index: enumerate
    :return: the word chosen
    :rtype: str'''

    with open(file_path, 'r') as word_read:
        content = word_read.read()
        items = content.split(' ')
        return items[int(index) - 1]

def check_win(secret_word, old_letters_guessed):

    '''Function check if user won or lost
    :param secret_word: secret word value
    :param old_letters_guessed: old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: result of checking
    :rtype: bool '''

    answer = True
    for n in secret_word:

        if n in old_letters_guessed:
            answer = True

        else:
            answer = False
            return answer
    return answer

def show_hidden_word(secret_word, old_letters_guessed):

    ''' Function returns secret word only with the found letters
    :param secret_word: secret word value
    :param old_letters_guessed: old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: result string
    :rtype: str'''

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

    ''' Function check if input is valid and tries to update old_letters_guessed. It also prints status and send another function to check
    if the game ends.
    :param letter_guessed: guessed letter value
    :param old_letters_guessed: old letters guessed
    :param secret_word: secret word value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :type secret_word: str
    :return: result if input is valid
    :rtype: str
    '''

    letter_guessed = letter_guessed.lower()
    old_letters_guessed.sort()
    if letter_guessed in old_letters_guessed:
        print('X')
        print(' -> '.join(old_letters_guessed))

        return 'no_good'
    elif len(letter_guessed) >= 2 or not letter_guessed.isalpha():
        print('X')
        print(' -> '.join(old_letters_guessed))
        return 'no_good'

    elif letter_guessed in secret_word:
        old_letters_guessed.append(letter_guessed)
        result = check_win(secret_word, old_letters_guessed)
        if result == True:
            return 'Win'


        else:
            return 'no_end'
    else:
        old_letters_guessed.append(letter_guessed)
        return 'False'

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
    f_path = input('Please enter file path: ')
    word_num = input('Please enter a num: ')
    secret_word = choose_word(f_path, word_num)
    print("""\nLet's Start!\n\n""", hang_photos(1))
    print('_' * len(secret_word))
    old_letters_guessed = []
    num_of_tries = 0
    while num_of_tries < MAX_TRIES:
        letter_guessed = input('Please guess a letter: ')
        result = try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word)
        if result == 'Win':
            print(secret_word)
            print('Win')
            exit()
        elif result == 'no_good' :
            continue
        elif result == 'no_end':
            print(show_hidden_word(secret_word, old_letters_guessed))
            continue
        elif result == 'False':
            num_of_tries += 1
            print(')-:')
            print(hang_photos(num_of_tries + 1))
    print('Lose')
    exit()


if __name__ == "__main__":
    main()