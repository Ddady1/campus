password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"


print(''.join([chr(ord(char) + 2) for char in password if char.isalpha()]))
#print(''.join(([chr(ord(char) + 2) if char.isalpha else char.replace(':', '') for char in password])))

''' k - > m
    o - > q
    e - > g'''