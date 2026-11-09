
class A :
    def __init__(self):
        print("A")
        pass

    def PrintClassName(self) :
        print(A)
        pass

    def A_Method(self) :
        print("Method A")
        pass

class B :
    def __init__(self):
        print(B)
        pass

    def PrintClassName(self) :
        print("Method A")
        pass

    def B_Method(self) :
        print("Method B")
        pass

# C will derive from A and B
# Doing this, python will use MRO (Method Resolution Order) when attempting
# to invoke the method when using super() searching from left to right for
# the base classes (A then B)
class C(A, B) :
    def __init__(self):
        # we use super to invoke the parent class (A) in this example
        super().__init__()
        print("C")
        pass

    def Method(self) :
        # super uses A
        super().PrintClassName()
        # We can invoke the A.PrintClassName specifically
        A.PrintClassName(self)
        # We can invoke the B.PrintClassName specifically
        B.PrintClassName(self)
        
        # We can invoke base class method using MRO calling super().___
        # this will search A class first then if not found B class and is
        # why we can do the second call for B_Method
        super().A_Method()
        super().B_Method()

        print("Method C")
        pass

c = C()
c.Method()