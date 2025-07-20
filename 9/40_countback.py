num = int(input('Enter a number below 50: '))
if num >50:
    print('enter number below 50')
else:
    print('entered no is',num)
    for i in range(50,num-1,-1):
        print(i)