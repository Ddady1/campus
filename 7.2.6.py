def bucket_list(gro_list):
    print(' 1. Print list. \n 2. Print number of list items. \n 3. Print if item in list. \n 4. Print how many times items in list \n '
          '5. Delete item from list. \n 6. Add item to list. \n 7. Print illigal item. \n 8. Remove duplicates. \n 9. Exit')


    x = int(input('Please NETER a number: '))
    while x != 0:
        if x == 1:
            print(gro_list)
            bucket_list(gro_list)
        '''elif x == 2:
            print(len(new_list))
            bucket_list(new_list)
        elif x == 3:
            item = input('Please enter item: ')
            if item in new_list:
                print(True)
            else:
                print(False)
            bucket_list(new_list)
        elif x == 4:
            item = input('Please enter item: ')
            print(f'You have {new_list.count(item)} of {item}')
            bucket_list(new_list)'''



grocery_list = 'Milk,Cottage,Tomatoes'
bucket_list(list(grocery_list.split(',')))