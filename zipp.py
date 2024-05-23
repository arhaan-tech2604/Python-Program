d1={'a':1,'b':3}
d2={'c':6,'d':9}

print(list(zip(d1,d1.values())))

a=list(zip(d1,d2))
b,c=zip(*a)
print(b)
print(c)
