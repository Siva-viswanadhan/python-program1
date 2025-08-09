#. Generate a list of numbers that are perfect squares from 1 to 100


def perfect_square():
    lst1 = [i*i for i in range(1, 11) if i*i < 101]
    return lst1

print(perfect_square())