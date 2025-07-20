#Write a Python code to count the number of uppercase letters in a string

def count_uppercase(str):
    count = 0
    for i in str:
        if i.isupper():
            count+= 1
    return count


print(count_uppercase('My nAme iS m'))