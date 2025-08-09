def length(lst):
    lst1 = [(i,len(i)) for i in lst]
    return lst1

lst = ['apple', 'banana', 'cherry']
print(length(lst))