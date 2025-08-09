def odd_even():
    return [(i,i+1) for i in range(1,11) if i%2!=0]

print(odd_even())