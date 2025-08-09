#Create a list of reversed strings from another list

def reversed_strings(lst):
    lst1 = [i[::-1] for i in lst]
    return lst1

lst = ['elppa', 'ananab', 'yrrehc']
print(reversed_strings(lst))