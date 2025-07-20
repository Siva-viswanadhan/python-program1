#Write a Python program to find the intersection of two sets


def intersection(list1,list2):
    return list(set(list1).intersection(set(list2)))



print(intersection([1,2,3],[1,5,2]))