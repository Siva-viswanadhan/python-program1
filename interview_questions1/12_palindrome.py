#Write a Python code to check if a string is a palindrome

def palindrome(str):
    if str == str[::-1]:
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')



str = input('Enter a string: ')
palindrome(str)