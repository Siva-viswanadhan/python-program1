#Write a Python code to convert a list of temperatures from Celsius to Fahrenheit


def temperature(celsius):
    return [(i * 9/5)+32 for i in celsius]



print(temperature([100,20,30]))