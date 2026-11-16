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

# Read Data

# Write UserAccount

# Read UserAccount

# Write UserAccount as records

# Read UserAccount as records

# Random File Access

# Write/Read with pickle

if __name__ == "__main__" :
    pass