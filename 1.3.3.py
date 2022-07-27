def is_funny(string):

    return False not in [False if char != 'h' and char != 'a' else True for char in string]





print(is_funny("hahahahahaha"))
