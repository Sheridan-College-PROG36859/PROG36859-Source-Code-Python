from dataclasses import dataclass, field
import pickle

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
def write_simple_data() :
    # file = open(r"C:\Users\William Barry\ExampleFile.txt", "w")
    # file = open("C:\\Users\\William Barry\\ExampleFile.txt", "w")
    # file = open("C:/Users/William Barry/ExampleFile.txt", "w")
    file = open("./Files/ExampleFile.txt", "w")
    file.write("Hello World\n")
    file.write("This is a file we are writing too" + '\n')
    value = input('Enter a value: ')
    file.write(str(value) + '\n')
    file.write(str(value) + '\n')
    file.close()
    pass

# Read Data
def read_simple_data() :
    file = open("./Files/ExampleFile.txt", "r")
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
    with open("./Files/ExampleFile.txt", "w") as file :
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
    with open("./Files/ExampleFile.txt", "r") as file :
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
    with open("./Files/Records.txt", "w") as file :
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
    with open("./Files/Records.txt", "r") as file :
        num_accounts = int(file.readline().rstrip())
        for i in range(num_accounts) :
            record = file.readline().rstrip()
            data = record.split(';')
            print(data)
            print(f'{data[1]} has an id of {data[0]} and is {data[2]} old')
            pass
        pass
    pass

# Random File Access
def Random_File_Access() :
    with open("./Files/RandomFile.txt", "rb") as file:
        print("Tell: " + str(file.tell()))
        value = float(file.read(4))
        print(value)
        print("Tell: " + str(file.tell()))
        print(file.read(10).decode())
        print("Tell: " + str(file.tell()))

        file.seek(2, 1)
        print("Tell: " + str(file.tell()))
        print(file.read(5).decode())
        print("Tell: " + str(file.tell()))

        file.seek(-5, 1)
        print("Tell: " + str(file.tell()))
        print(file.read(5).decode())
        print("Tell: " + str(file.tell()))

        file.seek(0, 0)
        print(file.read(5).decode())

        file.seek(-10, 2)
        print(file.read())

        pass
    pass    

# Write/Read binary and with pickle
def Binary_Pickle_Files() :

    with open("./Files/binary.dat", "wb") as file:
        file.write(str.encode("Hello"))
        file.write(int(10).to_bytes(4))
        pass

    with open("./Files/binary.dat", "rb") as file :
        string = file.read(5).decode()
        print(string)
        int_bytes = file.read(4)
        print(int.from_bytes(int_bytes))
        pass

    with open("./Files/pickle.data", "wb") as file:
        # pickle.dump(10, file)
        user = UserAccount(0, "Bob")
        print(user)
        pickle.dump(user, file)
        pass

    with open("./Files/pickle.data", "rb") as file:
        # value = pickle.load(file)
        # print(value)
        user = pickle.load(file)
        print(user)
        pass

    pass

if __name__ == "__main__" :
    # write_simple_data()
    # read_simple_data()
    # Write_UserAccount()
    # Read_UserAccount()
    # Write_UserAccount_as_records()
    # Read_UserAccount_as_records()
    # Random_File_Access() 
    Binary_Pickle_Files()
    pass