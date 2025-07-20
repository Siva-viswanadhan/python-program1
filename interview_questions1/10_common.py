def common(lst1,lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)

    common = list(lst1.intersection(lst2))
    return common


lst1 = [1,2,3,4,5]
lst2 = [4,7,8,1]
print(common(lst1,lst2))