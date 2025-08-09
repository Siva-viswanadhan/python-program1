import string
def not_alphanumeric(str):
    return [i for i in str if i in string.punctuation]

print(not_alphanumeric('banana,is a fruit ;'))