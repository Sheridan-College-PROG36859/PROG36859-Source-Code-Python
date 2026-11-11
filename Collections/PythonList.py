#This will import the Item class from our Item.py
from Item import Item

def isEven(x):
    return True if x % 2 == 0 else False
def isOdd(x):
    return True if x % 2 != 0 else False

if __name__ == '__main__':
    result = None
    grades = [90, 89, 85, 92, 66, 76, 82]

    # For loop to copy grades
    grades_copy1 = []
    for m in grades:
        grades_copy1.append(m)
    print (grades_copy1)

    # list comprehension
    result = [grade for grade in grades]
    print(result)

    # for loop to get grades > 80
    grades_copy3 = []
    for m in grades:
        if m > 80:
            grades_copy3.append(m)
    print (grades_copy3)
    print(len(grades_copy3))

    # use sum to add all grades greater than 80
    # [1, 1, 1, 1, 1]
    value = sum([1 for grade in grades if grade > 80])
    print(value)

    # find all grades greater than 80 condition based selection 

    # find all grades that are even using % condition based selection
    result = []
    for grade in grades :
        if grade % 2 == 0 :
            result.append(grade)

    result = [grade for grade in grades if grade % 2 == 0]
    print([grade for grade in grades if grade % 2 == 0])
    print(result)

    # find all grades that are even using % then mult by 2
    print([grade * 2 for grade in grades if grade % 2 == 0])

    # use comprehension to get even grades using isEven
    print([grade for grade in grades if isEven(grade)])
    # use comprehension to get even grades using isOdd
    print([grade for grade in grades if isOdd(grade)])

    # List of Item
    item1 = Item("Book", 90, [1.02, 10.4, 8.9])
    item2 = Item("Model", 80, [0.02, 6.3, 8.9])
    item3 = Item("Video Game", 80, [6.02, 16.3, 28.9])
    items = Item.get_items()

    # print the list by default
    print(items)

    # use comprehension to get a list by using str on the item
    print([str(item) for item in items])
    # use comprehension to get a list of the names
    print([item.name for item in items])
    # use comprehension to get a list of weight
    print([item.weight for item in items])
    # use comprehension to get a list of price history (just the list)
    print([item.price_history for item in items])
    # use comprehension to get a list of price history that has weight higher than > 80
    print([item.price_history for item in items if item.weight > 80])

    # Important, the if the IF uses a list we need to use any

    # use comprehension to get a list of items that have a price greater than 10
    result = [item for item in items if any(price > 10 for price in item.price_history)]
    # output the list length
    print(len(result))
    # output the list items (using str) 
    result = [str(item) for item in items if any(price > 10 for price in item.price_history)]
    print(result)

    # output the list items names using comprehension 
    result = [item.name for item in items if any(price > 10 for price in item.price_history)]
    print(result)

    # use comprehension to get a list of item names that have a price greater than 15 (the list should only have names)
