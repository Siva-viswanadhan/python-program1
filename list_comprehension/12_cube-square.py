#Create a list of squares of even numbers and cubes of odd numbers from -5 to 5

def square_cube():
    lst = [i**2 if i%2==0 else i**3 for i in range(-5,10)]
    return lst
print(square_cube())