name = input("Enter your name: ")
print(name,"has now been invited")
count = 1
invite_more = input("Do you want to invite more :y? ")
while invite_more == 'y' or invite_more == 'Y':
    name = input("Enter your name: ")
    print(name,"has now been invited")
    count += 1
    invite_more = input("Do you want to invite more :y? ")
print('total invited =',count)