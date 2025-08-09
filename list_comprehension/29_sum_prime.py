def sum_prime():
    return [(i,j) for i in range(1,11)
                  for j in range(1,11)
                   if all((i+j)%n !=0 for n in range(2,int((i+j)**0.5)+1)) ]

print(sum_prime())