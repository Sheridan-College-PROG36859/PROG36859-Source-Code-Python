# use the monsters.csv
import csv

# Read a CSV file manually
def Read_CSV_file_Manually() :
    print("\n----------- Read_CSV_file_Manually -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        header = file.readline().rstrip()
        print(header)
        record = file.readline().rstrip()
        while record != '' :
            split = record.split(',')
            print(f'{split[0]},{split[1]},{split[2]},{split[3]}')
            record = file.readline().rstrip()
            pass
        pass
    pass

# Read a CSV file line by line
def Read_CSV_file_line_by_line() :
    print("\n----------- Read_CSV_file_line_by_line -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader :
            # print(line[1])
            print(len(line))
            print(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}')
            pass
        pass
    pass

# Read a CSV file as a list of records
def Read_CSV_file_list_of_records() :
    print("\n----------- Read_CSV_file_list_of_records -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        records = list(reader)
        for rec in records :
            print(rec)
            pass
        pass
    pass

# Read a CSV file as a dictionary
def Read_CSV_file_dictionary() :
    print("\n----------- Read_CSV_file_dictionary -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        dictionary_reader = csv.DictReader(file, delimiter=',')
        for record in dictionary_reader :
            print(record)
            pass
        pass
    pass

# Read a CSV file as a list of dictionary items
def Read_CSV_file_list_of_dictionary_items() :
    print("\n----------- Read_CSV_file_list_of_dictionary_items -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        dictionary_reader = csv.DictReader(file, delimiter=',')
        for record in dictionary_reader :
            print(f'{int(record['id'])}, {record['name']}')
            pass
        pass
    pass

# Write a CSV file (Duplicate the file)
def Read_CSV_Duplicate_the_file() :
    print("\n----------- Read_CSV_Duplicate_the_file -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')

        with open("./Files-CSV/more_monsters.csv", "w", newline='') as outFile:
            csv_out = csv.writer(outFile)
            for record in reader :
                csv_out.writerow(record)
                pass
            pass
        pass
    pass

# Write a filtered CSV with less info with help of dictionary items
def Read_CSV_filtered_file() :
    print("\n----------- Read_CSV_filtered_file -----------")
    with open("./Files-CSV/monsters.csv", "r") as file:
        reamonster_dict = csv.DictReader(file, delimiter=',')

        filter_monsters = [monster for monster in reamonster_dict if int(monster['maxHealth']) > 500 and float(monster['scariness']) > 9.0]
        print(filter_monsters)

        with open("./Files-CSV/more_monsters_filters.csv", "w", newline='') as outFile:
            csv_out = csv.writer(outFile)
            for monster in filter_monsters :
                csv_out.writerow(f'{monster['name']},{monster['maxHealth']}')
                pass
            pass
        pass
    pass

if __name__ == "__main__":
    Read_CSV_file_Manually()
    Read_CSV_file_line_by_line()
    Read_CSV_file_list_of_records()
    Read_CSV_file_dictionary()
    Read_CSV_file_list_of_dictionary_items()
    Read_CSV_Duplicate_the_file()
    Read_CSV_filtered_file()

    pass
