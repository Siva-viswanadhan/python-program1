#Generate a list of prime numbers from 1 to 50
def prime():
    lst = [i for i in range(2,100) if all (i%n !=0 for n in range(2,int(i**0.5)+1))]
    return lst


print(prime())