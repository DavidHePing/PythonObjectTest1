class TestObject1:
    def __init__(self, parm1 = 1, parm2 = 2):
        self.prop1 = parm1
        self.prop2 = parm2

a = TestObject1()
print(a.prop1, a.prop2)
b = TestObject1(20, 30)
print(b.prop1, b.prop2)
