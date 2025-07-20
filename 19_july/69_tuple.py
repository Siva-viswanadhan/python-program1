def tup(tup1,user_input):

    print(tup1)

    if user_input in tup1:
        print(tup1.index(user_input))
    else:
        print('not found')


tup1 = ('india', 'usa','israel','russia','uae')
user_input = 'india'
tup(tup1,user_input)