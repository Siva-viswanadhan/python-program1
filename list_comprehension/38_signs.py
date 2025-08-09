def signs(lst):
    return [(i,'negative') if i < 0 else (i,'positive') if i > 0 else (i,'zero') for i in lst]


print(signs([1,2,0,4,-5,6,7,8,-9]))