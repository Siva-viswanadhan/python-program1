rain = input('is raining?')
if rain == 'yes' or rain == 'YES'or rain == 'Yes':
    wind = input('is there wind')
    if wind == 'yes' or wind == 'YES' or wind == 'Yes':
        print('it is too windy for an umbrella')
    else:
        print('take an umbrella')
else:
    print('enjoy your day')