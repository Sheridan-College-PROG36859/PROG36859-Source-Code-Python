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

# def function(id, name, age = 13, password = "password", address) :
#     pass

if __name__ == "__main__":
    user = UserAccount(1, "Bob")
    print(user)
    print(user.password)