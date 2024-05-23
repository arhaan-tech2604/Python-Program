my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)

while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break