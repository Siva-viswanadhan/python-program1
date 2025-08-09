#Generate a list of numbers with their signs reversed
def change_sign(lst):
    lst1 = [-(i) for i in lst]
    return lst1

lst = [-2, 3, -5, 7, -11]

print(change_sign(lst))