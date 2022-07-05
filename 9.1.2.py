f_path = input('Please enter file path: ')
f_action = input('Please enter the action: sort, rev or last: ')

with open(f_path, 'r') as f:


    if f_action == 'sort':
        content = f.read()
        content = content.replace('\n', ' ')
        content = content.replace('"', '')
        con_lst = content.split()
        new_lst = []
        for n in con_lst:
            if n in new_lst:
                pass
            else:
                new_lst.append(n)
        new_lst.sort()
        print(new_lst)

    elif f_action == 'rev':
        lines = f.readlines()
        for line in lines:
            lst = line.replace('\n', '')
            print(lst[::-1])

    elif f_action == 'last':
        n = input('Please enter numer of lines: ')
        lines = f.readlines()
        num = len(lines) - int(n)
        for tu in range(num, len(lines)):
            lst = lines[tu].replace('\n', '')
            print(lst)
            tu += 1

