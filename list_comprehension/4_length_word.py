def length_word(str1):
    lst = str1.split()
    lst1 = [len(i) for i in lst]
    return lst1

print(length_word('It sure is not too cold'))