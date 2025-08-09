#Create a list of first characters from a list of words
def first_letter(lst):
    lst1 = [i[0] for i in lst]
    return lst1


lst = ['apple', 'banana', 'cherry']
print(first_letter(lst))