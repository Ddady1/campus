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




secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))