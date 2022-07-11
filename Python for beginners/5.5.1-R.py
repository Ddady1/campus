def is_valid_input(letter_guessed):
    if len(letter_guessed) >= 2 or not letter_guessed.isalpha():
        return False
    else:
        return True


is_valid_input(letter_guessed)