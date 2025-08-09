def length_greater(str):
    return [i for i in str.split() if len(i) > 3]


print(length_greater('This is a sample sentence'))