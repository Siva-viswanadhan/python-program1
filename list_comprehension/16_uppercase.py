def upper_case(str):
    lst = [i.upper() for i in str.split()]
    return lst

print(upper_case('apple is a fruit'))