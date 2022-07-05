def who_is_missing(file_name):

    f = open(file_name, 'r')
    f_str = f.read()
    lst = []
    for n in f_str:
        if n.isdigit():
            lst.append(n)
        else:
            pass
    f.close()
    lst.sort()
    n = int(lst[0])
    if len(lst) == 1:
        n -= 1
        file_path = ("C:\campus\\found.txt")
        fw = open(file_path, 'w')
        fw.write(str(n))
        return n
    else:
        for num in range(1, len(lst)):
            if int(lst[num]) - int(n) == 1:
                n = lst[num]
                num += 1
            else:
                number = int(lst[num]) - 1
                file_path = ("C:\campus\\found.txt")
                fw = open(file_path, 'w')
                fw.write(str(number))
                fw.close()
                return number








print(who_is_missing("C:\campus\\findMe.txt"))