#Create a list of four three-digit numbers. Display the list to the user,
# showing each item from the list on a separate line.
# Ask the user to enter a three-digit number, If the number they have typed in matches one in the list,
# display the position of that number in the list, otherwise display the message "That is not in the list".

def three_digit(lst,element):
    for num in lst:
        print(num)
    for num in lst:
        if num == element:
            print('element found at',lst.index(num))
            break
    else:
        print('element not found')


lst =[123,234,124,235,768]
print(lst)
element = int(input('enter element : '))
three_digit(lst,element)