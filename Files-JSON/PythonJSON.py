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


filename = "Hello.csv"

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

def WorkingWithListsofDictionaryAndJSON() :
    # convert a json string to a list of monsters because it is many
    many_monsters_list = json.loads(monsters_json)
    # iterate through each monster in the list and access them as dictionary
    for monster_dict in many_monsters_list :
        print(monster_dict) # print the dictionary item
        print(monster_dict["name"]) # print the items name

    # Write a string that has many monsters to a file
    with open("./Files-JSON/many_monster_list_dict.json", "w") as file:
        json.dump(monsters_json, file, indent=4)
        pass

def CreateSaveLoadMonsters() :
    # Create a list of monsters with user names
    count = int(input("How man monsters: "))
    monster_list = []
    for i in range(count) :
        name = input("Monster name: ")
        m = Monster(0, name, 100, 10)
        monster_list.append(m)
        pass

    print(monster_list)

    # Convert the list of monsters to a list of dictionary items
    # we can do this because are using a dataclass for the monster
    monsters_dict = []
    for i in range(count) :
        monsters_dict.append(asdict(monster_list[i]))
        pass
    print(monsters_dict)

    # Write the monster list that are dictionary items to a JSON file 
    with open("too_many_monsters.json", "w")  as file :
        json.dump(monsters_dict, file, indent=4)

    # Load the JSON file back in as a list that are dictionary items
    try:
        with open("too_many_monsters.json", "r")  as file :
            monsters_dict = json.load(file)
            print(monsters_dict)
            pass
        pass
    except json.JSONDecodeError as err:
        print(err)
    except Exception as excep:
        print(excep)
        pass
    else :
        print("YAY")
        pass
    finally :
        print("Always")
        pass

    # convert the list of dictionary items to monster obects using the **kwargs
    # we can do this because are using a dataclass for the monster
    monster_list = []
    for i in range(len(monsters_dict)) :
        monster_list.append(Monster(**monsters_dict[i]))
        pass
    print(monster_list)
    pass


def ConvertTheDictToJSON():
    # Convert the dict to json
    print("\n----------- Convert the dict to json string -----------")
    json_str = json.dumps(single_monster_dict, indent=4)
    with open("./Files-JSON/MyFile.json", "w") as out_file :
        out_file.write(json_str)
        pass
    print(json_str)
    pass

def Convert_json_str_to_dict_and_access_keys() :
    # Convert json str to dict and access keys
    print("\n----------- Convert json str to dict and access keys -----------")
    new_json_dict = json.loads(single_monster_json)

    new_json_dict['name'] = "Fred"
    print(new_json_dict['name'])

def OpenJSONFileToReadInAsStr():
    with open("./Files-JSON/MyFile.json", "r") as in_file :
        new_json_str = in_file.read()
        another_json_dict = json.loads(new_json_str)
        pass
    print(another_json_dict)

def SaveAMonsterToAFileWithJSON() :
    # Save a monster to a file via JSON
    print("\n----------- Save a monster json str to a file via JSON -----------")
    with open("./Files-JSON/monster_from_json.json", "w") as file :
        json.dump(single_monster_json, file, indent=4)
        pass

def LoadAMonsterFromAFileToSTRThenConvertToJSON() :
    # Load a monster from a file
    print("\n----------- Load a monster from a file -----------")
    with open("./Files-JSON/monster_from_json.json", "r") as file :
        json_str = json.load(file)
        json_dict = json.loads(json_str)
        print(json_str)
        pass

def SaveMonsterUsing_asdict_ToMakeDictAndSave() :
    # Save a monster by using the dataclass asdict to make a dict which json can save as a string
    print("\n----------- Save a monster by using the dataclass asdict to make a dict which json can save as a string -----------")
    with open("./Files-JSON/monster_from_obj.json", "w") as file :
        json_data = asdict(single_monster_obj)
        json.dump(json_data, file, indent=4)
        pass

def LoadMonsterFromFileAsDictAndMakeMonsterObject() :
    # Load a monster by using the json string and the **kwards (keyword arguments)
    print("\n----------- Load a monster by using the json string and the **kwards (keyword arguments) with a dataclass -----------")
    with open("./Files-JSON/monster_from_obj.json", "r") as file :
        json_data = json.load(file)
        m = Monster(**json_data)
        print(m)
        pass

def LoadingWithExceptions() :
    try:
        with open("./Files-JSON/too_many_monsters.json", "r")  as file :
            monsters_dict = json.load(file)
            print(monsters_dict)
            pass
        pass
    except json.JSONDecodeError as err:
        print(err)
    except Exception as excep:
        print(excep)
        pass
    else :
        print("YAY")
        pass
    finally :
        print("Always")
        pass

if __name__ == "__main__":
    # There are a lot of functions here to test. The big one that works with
    # man items and dictionaries is uncommented but you can work through these 
    CreateSaveLoadMonsters()

    # WorkingWithListsofDictionaryAndJSON()
    # ConvertTheDictToJSON()
    # Convert_json_str_to_dict_and_access_keys()
    # OpenJSONFileToReadInAsStr()
    # SaveAMonsterToAFileWithJSON()
    # LoadAMonsterFromAFileToSTRThenConvertToJSON()
    # SaveMonsterUsing_asdict_ToMakeDictAndSave()
    # LoadMonsterFromFileAsDictAndMakeMonsterObject()
    # LoadingWithExceptions()
