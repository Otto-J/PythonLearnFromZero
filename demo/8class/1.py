class MyClass(object):
    i = 123
    def __init__(self,name):
        self.name = name
    
    def f(self):
        return 'hello, '+self.name

c1 = MyClass('bao')

print(c1.i)
print(c1.f())