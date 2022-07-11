def check_win(secret_word, old_letters_guessed):

    answer = True
    for n in secret_word:

        if n in old_letters_guessed:
            answer = True
        else:
            answer = False
            return answer
    return answer



secret_word = "plant"
old_letters_guessed = ['p', 'm', 'p', 'j', 'i', 's', 'k', 'n', 'f', 'e', 'r', 'd', 'y']
print(check_win(secret_word, old_letters_guessed))