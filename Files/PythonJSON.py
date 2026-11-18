# use the monsters.csv
import json
from dataclasses import dataclass, asdict
from json import JSONDecodeError, JSONEncoder

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

# Convert json str to dict and access keys

# Save a monster to a file via JSON

# Load a monster from a file

# Save a monster by using the dataclass asdict to convert the monster to a json string

# Load a monster by using the json string and the **kwards (keyword arguments)
