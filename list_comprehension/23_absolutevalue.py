#. Create a list of numbers with their absolute values


def absolute_values(lst):
    return [abs(i) for i in lst]

lst = [-1,2,-3,4,-5]
print(absolute_values(lst))


def absolute_values1(lst):
    return [x if x>0 else -x for x in lst]


lst = [-1,2,-3,4,-5]
print(absolute_values1(lst))