#Create a list of two sports, Ask the user what their favourite sport is and add this to the end of the list. Sort the list and display it.


def sports(lst,user_input):
    lst.append(user_input)
    print(lst)
    lst.sort()
    print(lst)


lst =['tennis','cricket']
user_input =input('enter you favourite sport: ')
sports(lst,user_input)