num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
total = num1 + num2
print('total = ',total)
yes_or_no = input("Do you want to add, if yes enter y? ")

# while yes_or_no in  ('y' or 'Y'):
while yes_or_no =='y' or yes_or_no ==  'Y':
    num = int(input("Enter a number: "))
    total += num
    print('total = ',total)
    yes_or_no = input("Do you want to add, if yes enter y? ")
print('total = ',total)