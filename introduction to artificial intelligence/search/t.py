class A:
    def __init__(self, a):
        self.a = a
        self.a[len(a)//2] = 'A'

class B(A):
    def __init__(self, a):
        super().__init__(a)
        self.a[0] = 'B'
class C(A):
    def __init__(self, a):
        super().__init__(a)
        self.a[-1] = 'C'
