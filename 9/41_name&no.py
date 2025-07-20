name = input('enter name')
num = int(input('enter number below 10:'))

if num <= 10:
    for i in range(1,num+1):
        print(name)
elif num < 1:
    print('no is too small')
else:
    for i in range(3):
        print('no is too big')

