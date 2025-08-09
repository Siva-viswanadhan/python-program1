#Generate a list of tuples containing two numbers whose sum is even

def sum_even():
    return [(i,j) for i in range(1,11) for j in range(1,11) if (i+j) %2 == 0]

print(sum_even())