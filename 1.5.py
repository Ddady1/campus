with open('names.txt', 'r') as f:
    print(max(f.readlines()))

with open('names.txt', 'r') as f:
    print(len(f.read()))