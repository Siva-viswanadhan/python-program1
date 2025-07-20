#Write a Python program to find the longest word in a sentence


def longest_word(str):
    words = str.split()
    largest =max(words,key = len)  # max(iterable,key)
    return largest



str = 'i love coding '
print(longest_word(str))