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

# Random File Access
def Random_File_Access() :
    print("\n----------- Random_File_Access -----------")
    with open("./Files-Binary/RandomFile.txt", "rb") as file:
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

    print("\n----------- Binary_Pickle_Files - Binary -----------")
    
    with open("./Files-Binary/binary.dat", "wb") as file:
        file.write(str.encode("Hello"))
        file.write(int(10).to_bytes(4))
        pass

    with open("./Files-Binary/binary.dat", "rb") as file :
        string = file.read(5).decode()
        print(string)
        int_bytes = file.read(4)
        print(int.from_bytes(int_bytes))
        pass

    print("\n----------- Binary_Pickle_Files - Pickle -----------")

    with open("./Files-Binary/pickle.data", "wb") as file:
        # pickle.dump(10, file)
        user = UserAccount(0, "Bob")
        print(user)
        pickle.dump(user, file)
        pass

    with open("./Files-Binary/pickle.data", "rb") as file:
        # value = pickle.load(file)
        # print(value)
        user = pickle.load(file)
        print(user)
        pass

    pass

if __name__ == "__main__" :
    Random_File_Access() 
    Binary_Pickle_Files()
    pass