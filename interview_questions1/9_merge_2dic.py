def merge(dic1, dic2):
    merge ={**dic1, **dic2}
    return merge

dic1 = {'a':1,'b':2,'c':3,'d':4}
dic2 = {'c':2,'e':3}
print(merge(dic1, dic2))