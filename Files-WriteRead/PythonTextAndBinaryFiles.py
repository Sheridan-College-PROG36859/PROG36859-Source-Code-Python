from dataclasses import dataclass, field

@dataclass
class UserAccount :
    id : int
    name : str
    password : str = field(default="12345", repr=False)
    age : int = 13

    def __post_init__(self):
        if self.age < 0 :
            raise ValueError("Age cannot be negative")
        pass
    pass

# Write Data
def Write_simple_data() :
    print("\n----------- Write_simple_data -----------")
    # file = open(r"C:\Users\William Barry\ExampleFile.txt", "w")
    # file = open("C:\\Users\\William Barry\\ExampleFile.txt", "w")
    # file = open("C:/Users/William Barry/ExampleFile.txt", "w")
    file = open("./Files-WriteRead/ExampleFile.txt", "w")
    file.write("Hello World\n")
    file.write("This is a file we are writing too" + '\n')
    value = input('Enter a value: ')
    file.write(str(value) + '\n')
    file.write(str(value) + '\n')
    file.close()
    pass

# Read Data
def Read_simple_data() :
    print("\n----------- Read_simple_data -----------")
    file = open("./Files-WriteRead/ExampleFile.txt", "r")
    # file_data = file.read()
    # print(file_data)

    line = file.readline().rstrip()
    while line != '' :
        print(line)
        line = file.readline().rstrip()
        pass

    file.close()
    pass

# Write UserAccount
def Write_UserAccount() :
    print("\n----------- Write_UserAccount -----------")
    with open("./Files-WriteRead/ExampleFile.txt", "w") as file :
        num_accounts = int(input("How many accounts: "))
        file.write(str(num_accounts) + '\n')
        for i in range(num_accounts) :
            id = int(input("User Id: " ))
            name = input("User name: ")
            file.write(str(id) + '\n')
            file.write(name + '\n')
            pass
        pass
    pass

# Read UserAccount
def Read_UserAccount() :
    print("\n----------- Read_UserAccount -----------")
    with open("./Files-WriteRead/ExampleFile.txt", "r") as file :
        num_accounts = int(file.readline().rstrip())
        for i in range(num_accounts) :
            id = int(file.readline().rstrip())
            name = file.readline().rstrip()
            print(f'{name} has an id of {id}')
            pass
        pass
    pass

# Write UserAccount as records
def Write_UserAccount_as_records() :
    print("\n----------- Write_UserAccount_as_records -----------")
    with open("./Files-WriteRead/Records.txt", "w") as file :
        num_accounts = int(input("How many accounts: "))
        file.write(str(num_accounts) + '\n')
        for i in range(num_accounts) :
            id = int(input("User id: "))
            name = input("User name: ")
            age = int(input("User age: "))
            file.write(f'{id};{name};{age}\n')
            pass
        pass
    pass

# Read UserAccount as records
def Read_UserAccount_as_records() :
    print("\n----------- Read_UserAccount_as_records -----------")
    with open("./Files-WriteRead/Records.txt", "r") as file :
        num_accounts = int(file.readline().rstrip())
        for i in range(num_accounts) :
            record = file.readline().rstrip()
            data = record.split(';')
            print(data)
            print(f'{data[1]} has an id of {data[0]} and is {data[2]} old')
            pass
        pass
    pass

if __name__ == "__main__" :
    Write_simple_data()
    Read_simple_data()
    Write_UserAccount()
    Read_UserAccount()
    Write_UserAccount_as_records()
    Read_UserAccount_as_records()
    pass