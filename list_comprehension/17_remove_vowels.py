#Generate a list of strings with vowels removed

def remove_vowels(s):
    lst = s.split()
    lst1 = [''.join([ch for ch in word if ch.lower() not in ['a', 'e', 'i', 'o', 'u']]) for word in lst]
    return lst1

print(remove_vowels('apple is a fruit'))
