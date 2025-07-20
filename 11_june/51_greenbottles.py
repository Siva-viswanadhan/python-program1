left = 10

while left > 0:
    print(f'there are {left} green bottles hanging on the wall')
    num = int(input("if one fall how many left:"))
    while num != left - 1:
        num = int(input("try again"))

    left -= 1
    print('correct')
print('there are no more green bottles left')

