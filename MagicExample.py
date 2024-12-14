class NewDiv:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        return NewDiv(self.value + other.value)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value > 0:
            self.value //= 2
            return self.value
        raise StopIteration
    
    def __len__(self):
        return 1
    
a = NewDiv(256)
b = NewDiv(450)

print(a)
print(b + ((a + b) + a))
for el in a:
    print(el)
print(len([1, 2, 3]))
print(len(a))