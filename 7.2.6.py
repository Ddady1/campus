def bucket_list(gro_list):
    print(' 1. Print list. \n 2. Print number of list items. \n 3. Print if item in list. \n 4. Print how many times items in list \n '
          '5. Delete item from list. \n 6. Add item to list. \n 7. Print illigal item. \n 8. Remove duplicates. \n 9. Exit')


    x = int(input('Please Select a number: '))
    while x != 0:
        if x == 1:
            print(gro_list)
            bucket_list(gro_list)
        elif x == 2:
            print(len(gro_list))
            bucket_list(gro_list)
        elif x == 3:
            item = input('Please enter an item: ')
            if item in gro_list:
                print(True)
            else:
                print(False)
            bucket_list(gro_list)
        elif x == 4:
            item = input('Please enter an item: ')
            print(f'You have {gro_list.count(item)} of {item}')
            bucket_list(gro_list)
        elif x == 5:
            item = input('Please enter an item: ')
            num = gro_list.index(item)
            gro_list.pop(num)
            bucket_list(gro_list)
        elif x == 6:
            item = input('Please enter an item: ')
            gro_list.append(item)
            bucket_list(gro_list)



grocery_list = 'Milk,Cottage,Tomatoes'
bucket_list(list(grocery_list.split(',')))