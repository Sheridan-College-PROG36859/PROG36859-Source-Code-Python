from abc import ABC, abstractmethod

# To make Tossable an abstract class we derive crom ABC
# and which allows us to make toss an abstract method
# any class that derives from Tossable will need to 
# implement the toss method
class Tossable(ABC) :

    @abstractmethod
    def toss(self) :
        pass

# Ball derives from Tossable and abstract class
# and is abstract itself implemening the bounce
# method as abstract
class Ball(Tossable, ABC) :
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self) -> str :
        return self.name

    # We comment this out because a ball itself does not know
    # how to toss, the derived classes should do this
    # def toss(self) :
    #     pass

    # Again, a ball does not know how to bounce, the derived
    # classes should know this
    @abstractmethod
    def bounce(self) :
        pass

    # A few MAGIC methods __MAGIC__ implemented below

    # Equals
    # here we compare name and weight
    def __eq__(self, value):
        if not isinstance(value, Ball) :
            return NotImplemented
        return self.weight == value.weight and self.name == value.name

    # Returns a string for print
    def __str__(self):
        return f'Name of the ball: {self.name} weighs {self.weight}'

    # Greater than or Equal
    # here we compare weight
    def __ge__(self, other) :
        return self.weight >= other.weight 

    # Less than 
    # We write the Less than so we can call sort on a list
    def __lt__(self, other):
        return self.weight > other.weight 

    # Represents something more code like
    def __repr__(self):
        return "{\"name\":" + self.name + "}"

class Baseball(Ball) :

    # We implement the __init__ and call the base class by using
    # super().__init__
    def __init__(self, name, weight):
        super().__init__(name, weight)
        pass

    # implement the base class (Tossable) abstract method
    def toss(self) :
        print("Throw forward")
        pass

    # bounce is abstract in Ball so we must also implement it
    def bounce(self) :
        print("Up and Down")
        pass

    def __str__(self):
        return super().__str__()

# Similar to Baseball just different output
class Rugbyball(Ball) :

    def __init__(self, name, weight):
        super().__init__(name, weight)
        pass

    def toss(self) :
        print("Pass backwards")
        pass

    def bounce(self) :
        print("All over the place")
        pass

    def __str__(self):
        return super().__str__()

# Rock only extends from Tossable and only needs to implement the
# toss method. Note we don't use __init__ here. If we wanted to
# do something with it we can
class Rock(Tossable) :

    def toss(self) :
        print("We skip it")
        pass

# Cannot do this because it is abstract and does not know how to toss
# t = Tossable()

# Ball is generic can cannot be created because it does not know how to toss
# b = Ball("Unknown")

bb = Baseball("Rawlings", 1)
rb = Rugbyball("Glibert", 2)
r = Rock()

# print(b.get_name()) # b is not a valid object
print(bb.get_name())
print(rb.get_name())

# b.toss() # b is not a valid object
bb.toss()
rb.toss()
r.toss()

bb1 = Baseball("Rawlings", 4)
bb2 = Baseball("Rawlings", 3)

print(bb1 == bb2) # compares the name and weight
print(bb1 >= bb2) # compares just the weight

# a list of balls
balls = [bb1, bb, rb, bb2]
balls.sort()

# To get the __str__ to output we need to iterate each
print([str(ball) for ball in balls])

# This will use the __repr__ method. We could also write
# the __repr__ to call self.__str__() if we wanted the
# __repr__ to output the same as __str__
print(balls) 