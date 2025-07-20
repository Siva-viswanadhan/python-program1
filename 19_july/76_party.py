#Ask the user to enter the names of three people they want to invite to a
# party and store them in a list. After they have entered all three names,
# ask them if they want to add another. If they do, allow them to add more names until they answer "no".
# When they answer "no", display how many people they have invited to the party.

def party():
    lst =[]
    for i in range(3):
        name = input('enter  name: ')
        lst.append(name)

    while True:
        invite = input('enter invite (yes/no): ').strip().lower()
        if invite == 'yes':
            name2 = input('enter name to invite: ')
            lst.append(name2)
        elif invite == 'no':
            break
        else:
            print('enter yes/no')

        print('no of person invited',len(lst))
        print('invited list',lst)

party()