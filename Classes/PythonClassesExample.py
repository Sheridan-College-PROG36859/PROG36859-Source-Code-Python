from Student import Student

def main() :
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

if __name__ == "__main__" :
    main()