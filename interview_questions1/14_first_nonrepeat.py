#Write a Python code to find the first non-repeating character in a string


def non_repeating(lst):

    for i in lst:
        if lst.count(i) == 1:
            return i
    return None # if all characters repeat


print(non_repeating('my name is m'))