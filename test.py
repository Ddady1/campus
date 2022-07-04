count = 0
print("Using readlines()")

with open("C:\campus\sampleFile.txt") as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))