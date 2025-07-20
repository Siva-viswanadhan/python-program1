up_down = input('enter up or down ? :')

if up_down == 'up':
    num = int(input('enter top number :'))
    for i in range(1,num+1):
        print(i)
elif up_down == 'down':
    num = int(input('enter a number below 20 :'))
    if num <= 20:
        for i in range(20,num-1,-1):
         print(i)
    else:
        print('enter a valid number')
else:
    print('i dont understand')