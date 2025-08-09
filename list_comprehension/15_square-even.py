#Generate a list of numbers with their squares if the number is even

def even_square():
    lst1 = [i**2 for i in range(1, 11) if i%2==0]
    return lst1

print(even_square())