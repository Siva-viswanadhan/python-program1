num = int(input("enter number between 10 and 20"))

while num not in range (10,21):
    if num < 10:
        print('too low')
        num = int(input("try again"))
    elif num > 20:
        print('too high')
        num = int(input("try again"))
print('thank you')