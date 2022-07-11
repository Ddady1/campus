famous = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}
x = int(input('Please enter a number between 1 and 7: '))
if x == 1:
    print(famous['last_name'])
if x == 2:
    print(famous['birth_date'])
if x == 3:
    print(len(famous['hobbies']))
if x == 4:
    f = len(famous['hobbies'])
    print(famous['hobbies'][f - 1])
if x == 5:
    famous['hobbies'].append('Cooking')
if x == 6:
    date = famous['birth_date'].split('.')
    print(tuple(date))
if x == 7:
    today = 2022 - 1970
    famous['age'] = today
    print(famous['age'])
