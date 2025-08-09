def ascii_values(str):
    words = str.split()
    return [(i,ord(i)) for i in str if i !=' ']


print(ascii_values('This is a sample sentence'))