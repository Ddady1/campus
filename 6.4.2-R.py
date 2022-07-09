def try_update_letter_guessed(letter_guessed, old_letters_guessed):
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
        return False
    elif len(letter_guessed) >= 2 or not letter_guessed.isalpha():
        print('X')
        print(' -> '.join(old_letters_guessed))
        return False
    else:
        old_letters_guessed.append(letter_guessed)
        return True