#21. Generate a list of positive numbers from another list



def positive_lst(lst):
    lst1 = [i for i in lst if i > 0]
    return lst1


lst = [1,2,-3,4,-2]
print(positive_lst(lst))