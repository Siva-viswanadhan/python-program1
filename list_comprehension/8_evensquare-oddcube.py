def square_cube():
    lst = [i**2 if i%2==0 else i**3 for i in range(1,11)]
    return lst
print(square_cube())