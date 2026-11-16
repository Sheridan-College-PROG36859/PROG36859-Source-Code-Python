if __name__ == '__main__':

    dictionary = {101: 'Book', 202: 'Model', 303: 'Video Game'}

    # print the dictionary
    print(dictionary)
    
    # print the value of key = 202
    print(dictionary[202])
    
    # try to print a key that does not exist
    # value = dictionary[404]

    # add an element, always check for key
    if 404 not in dictionary :
        dictionary[404] = 'Not Found, but found'
        pass

    dictionary[404] = "FOUND!"
    print(dictionary)

    # delete an element, always check for key
    if 404 in dictionary :
        del dictionary[404]

    print(dictionary)

    # get the length of the dictionary
    print(len(dictionary))    

    # use a loop to naviage through the dictionary
    for k in dictionary :
        print(f'{k} -> {dictionary[k]}')

    # CLEAR everything from your dictionary 
    # dictionary.clear()
    # print(dictionary)
    # print(len(dictionary))

    # Delete the items in the dictionary itself
    # del dictionary
    # print(dictionary)

    # Get an element from the dictionary using [] notation
    ### Option 1: using the key [] notation
    print(dictionary[202])
    # print(dictionary[404])

    ### Option 2: using the get() function, with default
    value = dictionary.get(101)
    print(value)
    value = dictionary.get(404)
    print(value)
    value = dictionary.get(404, 'Default - Not Found')
    print(value)

    ### Option 3: Using pop() function
    value = dictionary.pop(303)
    print(value)
    if 303 not in dictionary :
        print('303 has been removed')
        pass
    print(dictionary)
    # value = dictionary.pop(303)

    # iterate using items() and k, v 
    for k, v in dictionary.items() :
        print(f'{k}:{v}')

    # iterate keys(), values() 
    for k in dictionary.keys() :
        print(k)

    # iterate using values()
    for v in dictionary.values() :
        print(v)

    # print each the items, keys and values
    print(dictionary.items())
    print(dictionary.keys())
    print(dictionary.values())

    # Dictionary comprehensions
    campuses = ('Oakville', 'Mississauga', 'Brampton')
    student_count = (5000, 4000, 6000)

    # Combine the campuses and student_count
    campus_students = {campuses[i]:student_count[i] for i in range(len(campuses))}
    print(campus_students)

    # Output only the campuses with student_count greater than 5000
    output = [k for k, v in campus_students.items() if v > 5000]
    print(output)

    # New dictionary of campuses with student_count greater than 5000
    output = {k:v for k, v in campus_students.items() if v > 5000}
    print(output)

    # reverse key and values
    output = {v:k for k, v in campus_students.items()}
    print(output)

