def isOdd(x):
    return True if x % 2 != 0 else False

if __name__ == '__main__':

    # sets are unordered collection of unique data (i.e., no duplicaiton allowed)
    # ceate a set 
    # not_a_set = set(2, 4, 3, 2) # will not work to create a set
    myset = set([2, 4, 3, 2]) # any duplicaiton of data will automatically be removed in set
    print(myset)

    # add an element of 10 and output it
    myset.add(10)
    print(myset)

    # add an element of 5 and output it
    myset.add(5)
    print(myset)

    # output length of a set
    print(len(myset))

    # update the set by adding another collection, e.g., list, tuple, and output it
    myset.update([101, 202, 303])
    print(myset)

    # update the set with another set and output it
    set2 = set(['a', 'b', 'c'])
    myset.update(set2)
    print(myset)

    # use remove() to remove an item
    myset.remove(101)
    print(myset)

    # use discard() to remove an item
    myset.discard(202) 
    print(myset)

    # what happens when we attempt to remove something that does not exist
    #myset.remove(404)
    myset.discard(404)

    # output each item using a for loop
    for item in myset :
        print(item, end='-')
    print()

    # clear a set
    myset.clear()
    print(myset)

    #________________________________________________________________________________________________________
    # SET OPERATIONS
    setA = set([1, 2, 3, 4])
    setB = set([3, 4, 5, 6])
    #print (f'SetA: {setA}')
    #print (f'SetB: {setB}')

    # union of two sets, using union() and | to find make a new set that has all unique items
    result = setA.union(setB)
    print(result)
    result = setA | setB
    print(result)

    # intersection of two sets, using intersection() and & to find common items in both sets
    result = setA.intersection(setB)
    print(result)
    result = setA & setB
    print(result)

    # difference of two sets, using difference() and - to find items that are not in set A but in set B
    result = setA.difference(setB)
    print(result)
    result = setA - setB
    print(result)

    # symmetric difference of two sets, using symmetric_difference and ^ to find items that are in one set, but not in both
    result = setA.symmetric_difference(setB)
    print(result)

    # Subset/superset Finding
    small_basket = {"apple", "banana"}
    big_basket = {"apple", "banana", "orange", "mango"}

    # --- ISSUBSET ---
    # Checks if all items in the parameter exist in the caller set
    # using issubset or <=
    print(small_basket.issubset(big_basket))
    print(big_basket.issubset(small_basket))

    # --- ISSUPERSET ---
    # Checks if the caller containes all the items in the parameter
    # using issuperset or >=
    print(small_basket.issuperset(big_basket))
    print(big_basket.issuperset(small_basket))

    # Set comprehensions are similar to list
    print(['apple' for item in big_basket if item == 'apple'])

