
class Student :

    __id = 0

    @classmethod
    def get_next_id(cls):
        return cls.__id

    # add name and age as parameters and set them as attributes
    def __init__(self, name, age = 0, grades = None, id = None):
        self.name = name
        self.age = age
        if not isinstance(grades, list) :
            raise TypeError("Error grades is not a list")
        if not all (type(item) is float for item in grades) :
            raise TypeError("All items in grades must be floats")
        self.grades = grades
        if id == None :
            self.__id = Student.__id
            Student.__id += 1
        else :
            self.__id = id

    #write a method called display that returns a string like below
    def display(self) :
        return f"Student {self.name}:{self.__id} is {self.age} old has grades {self.grades}"

    def set_phone_number(self, phone_number) :
        self._phone_number = phone_number

    def get_phone_number(self) :
        if hasattr(self, "_phone_number") :
            return self._phone_number
        return "(XXX)XXX-XXXX"

    #write a getter for the instance id
    def get_id(self) :
        return self.__id 


s1 = Student("Bob", 20, [70.5, 34.5, 55.8, 90.8])
s2 = Student("Fred", 22, [90.2, 40.9, 50.8, 20.8])

print(s1.display())
print(s2.display())

print(f"Next id: {Student.get_next_id()}")

s1.set_phone_number("(905)555-1234")
print(s1.get_phone_number())
print(s1._phone_number)
print(s2.get_phone_number())