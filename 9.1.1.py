def are_files_equal(file1, file2):

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')
    rf1 = f1.read()
    rf2 = f2.read()
    if rf1 == rf2:
        return True
    else:
        return False







print(are_files_equal(r"c:\vacation.txt", "c:\work.txt"))