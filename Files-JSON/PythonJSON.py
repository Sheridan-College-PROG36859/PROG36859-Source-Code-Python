# use the monsters.csv
import json
from dataclasses import dataclass, asdict

@dataclass
class Monster :
    id : int
    name : str
    maxHealth : int
    scariness : float
    pass

# monsters_json = '''{
#                         "id":0,
#                         "name":"Bob",
#                         "maxHealth":100,
#                         "scariness":10.0
#                    }'''

# monsters_json = '''[
#                      {
#                         "id":0,
#                         "name":"Bob",
#                         "maxHealth":100,
#                         "scariness":10.0
#                     },
#                     {
#                         "id":0,
#                         "name":"Fred",
#                         "maxHealth":100,
#                         "scariness":10.0
#                     }
#                 ]'''

# monsters_dict = [
#                      {
#                         "id":0,
#                         "name":"Bob",
#                         "maxHealth":100,
#                         "scariness":10.0
#                     },
#                     {
#                         "id":0,
#                         "name":"Fred",
#                         "maxHealth":100,
#                         "scariness":10.0
#                     }
#                 ]

single_monster_json = '''{"id":0,"name":"Bob","maxHealth":100,"scariness":10.0}'''
single_monster_dict = {"id":0,"name":"Bob","maxHealth":100,"scariness":10.0}
single_monster_obj = Monster(0, "Bob", 100, 10.0)

monsters_json = '''[{"id":0,"name":"Bob","maxHealth":100,"scariness":10.0},{"id":0,"name":"Fred","maxHealth":100,"scariness":10.0}]'''
monsters_dict = [{"id":0,"name":"Bob","maxHealth":100,"scariness":10.0},{"id":0,"name":"Fred","maxHealth":100,"scariness":10.0}]
monsters_list = [Monster(0, "Bob", 100, 10.0), Monster(0, "Fred", 100, 10.0)]

# Convert the dict to json
print("\n----------- Convert the dict to json string -----------")
json_str = json.dumps(single_monster_dict)
print(json_str)

# Convert json str to dict and access keys
print("\n----------- Convert json str to dict and access keys -----------")
json_dict = json.loads(single_monster_json)
print(json_dict)

# Save a monster to a file via JSON
print("\n----------- Save a monster json str to a file via JSON -----------")
with open("./Files-JSON/monster_from_json.json", "w") as file :
    json.dump(single_monster_json, file, indent=4)
    pass

# Load a monster from a file
print("\n----------- Load a monster from a file -----------")
with open("./Files-JSON/monster_from_json.json", "r") as file :
    json_str = json.load(file)
    json_dict = json.loads(json_str)
    print(json_str)
    pass

# Save a monster by using the dataclass asdict to make a dict which json can save as a string
print("\n----------- Save a monster by using the dataclass asdict to make a dict which json can save as a string -----------")
with open("./Files-JSON/monster_from_obj.json", "w") as file :
    json_data = asdict(single_monster_obj)
    json.dump(json_data, file, indent=4)
    pass

# Load a monster by using the json string and the **kwards (keyword arguments)
print("\n----------- Load a monster by using the json string and the **kwards (keyword arguments) with a dataclass -----------")
with open("./Files-JSON/monster_from_obj.json", "r") as file :
    json_data = json.load(file)
    m = Monster(**json_data)
    print(m)
    pass
