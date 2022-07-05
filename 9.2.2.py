def copy_file_content(source, destination):

    s_file = open(source, 'r')
    s_con = s_file.read()

    d_file = open(destination, 'w')
    d_file.write(s_con)






copy_file_content("C:\campus\copy.txt", "C:\campus\paste.txt")