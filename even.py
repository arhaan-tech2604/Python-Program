def show(num):
    if num%2==0:
        return"Even"
    else:
        return"odd"
    
lst=[1,2,3,4,5]
m=map(show , lst)
print(list(m))