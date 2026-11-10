
class Student :

    # These are static attributs which means these are shared variables across all students
    # we have used the __ to lable the attributes as private
    __id = 0
    __students = []

    # Although static, this is also considered a CONST variable because we use capatial letters
    COLLEGE_NAME = "Sheridan"

    # A Class method that can access the private static variables
    @classmethod
    def get_next_id(cls):
        return cls.__id

    # A static  method that can access the private static variables
    @staticmethod
    def get_students() :
        return Student.__students

    # add name and age as parameters and set them as attributes
    def __init__(self, name, age = 0, grades = None, id = None):
        Student.__students.append(self)
        self.name = name
        self.age = age
        if grades != None:
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

    # We can create attrivutes on the fly, here we create a protected by using the _
    # phone_number, the object will only have this attribute if this method is called
    def set_phone_number(self, phone_number) :
        self._phone_number = phone_number

    # because we cannot gurantee a _phone_number exists we must check (this is because we
    # only create _phone__number if the set_phone_number method is called)
    def get_phone_number(self) :
        if hasattr(self, "_phone_number") :
            return self._phone_number
        return "(XXX)XXX-XXXX"

    #write a getter for the instance id
    def get_id(self) :
        return self.__id 

    # Magic method __str__ to return a readble string for the Student
    def __str__(self):
        return f'Student: {self.name} is {self.age} old'


if __name__ == "__main__":
    s1 = Student("Bob", 20, [70.5, 34.5, 55.8, 90.8])
    s2 = Student("Fred", 22, [90.2, 40.9, 50.8, 20.8])

    print(s1.display())
    print(s2.display())

    print(f"Next id: {Student.get_next_id()}")

    s1.set_phone_number("(905)555-1234")
    print(s1.get_phone_number())
    print(s1._phone_number)
    print(s2.get_phone_number())

    print(Student.get_students())