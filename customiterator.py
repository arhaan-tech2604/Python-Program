class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            current_value = self.data[self.index]
            self.index += 1
            return current_value
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
my_iterator = CustomIterator(my_list)
for item in my_iterator:
    print(item)