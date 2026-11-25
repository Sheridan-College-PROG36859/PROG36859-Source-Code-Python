# pip3 install mysql-connector-python
# import mysql.connector
import sqlite3

def ConnectToDatabase() :
    global conn
    try:
        # conn = mysql.connector.connect(host="localhost", user="root", password="1234")
        conn = sqlite3.connect('./Databases/localdatabase.db')
        pass
    except Exception as err:
        print(err)
        pass
    else:
        print("Connected to database")
    pass

def CreateCursor():
    global my_cursor
    my_cursor = conn.cursor() # creates a cursor from the connection
    pass

def CreateDatabase():
    sql = 'create database if not exists prog36859'
    try:
        my_cursor.execute(sql)
        pass
    except Exception as err:
        print(err)
        pass
    else:
        print("Database is created or exists")
        pass
    pass

def UseDatabase() :
    sql = 'use prog36859'
    my_cursor.execute(sql)
    pass

def CreateTable():
    try:
        sql = 'create table if not exists Monsters (id int not null, name varchar(200), max_health int, scariness float(0))'
        my_cursor.execute(sql)
        pass
    except Exception as err:
        print(err)
        pass
    else:
        print("Table exists or was created")
        pass
    pass

def InsertOneMonster():
    sql = 'insert into monsters values(101, "Bob", 100, 9.6)'
    my_cursor.execute(sql)
    conn.commit()
    pass

def InsertMultipleMonsters():
    records = [
        (202, "Fred", 90, 7.7),
        (303, "Mary", 95, 8.9),
        (202, "Bob", 70, 7.7)
    ]

    try:
        # sql = 'insert into monsters values (%s, %s, %s, %s)' #MySQL command
        sql = 'insert into monsters values (?, ?, ?, ?)'
        my_cursor.executemany(sql, records)
        conn.commit()
        pass
    except Exception as err:
        print(err)
        pass
    else:
        print("Many inserted")
    pass

def UpdateScariness():
    sql = 'update monsters set scariness = 1.0 where name = "Bob"'
    my_cursor.execute(sql)
    conn.commit()
    pass

def ReadRecords():
    sql = 'Select * from Monsters'
    my_cursor.execute(sql)
    results = my_cursor.fetchall()

    # print(results)
    for r in results:
        print(r)
        pass
    pass

def ReadAField():
    sql = 'Select * from Monsters'
    my_cursor.execute(sql)
    results = my_cursor.fetchall()
    for row in results:
        print(row[1])
    pass

def DeleteByName() :
    sql = 'Delete from monsters where name = "Bob"'
    my_cursor.execute(sql)
    conn.commit()
    pass

def ClearTable() :
    sql = 'Delete from Monsters'
    my_cursor.execute(sql)
    conn.commit()

    print("Bye Bob")

    pass

if __name__ == "__main__":

    ConnectToDatabase()
    CreateCursor()

    # Only use these when working with MySQL
    # CreateDatabase()
    # UseDatabase()
    CreateTable()

    InsertOneMonster()
    InsertMultipleMonsters()

    UpdateScariness()

    ReadRecords()
    # ReadAField()

    DeleteByName()
    ClearTable()

    my_cursor.close()
    conn.close()

    pass