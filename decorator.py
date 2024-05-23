def make(func):
    def inner():
        print("I am Decorator")
        func()
    return inner

def order():
    print("I am Ordinary")
    
dec=make(order)
dec()    