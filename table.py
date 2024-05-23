def table():
    n = 1
    while True:
        yield 5 * n
        n += 1

generator = table()
for i in range(10):  
    print(next(generator))