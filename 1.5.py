'''with open('names.txt', 'r') as f:
    print(max(f.readlines()))'''

with open('names.txt', 'r') as f:
    #print(sum(f.readlines()))
    print(sum([len(i) - 1 for i in f.readlines()]))