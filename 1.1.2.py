def duplicate (num):
    #print(num)
    return num * 2

def double_letter(my_str):
    #print(my_str)
    return ''.join(list(map(duplicate, my_str)))





print(double_letter("python"))

print(double_letter("we are the champions!"))