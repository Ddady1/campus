def check_valid_input(letter_guessed, old_letters_guessed):
    ''' Function check if input is valid.
    :param letter_guessed: guessed letter value
    :param old_letters_guessed: old letters guessed
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: result if input is valid
    :rtype: booelean
    '''

    letter_guessed = letter_guessed.lower()
    if letter_guessed in old_letters_guessed:
        return False
    elif len(letter_guessed) >= 2 or not letter_guessed.isalpha():
        return False
    else:
        return True
