f_path = input('Please enter file path: ')
f_action = input('Please enter the action: sort, rev or last: ')

with open(f_path, 'r') as f:
    content = f.read()
    if f_action == 'sort':
        con_lst = content.split(' ')
        new_lst = []
        for n in con_lst:
            if n in new_lst:
                pass
            else:
                new_lst.append(n)
        print(new_lst.sort())