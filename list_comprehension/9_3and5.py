def multiple_3and5():
    lst = [i for i in range(100) if i % 3==0 and i%5==0]
    return lst

print(multiple_3and5())
