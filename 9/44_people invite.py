no_of_people = int(input('enter number of people: '))

if no_of_people < 10:
    for i in range(no_of_people):
        name = input('enter name of person: ')
        print(name, 'has been invited')

else:
    print('too many people')