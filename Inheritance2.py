class A:
    def foo(self):
        print('A')

class B:
    def foo(self):
        print('B')

class D(A, B):
    def foo(self):
        print('D')

class C(B, A):
    def foo(self):
        print('C')

class MetaMRO(type):
    def mro(cls):
        return (A, cls, B, D, C, object)
    
class E(D, C, metaclass=MetaMRO):
    def foo(self):
        print('E')

E().foo()