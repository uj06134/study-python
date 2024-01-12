class A:
    @classmethod
    def __new__(cls, *args, **kwargs):
        print('__new__')
        obj = super().__new__(cls)
        return obj

    def __init__(self, data1, data2, name=''):
        print('__init__')
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name

    # def print_name(self, name):
    #     print(name)

    def print_name(self):
        print(self.name)

# a = A()
a = A(10, 20, 'a')
print(a)
# a.data1 = 10
# a.data2 = 20
print(a.data1, a.data2)
# a.print_name('a')
a.print_name()

# b = A()
b = A(100, 200, 'b')
print(b)
# b.data1 = 100
# b.data2 = 200
print(b.data1, b.data2)
# b.print_name('b')
b.print_name()