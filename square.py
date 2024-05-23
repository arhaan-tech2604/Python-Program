def generator():
    n=1
    
    while n<=10:
        sqr=n*n
        yield sqr
        n+=1

o=generator()
print(next(o)) 
print(next(o))

for j in o:
    print(j)
        