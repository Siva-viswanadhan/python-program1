
total = 0
for i in range(5):
    include = input('enter include or not')
    num = int(input('enter number'))
    if include == 'include':
        total += num
print('total =', total)
