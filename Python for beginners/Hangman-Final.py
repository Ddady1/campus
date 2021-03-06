def hang_photos(photo_num):

    '''Function that return a string ad pic according to a number
    :param photo_num: number of the photo
    :type photo_num: int
    :return: string
    :rtype: str'''

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
    :param index: the index value of the word
    :type file_path: str
    :type index: int
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

def is_valid_input(letter_guessed):

    '''Function check if letter is under approved conditions
    :param letter_guessed: value of guessed letter
    :type letter_guessed: str
    :return: Treu or False
    :rtype: bool'''

    if len(letter_guessed) >= 2 or not letter_guessed.isalpha():
        return False
    else:
        return True

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

    ''' Function that prints the welcome screen
    :param nothing:Null
    :type nothing:Null
    :return: Welcome screen
    :rtype: str'''

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
    print(hangma_main_pic(), '  You have', MAX_TRIES, 'tries')
    f_path = input('Please enter file path: ')
    word_num = input('Please enter a num: ')
    secret_word = choose_word(f_path, int(word_num))
    print("""\nLet's Start!\n\n""", hang_photos(1))
    print('_' * len(secret_word))
    old_letters_guessed = []
    num_of_tries = 0
    while num_of_tries < MAX_TRIES:
        if_good = False
        while if_good != True:
            letter_guessed = input('Please guess a letter: ')
            if_good = is_valid_input(letter_guessed)
            if if_good is True:
                continue
            else:
                print('X')
                print(' -> '.join(old_letters_guessed))
        result = try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word)
        if result == 'Win':
            print(secret_word)
            print('WIN')
            exit()
        elif result == 'no_good' :
            continue
        elif result == 'no_end':
            print(show_hidden_word(secret_word, old_letters_guessed))
            continue
        elif result == 'False':
            num_of_tries += 1
            print(')-:  Wrong, no such letter!')
            print(f'You have left {6-num_of_tries} tries')
            print(hang_photos(num_of_tries + 1))
    print('LOSE')
    exit()


if __name__ == "__main__":
    main()