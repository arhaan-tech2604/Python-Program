def num():
    n=1
    while n<=100:
        yield n
        n+=1

for i in num():
    print(i)