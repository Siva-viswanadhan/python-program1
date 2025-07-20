compnum = 50
count = 1
guess = int(input("Guess the number"))

while guess != compnum:
    if guess > compnum:
        print('too high')
        count += 1
        guess = int(input("Guess the number"))
    elif guess < compnum:
        print('too low')
        count += 1
        guess = int(input("Guess the number"))
print('you guessed correctly',count,'times')