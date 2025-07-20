num = int(input('enter no between 1 to 12:'))

if num <= 1 or num >= 12:
    print('not between 1 and 12')
else:
    for i in range(1,11):
        print(i,'*',num,'=',num*i)
