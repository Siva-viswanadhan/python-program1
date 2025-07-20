def flatten(lst):
    flat =[]
    for i in lst:
        if isinstance(i,list):
            flat.extend(flatten(i))
        else:
            flat.append(i)

    return flat



print(flatten([[1,2,3],[4,5,6],7,8,9]))
