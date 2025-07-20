def vowel_count(string):
    vowel ='aeiouAEIOU'
    count = 0


    for i in string:
        if i in vowel:
            count += 1
    return count


string = input('enter a string')
print(vowel_count(string))