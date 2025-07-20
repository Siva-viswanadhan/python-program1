def tup(tup1,user_input,user_index):

    print(tup1)

    if user_input in tup1:
        print(tup1.index(user_input))
    else:
        print('not found')

    print(tup1[user_index])


tup1 = ('india', 'usa','israel','russia','uae')
user_input = 'india'
user_index =int(input('enter index: '))
tup(tup1,user_input,user_index)