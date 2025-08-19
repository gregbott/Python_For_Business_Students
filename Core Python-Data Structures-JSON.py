import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Data Structures

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## What's a data structure?
        As its name implies, a data structure is a container that holds data. Just like some post office boxes hold packages and others hold letters, Python's built-in data structures have different purposes and uses. Use data structures to organize and perform operations on data. Python has the following built-in data structures: Lists, Dictionaries, Sets, and Tuples. Each container has different attributes and is used for a different purpose.

        sources: (W3Schools, RealPython.com)

        <img src="./images/post_office_boxes.jpg" align="middle">
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Comparing Built-in Data Structures
        Below is a comparsion of four built-in data structures in Python. 

        <img src="./images/structures.jpg" align="middle">
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Tuples
        What is the proper pronunication of "tuple"? Answer: either TEW-pull or Tupple (like the 'u' sound in pup). 

        * Ordered sequence of elements
        * Tuples are immutable
        * Parentheses denote a tuple
        """
    )
    return


@app.cell
def _():
    t = 99
    return


@app.cell
def _():
    t_1 = ()
    t_1 = (4, 'hello', True, 3.1)
    return (t_1,)


@app.cell
def _(t_1):
    print(t_1[3])
    return


@app.cell
def _(t_1):
    print(t_1)
    print("Concatenate '7'")
    print(t_1 + (7,))
    return


@app.cell
def _(t_1):
    for v in t_1:
        print(v)
    return


@app.cell
def _():
    def tip_options(amount):
        # Use a tuple to return more than one value
        return(amount, amount*1.10, amount*1.15, amount*1.2)

    print(tip_options(30))
    print(type(tip_options(30)))
    return


@app.cell
def _():
    # Use a tuple to swap values
    y = 5
    x = 10
    print('x =', x, 'y =', y)
    (x, y) = (y, x)
    print('x =', x, 'y =', y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Lists

        A list is an ordered sequence of *items*. Lists are similar to arrays in other languages. One difference is that Lists can contain different types of data.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating Lists
 
        Lists are created using several methods.
        """
    )
    return


@app.cell
def _():
    #Use square brackets to make list

    cities = [] # an empty list
    return (cities,)


@app.cell
def _(cities):
    print(cities)
    return


@app.cell
def _(cities):
    type(cities)
    return


@app.cell
def _():
    cities_1 = ['Dallas', 'Chicago', 'Miami', 'Grand Rapids']
    print(cities_1, ' is of type ', type(cities_1))
    return (cities_1,)


@app.cell
def _(cities_1):
    len(cities_1)
    return


@app.cell
def _(cities_1):
    print(cities_1[2])
    return


@app.cell
def _(cities_1):
    print(cities_1[-1])
    return


@app.cell
def _(cities_1):
    print(cities_1[1:3])
    return


@app.cell
def _(cities_1):
    print(cities_1[1:])
    return


@app.cell
def _(cities_1):
    print(cities_1[1::2])
    return


@app.cell
def _(cities_1):
    print(cities_1[::-1])
    return


@app.cell
def _():
    # Lists are not limited to containing only values of a single type
    # A list may contain objects such as another list 
    my_list = [True, 0, "Greg Bott", 3.14159, ["steak","eggs","donuts"]]
    print(my_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Lists are Mutable
        """
    )
    return


@app.cell
def _(cities_1):
    print(cities_1)
    cities_1[2] = 'San Antonio'
    print(cities_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Adding items to a list
        * Use append to add elements to the end of a list. This operation *mutates* the list.
        ```Python
        <list>.append(element)
        ``` 

        Combine lists using the extend() function or + operator
        ```Python
        <list>.extend(element)

        <list> + <list>
        ``` 

        Insert an item at specified index location using insert().


        """
    )
    return


@app.cell
def _(cities_1):
    print(cities_1)
    print('Adding Columbia...')
    cities_1.append('Columbia')
    print(cities_1)
    return


@app.cell
def _(cities_1):
    more_cities = ['St. Louis', 'Tempe', 'Atlanta']
    cities_1.append(more_cities)
    print(cities_1)
    return


@app.cell
def _(cities_1):
    cities_1[5][2]
    return


@app.cell
def _(cities_1):
    print(cities_1)
    cities_1.insert(1, 'Austin')
    print(cities_1)
    return


@app.cell
def _():
    cities_2 = ['Dallas', 'Austin', 'Chicago', 'Miami', 'Grand Rapids', 'Columbia']
    return (cities_2,)


@app.cell
def _(cities_2):
    more_cities_1 = ['St. Louis', 'Tempe', 'Atlanta']
    cities_2.extend(more_cities_1)
    print(cities_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Copying a list
        If you use the following expression to create a new list, what you have is two references to a single object, NOT two lists.
        ```Python
        list_a = list_b
        ```
        """
    )
    return


@app.cell
def _():
    list_a = [1,2,3,4,5]

    list_b = list_a
    print("a=",list_a)
    print("b=",list_b)
    return list_a, list_b


@app.cell
def _(list_a, list_b):
    # Change ONLY list_b
    list_b[0] = 'Protein bar'
    print("a=",list_a)
    print("b=",list_b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Even though I did not change list a, changing list b also changed list a because the two lists are not two separate objects. They are two references pointing to the same object.
        """
    )
    return


@app.cell
def _():
    list_a_1 = [1, 2, 3, 4, 5]
    list_b_1 = list_a_1.copy()
    print('a=', list_a_1)
    print('b=', list_b_1)
    return list_a_1, list_b_1


@app.cell
def _(list_a_1, list_b_1):
    list_b_1[0] = 'Protein bar'
    print('a=', list_a_1)
    print('b=', list_b_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This time, list a did not change. Now we have TWO separate objects. Therefore, changing list b does not affect list a and vice versa.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Splitting and Joining Lists
        Using the split() function to separate a string using a delimter (e.g., a comma) creates a list object.
        """
    )
    return


@app.cell
def _():
    states = "Missouri, Alabama, Texas, Washington, Florida"
    print("States is of ", type(states))

    states = states.split(",")
    print(states, "this is of",type(states))
    return (states,)


@app.cell
def _(states):
    print(states[2])
    return


@app.cell
def _(states):
    print(type(states))
    states_1 = ','.join(states)
    print(states_1, 'this is of', type(states_1))
    return


@app.cell
def _():
    # Remember that you may split on any character.
    #   Here is an example of splitting an email address
    #   into the user name (string prior to the '@' symbol)
    #   and the domain (the part following the '@' symbol.')

    addr = 'monty@python.org'
    uname, domain = addr.split('@')
    split_email = addr.split('@' )
    print(f"user name = {uname}")
    print(f"domain name = {domain}")
    print(split_email)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## List Comprehensions

        List comprehensions are a compact method to build lists using a single line of code.

        Basic syntax
        ```python
        [ expr for item in iterable ]
        ```

        Using a conditional:
        ```python
        my_list = [ expr(element) for item in iterable if condition ] 
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For example, if I wanted to iterate over a range of numbers and make a list of the even ones, I could use this code:
        """
    )
    return


@app.cell
def _():
    even_number_list = []
    for x_1 in range(20):
        if x_1 % 2 == 0:
            even_number_list.append(x_1)
    print(even_number_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using a list comprehension I can do the same with a single line of code.
        """
    )
    return


@app.cell
def _():
    even_number_list_1 = [x for x in range(20) if x % 2 == 0]
    print(even_number_list_1)
    return


@app.cell
def _():
    even_number_list_2 = [x for x in range(20) if x % 2 == 0]
    return


@app.cell
def _():
    num_list = [y for y in range(100) if (y % 2 == 0) or (y % 5 == 0)]
    print(num_list)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Removing Items from a List
        """
    )
    return


@app.cell
def _():
    t_2 = ['a', 'b', 'c', 'd', 'e']
    del t_2[1]
    print(t_2)
    return (t_2,)


@app.cell
def _(t_2):
    x_2 = t_2.pop()
    print('Deleted ', x_2)
    print('New list is ', t_2)
    return


@app.cell
def _(cities_2):
    print(cities_2)
    cities_2.remove('Chicago')
    print(cities_2)
    return


@app.cell
def _(cities_2):
    cities_2.remove('St. Louis')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Be careful when removing items from a list. If you attempt to remove items while iterating over the same list, items may be skipped. 
        """
    )
    return


@app.cell
def _():
    my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return (my_list_1,)


@app.cell
def _(my_list_1):
    for item in my_list_1:
        if item > 5:
            my_list_1.remove(item)
    print(my_list_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        One solution is to use a list comprehension.
        """
    )
    return


@app.cell
def _():
    my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    my_list_2 = [item for item in my_list_2 if item < 6]
    print(my_list_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Another solution is to reverse the list. That way, if the last item (item 9) is deleted, it doesn't alter the indexes of the rest of the list.
        """
    )
    return


@app.cell
def _():
    my_list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item_1 in reversed(my_list_3):
        if item_1 > 5:
            my_list_3.remove(item_1)
    print(my_list_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Testing for membership

        Use the in keyword to test for list membership.
        """
    )
    return


@app.cell
def _(cities_2):
    print(cities_2)
    print('Dallas' in cities_2)
    print('Tuscaloosa' in cities_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Enumerating a list
        """
    )
    return


@app.cell
def _(cities_2):
    count = 0
    for city in cities_2:
        print(count, city)
        count = count + 1
    return


@app.cell
def _(cities_2):
    for x_3 in range(len(cities_2)):
        print(x_3, cities_2[x_3])
    return


@app.cell
def _(cities_2):
    for city_1 in enumerate(cities_2):
        print(city_1)
    return


@app.cell
def _(cities_2):
    for count_1, ele in enumerate(cities_2, 10):
        print(count_1, ele)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Iterating a list

        Use a for loop to iterate a list.
        """
    )
    return


@app.cell
def _(cities_2):
    for city_2 in cities_2:
        print(city_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Use the len() function to determine how many items are in the list and use that within a range() function.
        """
    )
    return


@app.cell
def _(cities_2):
    for i in range(len(cities_2)):
        print(cities_2[i], end=' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## List Concatenation

        """
    )
    return


@app.cell
def _():
    # Use the '+' operator to concatenate lists
    a = [1,2,3]
    b = [4,5,6]
    c = a + b # does not mutate 'a' or 'b'

    print("c = ", c)

    print("a = ", a)
    print("b = ", b)
    return a, b, c


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Extending a list
        """
    )
    return


@app.cell
def _(a, b, c):
    print("list 'a' = ", a)
    print("list 'b' =", b)

    a.extend(b) # This combines a and b, mutates a but not b

    print("list 'a' =", a)
    print("list 'b' =", b)
    print(c)
    return


@app.cell
def _(a):
    # Use the '*' operator to repeat items
    print(a * 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ##Slicing Lists
        You can return parts of a list using slicing operators. Other objects (e.g., strings and tuples) can also be sliced.
        """
    )
    return


@app.cell
def _():
    t_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(t_3[1:3])
    return (t_3,)


@app.cell
def _(t_3):
    print(t_3[:3])
    return


@app.cell
def _(t_3):
    print(t_3[3:])
    return


@app.cell
def _(t_3):
    print('Last item in the list = ', t_3[-1])
    return


@app.cell
def _(t_3):
    t_3[-1] = 'watermelon'
    print(t_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Zipping a list

        The zip() function takes iterables as its parameter and returns a zip object. Think of zip like a physical zipper that brings together two different iterable objects. 
        """
    )
    return


@app.cell
def _():
    # zip function example

    students = 'Darlene','Desmond','Billy'
    grades = [100, 99, 72] 
    zipped_students = list(zip(students, grades))

    print(zipped_students)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Zipping unequal length lists

        The zip() function expects iterables of **equal lengths**. Trailing items are ignored.

        To work with iterables of different lengths, Python provides the zip_longest() function as part of the **itertools** module.

        ```Python
        zip_longest( iterable1, iterable2, fillvalue)
        ```
        """
    )
    return


@app.cell
def _():
    import itertools
    students_1 = ('Darlene', 'Desmond', 'Billy', 'Macy')
    grades_1 = [100, 99, 72]
    zipped_students_1 = list(itertools.zip_longest(students_1, grades_1, fillvalue=None))
    print(zipped_students_1)
    return


@app.cell
def _():
    students_2 = ('Darlene', 'Desmond', 'Billy', 'Macy')
    grades_2 = [100, 99, 72]
    zipped_students_2 = list(zip(students_2, grades_2))
    print(zipped_students_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Sorting Lists
        """
    )
    return


@app.cell
def _():
    # Use sorted() to display a sorted list but not mutate it.
    my_letters = ['n','r','y','x','a','w']

    print("sorted list = ", sorted(my_letters))
    print("my_letters = ", my_letters)
    return (my_letters,)


@app.cell
def _(my_letters):
    # Use the sort() method to sort the items in a list
    my_letters.sort()
    print(my_letters)
    return


@app.cell
def _(my_letters):
    my_letters_1 = my_letters.sort()
    print(my_letters_1)
    return


@app.cell
def _():
    my_letters_2 = ['n', 'r', 'y', 'x', 'a', 'w']
    my_letters_2.sort(reverse=True)
    print(my_letters_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Use a list to return more than one value from a function
        """
    )
    return


@app.cell
def _():
    def tip_options_1(amount):
        return [amount, amount * 1.1, amount * 1.15, amount * 1.2]
    print(tip_options_1(30))
    print(type(tip_options_1(30)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Working With Nested Lists
        """
    )
    return


@app.cell
def _():
    my_list_4 = [['Ford', 'Chevrolet', 'Volkswagen'], ['F150', 'Suburban', 'Passat'], ['Big Bang Theory', 'Young Sheldon', 'Mindhunter']]
    print(my_list_4[0][1])
    print(my_list_4[2][2])
    return


@app.cell
def _():
    y_1 = 5
    x_4 = 10
    print('x =', x_4, 'y =', y_1)
    [x_4, y_1] = [y_1, x_4]
    print('x =', x_4, 'y =', y_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Sets
        * Sets are unordered.
        * Set elements are unique. Duplicate elements are not allowed.
        * You may add or remove items from the set, but you cannot edit an item in a set.
        * Accessing items by index (e.g., myset[1]) is NOT supported.
        * Sets are denoted by curly braces.
        * Membership tests are more efficient using sets than lists or tuples.

        You can define a set using the set() function.b
        ```python
        x = set(<iter>)
        ```
        """
    )
    return


@app.cell
def _():
    my_list_5 = ['a', 'b', 1, 'c', 1]
    set2 = set(my_list_5)
    print(set2)
    print(my_list_5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You can also create a set using curly braces {}. However, you cannot create an empty set using a pair of curly braces like you can for a list.
        """
    )
    return


@app.cell
def _():
    # INCORRECT
    my_set = {}  # <-- results in a dictionary, NOT a set
    print(type(my_set))
    return


@app.cell
def _():
    my_set_1 = set()
    print(type(my_set_1))
    return


@app.cell
def _():
    my_set_2 = {1, 1, 6, 7, 3, 5, 5, 5, 5, 5, 'red'}
    print(type(my_set_2))
    print(my_set_2)
    return (my_set_2,)


@app.cell
def _(my_set_2):
    my_set_2[0]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Why do I care about sets?
        Sets in Python provide the same benefits as sets in mathematics. Sets contain a well-defined collection of distinct objects called elements. Using the set object enables you to efficiently perform set operations such as union and intersection.

        ![](images/data_science_diagram.png) <br>
        (image source: https://towardsdatascience.com)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating sets
        Use curly braces to denote a set or use the set() constructor. If you use set(), you must provide an iterable as the argument.
        """
    )
    return


@app.cell
def _():
    # Persons with expertise in specific areas
    cs_expertise = {"Bill", "Matt", "Alexandra", "Joe", "Dexter"}
    stats_expertise = set(["Dexter", "Subha", "Brad", "Bruce"])
    business_expertise = {"Kay","Jonathan","Dexter","Suzanne", "Matt"}
    return business_expertise, cs_expertise, stats_expertise


@app.cell
def _(business_expertise, cs_expertise, stats_expertise):
    # Who might be suited for Data Science (intersection of three topics)
    data_scientists = cs_expertise.intersection(stats_expertise, business_expertise)
    print(data_scientists)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You can also use the set() method to create a set. The argument for the set method must be an iterable.
        """
    )
    return


@app.cell
def _():
    #Use the set() method to create a set, parameter must be <iter> (an iterable --e.g., a list)
    my_set2 = set(['foo', 'bar', 3.141, 'bar'])
    print(my_set2)
    return


@app.cell
def _():
    #Error creating tropical_fruits set using set() contructor...why?
    tropical_fruits = set(["Guava", "Dragon Fruit", "Banana","Banana"])
    temperate_fruits = {"Apple", "Peach", "Plum"}

    all_fruit = tropical_fruits.union(temperate_fruits)
    print(all_fruit)
    return


@app.cell
def _():
    #Empty sets are evaluated as False
    loch_ness_monsters = set()
    print("The set of Loch Ness Monsters is " + str(bool(loch_ness_monsters)))
    print()
    return (loch_ness_monsters,)


@app.cell
def _(loch_ness_monsters):
    #You can add, update, and remove items, but you cannot change items in a set
    loch_ness_monsters.add("Marvin")
    print("Added Marvin to monster set...")
    print("The set of Loch Ness Monsters is " + str(bool(loch_ness_monsters)), loch_ness_monsters)
    print("The length of the monster set is " + str(len(loch_ness_monsters)))
    return


@app.cell
def _():
    grades_3 = {81, 100, 81, 89, 99, 99, 99, 76, 94, 93, 86, 75, 88, 96, 76, 87, 90, 81, 78, 99, 83, 94, 75, 83, 92, 96, 81, 99, 89, 99, 98, 100, 95, 84, 94, 97, 100, 92, 97, 98, 92, 95, 88, 90, 98, 87, 86, 95, 86, 84, 91, 87, 88, 83, 89, 84, 98, 75, 90, 100, 79, 83, 94, 89, 93, 84, 83, 94, 84, 93, 97, 75, 81, 91, 84, 78, 89, 96, 97, 99, 90, 98, 83, 93, 96, 98, 91, 77, 98, 97, 76, 98, 75, 89, 92, 81, 83, 84, 82, 94, 89, 77, 96, 94, 100, 86, 79, 87, 78, 83, 86, 89, 99, 77, 96, 88, 91, 86, 89, 99, 82, 83, 92, 91, 84, 83, 76, 89, 90, 82, 75, 84, 83, 81, 96, 87, 90, 82, 93, 76, 86, 100, 81, 88, 100, 94, 84, 99, 77, 91, 92, 98, 88, 90, 83, 88}
    print(grades_3)
    return (grades_3,)


@app.cell
def _(grades_3):
    c_and_higher = set(range(75, 101))
    missing_grades = grades_3.symmetric_difference(c_and_higher)
    print('What grades are missing from 75-100?: ' + str(missing_grades))
    return


@app.cell
def _():
    # Add set lookup differences and symmetric_differene vs. difference
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Dictionaries

        A Python Dictionary object uses key-value pairs. Just like you would use a traditional dictionary to find the definition (value) of a word (key), a Python dictionary uses keys and values. A key is a unique identifier used to find data (the value). You can think of dictionaries like a list, but with a flexible index. List indexes are integers (e.g., MyList[2]), but the index or keys used to associate values in a dictionary can be any immutable data type (e.g., employee['2334']).

        Dictionaries are **unordered** and use key-value pairs to store and retrieve data. In other languages this structure might be called an *associative array* or a *hashmap*.

        \*Python 3.6+ supports using a ordered (insert order) dict.

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating dictionaries
        Use curly braces and a colon to indicate to the interpreter that you are creating a dictionary data structure. A key can be any immutable data type.
        """
    )
    return


@app.cell
def _():
    # Pretty Print is a module that displays dictionaries in a more human-readable format.
    import pprint as pp

    # The employee ID is associated with the employee name
    ua_directory = {'netID':'gjbott', 'name':'Gregory J. Bott', 'role':'faculty','courses':['MIS501', 'MIS460/561', 'MIS598']}

    print("Without pretty print:")
    print(ua_directory,'\n')

    print("With pretty print:")
    pp.pprint(ua_directory)
    return (pp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Creating an empty dictionary
        If you attempt to reference a dictionary object without creating it first, you'll receive a NameError.
        """
    )
    return


@app.cell
def _(person):
    # ERROR you cannot create a key-value pair in a non-existent dict
    person[1000] = {'first_name':'Greg', 'last_name':'Bott', 'spouse':'Amy', 'children':['John Davis', 'Piper', 'Will', 'Truett'], 'pets':{'Bama':'dog', 'TJ':'cat'}}
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To assign a dict object to a variable, use a set of empty curly braces.
        """
    )
    return


@app.cell
def _():
    # Create an empty dictionary
    person = {}

    #Display the type of the 'person' variable
    print(type(person))
    return (person,)


@app.cell
def _():
    a_1 = {'first_name': 'Greg', 'last_name': 'Bott', 'spouse': 'Amy'}
    print(a_1)
    return


@app.cell
def _():
    a_2 = {'first_name': 'Joe', 'last_name': 'Devlin', 'spouse': 'Suzanne'}
    print(a_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Adding values to a dictionary
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Instead, add a key (e.g., 1000, 1001) and provide the dict as the value. So, person has nested dictionaries and a nested list.

        1000, 1001 are keys. The dict containing first_name, last_name, etc. is the value. Within that dict are additional key-value pairs (first name --> Greg, etc.). 
        """
    )
    return


@app.cell
def _(person, pp):
    person[1000] = {'first_name':'Greg', 'last_name':'Bott', 'spouse':'Amy', 'children':['John Davis', 'Piper', 'Will', 'Truett'], 'pets':{'Bama':'dog', 'TJ':'cat'}}
    person[1001] = {'first_name':'Joe', 'last_name':'Devlin', 'spouse':'Suzanne', 'children':['CK', 'Alan', 'Devin', 'Tom'], 'pets':{'Orangey':'gold fish', 'Hammer':'turtle'}}

    pp.pprint(person)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Accessing data in a dictionary
        Use ```dict[key]``` to return the value from the key-value pair. If the value doesn't exist, an exception is thrown. Use the get() method to retrieve keys and handle missing keys more gracefully.

        You can also use ```keys()``` to list the keys in your dictionaries, ```values``` to access the values of the key-value pair or ```items()``` to access both.
        """
    )
    return


@app.cell
def _(person):
    person.keys()
    return


@app.cell
def _(person):
    person.values()
    return


@app.cell
def _(person):
    person.items() # The key-value pair is an item.
    return


app._unparsable_cell(
    r"""
    person[[] = {'name':'green'}
    """,
    name="_"
)


@app.cell
def _(person):
    # Print the first_name attribute of the person 1001 key.
    print(person[1001]['first_name'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Using the get() method
        Use the get() method to access keys. Using get() avoids a KeyError if the desired key does not exist. Instead, Python returns the None value.
        """
    )
    return


@app.cell
def _(person, pp):
    # Display the person dictionary
    pp.pprint(person)

    # ERROR - this key does NOT exist
    person[9999]
    return


@app.cell
def _(person):
    # Attempting to retrieve a non-existent dict value using get() returns None instead of a KeyError
    print(person.get(1000).get('pets').get('bama'.title()))
    return


@app.cell
def _(person, pp):
    pp.pprint(person.get(1001))
    return


@app.cell
def _(person):
    # You can also provide a default value if a key does not exist
    print(person.get('ss_number', 'no SS# provided'))
    return


@app.cell
def _():
    # Use a List as values a dictionary
    make_model = {"Ford":["Mustang","Explorer","Focus"],"Volkswagen":["Passat","Jetta","Beetle"]}
    print(make_model["Ford"])
    return (make_model,)


@app.cell
def _(person, pp):
    # Replace values using a key
    pp.pprint(person[1001])
    return


@app.cell
def _(person, pp):
    person[1001]['pets'] = {'Rocky':'flying squirrel'}
    pp.pprint(person[1001])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Removing an items using del or pop
        You can use ```del``` or ```pop``` to remove items from a dictionary. 
        """
    )
    return


@app.cell
def _(person, pp):
    pp.pprint(person[1001])
    return


@app.cell
def _(person, pp):
    # Remove the pets key and values
    del person[1001]['pets']
    pp.pprint(person[1001])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Just as in a list, ```pop``` returns the value deleted that you can store in a variable.
        """
    )
    return


@app.cell
def _(person, pp):
    pp.pprint(person[1000])
    children = person[1000].pop('children')
    return (children,)


@app.cell
def _(person, pp):
    pp.pprint(person[1000])
    return


@app.cell
def _(children):
    children
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Clear a dictionary
        Use the clear() method to empty the contents of a dictionary.
        """
    )
    return


@app.cell
def _(person):
    print(person)
    person.clear()
    print(person)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Using a loop to examine a dictionary
        Although looping through a dictionary fails to take advantage the speed of a dictionary, sometimes you may find it useful. Remember that dictionaries contain a key / value pair and that you must loop through them differently than you would a list.
        """
    )
    return


@app.cell
def _(person):
    person[1000] = {'first_name':'Greg', 'last_name':'Bott', 'spouse':'Amy', 'children':['John Davis', 'Piper', 'Will', 'Truett'], 'pets':{'Bama':'dog', 'TJ':'cat'}}
    person[1001] = {'first_name':'Joe', 'last_name':'Devlin', 'spouse':'Suzanne', 'children':['CK', 'Alan', 'Devin', 'Tom'], 'pets':{'Orangey':'gold fish', 'Hammer':'turtle'}}
    return


@app.cell
def _(person):
    for x_5 in person:
        print(x_5)
    return


@app.cell
def _(person, pp):
    for v_1 in person.values():
        print(v_1)
        for val in v_1.values():
            pp.pprint(val)
        print('-' * 30)
    return


@app.cell
def _(person):
    for k, v_2 in person.items():
        print(k, v_2)
    return


@app.cell
def _(person):
    list(person.items())[-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Using a loop to add values to a dictionary.
        So far we have manually added items to a dictionary. Most often you will add items progamatically (e.g., using a loop) rather than manually. Below is part of the code I use find duplicate files using an MD5 hash. A hash is a one-way algorithm applied to an object that results in a fixed-length string that uniquely identifies that object.

        We'll use the os module to access the file system and the hashlib to apply the MD5 algorithm to the files and then store them in a dictionary using the MD5 value as the key.
        """
    )
    return


@app.cell
def _(pp):
    import os
    import hashlib

    # Create a blank dictionary
    os_files = {}

    # Hash Function
    def hashfile(path, blocksize=65536):
    
        # Get the file, read binary
        file_to_hash = open(path, 'rb')
    
        # Create an MD5 hasher object
        hasher = hashlib.sha256()
    
        # Load part of the file (the size of the block)
        #    We divide the file into smaller parts to avoid using all the 
        #    available RAM
        buf = file_to_hash.read(blocksize)
    
        # Add blocks of the file until the buffer is empty
        while len(buf) > 0:
            hasher.update(buf)
            buf = file_to_hash.read(blocksize)
        file_to_hash.close()
    
        # Return the MD5 hex digest of the file
        return hasher.hexdigest()

    for file in os.listdir():
        # Use error handling to avoid errors (e.g., file permission issues)
        try:
            # Use the hash value (hex digest) as the key and use the file name as the value
            os_files[hashfile(file)] = file
        except:
            pass
    
    # Display the Dictionary
    pp.pprint(os_files)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Check for Values in a Dictionary

        To determine if a value is present within a key, us the *in* keyword.
        """
    )
    return


@app.cell
def _(make_model):
    make_model
    return


@app.cell
def _(make_model):
    # "Focus" is a value in the dict
    print("Focus" in make_model["Ford"])
    return


@app.cell
def _(make_model):
    make_model["Ford"]
    return


@app.cell
def _(make_model):
    # "Explorer II" is not in the dict
    print("Explorer II" in make_model["Ford"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Check for Keys in a Dictionary
        """
    )
    return


@app.cell
def _(make_model):
    search_key = "Ford"
    if search_key in make_model:
        print(f"'{search_key}' key found in dictionary!")
    else:
        print(f"'{search_key}' key NOT found in dictionary.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Attempting to Access Keys that Don't exist
        If you attempt to access a key that does not exist within the dictionary, Python will raise an exception

        """
    )
    return


@app.cell
def _(person):
    person[1000] = {'first_name':'Greg', 'last_name':'Bott', 'spouse':'Amy', 'children':['John Davis', 'Piper', 'Will', 'Truett'], 'pets':{'Bama':'dog', 'TJ':'cat'}}
    person[1001] = {'first_name':'Joe', 'last_name':'Devlin', 'spouse':'Suzanne', 'children':['CK', 'Alan', 'Devin', 'Tom'], 'pets':{'Orangey':'gold fish', 'Hammer':'turtle'}}
    return


@app.cell
def _(person, pp):
    pp.pprint(person)
    return


@app.cell
def _(person):
    # ERROR: KeyError (key does not exist in the dictionary)
    print(person[1000])
    print(person['first_name']) # first_name IS a key in the dict, why the error?
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Creating a dictionary from a JSON file
        """
    )
    return


@app.cell
def _():
    import pathlib
    import json
    # create Path object for file path (path to the file, filename)
    fb_game_path = pathlib.Path('/home/gjbott/Dropbox/research/github/gregbott/mis501/2023_501/files/2017_Alabama_v_LSU.json')
    fb_game_path.absolute()
    return fb_game_path, json


@app.cell
def _(fb_game_path, json):
    if fb_game_path.exists():
        # open the data filepath
        with open(fb_game_path, 'r') as fp:

            # read the bytes from the datafile
            json_bytes = fp.read()

            # decode the bytes to utf-8
            #json_str = json_bytes.decode('utf-8')

            # load the decoded bytes as JSON
            game_data = json.loads(json_bytes)
        
            print(f'The game file includes {len(game_data)} records.\n The game file is a {type(game_data)}.')
    else:
        print('{fb_game_path.name} does not exist')
    return (game_data,)


@app.cell
def _(game_data):
    # Let's examine what's in the dictionary
    # Most often, dictionaries will be too long to just print them. Even just printing the keys can be problematic, but since 
    #    we already know the length of the dict is 8, let's print the keys.
    game_data.keys()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        One method to view the contents of a dictionary is to first convert the dictionary items (aka, keys and pairs) to a list and then slice the list. 
        """
    )
    return


@app.cell
def _(game_data, pp):
    pp.pprint(game_data['videos'][0])
    return


@app.cell
def _(game_data, pp):
    pp.pprint(game_data['videos'][0]['links']['source']['full']['href'])
    return


@app.cell
def _(game_data):
    len(game_data['drives']['previous'][0]['plays'])
    return


@app.cell
def _(game_data, pp):
    for play in game_data['drives']['previous'][0]['plays']:
        pp.pprint(play['text'])
        #pp.pprint(play['start']['yardLine'])
        #pp.pprint(play['statYardage'])
    return


@app.cell
def _(game_data):
    # First let's determine what type of object 'scoringPlays' is
    print(type(game_data['scoringPlays']))
    return


@app.cell
def _(game_data):
    # Since it's a list, we can slice it
    # Here are the first three items
    plays = game_data['scoringPlays']
    plays
    return (plays,)


@app.cell
def _(plays):
    # Plays is a list of dicts
    print(type(plays))
    print(type(plays[0]))
    return


@app.cell
def _(plays):
    # Since each item of the list is a dict, we can get its keys
    plays[0]
    return


@app.cell
def _(plays):
    for play_1 in plays:
        print(play_1['clock']['displayValue'], play_1['text'])
    return


@app.cell
def _(game_data):
    list(game_data['drives']['previous'])[1]
    return


@app.cell
def _(game_data):
    for play_2 in game_data['drives']['previous'][5]['plays']:
        print(play_2['text'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Updating dictionary values
        Assigning a value to an existing key/value pair will replace the value.

        You can also use the update method to replace multiple values in a dictionary and add new values.

        ```update()``` takes a dictionary as its parameter.

        To update/add multiple values at the same time, provide the keys to add/update and their valuesTo update/add multiple values at the same time, provide the keys to add/update and their values.
        """
    )
    return


@app.cell
def _():
    person_1 = {}
    return (person_1,)


@app.cell
def _(person_1, pp):
    person_1[1000] = {'first_name': 'Greg', 'last_name': 'Bott', 'spouse': 'Amy', 'children': ['John Davis', 'Piper', 'Will', 'Truett'], 'pets': {'Bama': 'dog', 'TJ': 'cat'}}
    person_1[1001] = {'first_name': 'Joe', 'last_name': 'Devlin', 'spouse': 'Suzanne', 'children': ['CK', 'Alan', 'Devin', 'Tom'], 'pets': {'Orangey': 'gold fish', 'Hammer': 'turtle'}}
    pp.pprint(person_1)
    return


@app.cell
def _(person_1, pp):
    person_1[1000].update({'first_name': 'Gregory', 'ss_number': '123-45-6789', 'middle': 'Hamilton'})
    pp.pprint(person_1)
    return


@app.cell
def _(person_1, pp):
    person_1[1001]['children'].append('Sally')
    pp.pprint(person_1[1001])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # JSON
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        load() vs loads()

        ![alt text](./images/load_vs_loads.jpg "Title")
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        dump() vs dumps()

        ![alt text](./images/dump-vs-dumps.jpg "Title")
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Loading JSON
        """
    )
    return


@app.cell
def _():
    json_file = """
    {'people': [{'children': ['John Davis', 'Piper', 'Will', 'Truett'],
                 'first_name': 'Greg',
                 'last_name': 'Bott',
                 'pets': {'Bama': 'dog', 'TJ': 'cat'},
                 'spouse': 'Amy'},
                {'children': ['CK', 'Alan', 'Devin', 'Tom'],
                 'first_name': 'Joe',
                 'last_name': 'Devlin',
                 'pets': {'Hammer': 'turtle', 'Orangey': 'gold fish'},
                 'spouse': 'Suzanne'}]}

    """
    return


@app.cell
def _(data, pp):
    pp.pprint(data)
    return


@app.cell
def _(json):
    with open('files/directory.json', 'r') as f:
        data = json.loads(f.read())
    return (data,)


@app.cell
def _(data):
    type(data)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        <table class="docutils align-default" id="json-to-py-table">
        <colgroup>
        <col style="width: 44%">
        <col style="width: 56%">
        </colgroup>
        <thead>
        <tr class="row-odd"><th class="head"><p>JSON</p></th>
        <th class="head"><p>Python</p></th>
        </tr>
        </thead>
        <tbody>
        <tr class="row-even"><td><p>object</p></td>
        <td><p>dict</p></td>
        </tr>
        <tr class="row-odd"><td><p>array</p></td>
        <td><p>list</p></td>
        </tr>
        <tr class="row-even"><td><p>string</p></td>
        <td><p>str</p></td>
        </tr>
        <tr class="row-odd"><td><p>number (int)</p></td>
        <td><p>int</p></td>
        </tr>
        <tr class="row-even"><td><p>number (real)</p></td>
        <td><p>float</p></td>
        </tr>
        <tr class="row-odd"><td><p>true</p></td>
        <td><p>True</p></td>
        </tr>
        <tr class="row-even"><td><p>false</p></td>
        <td><p>False</p></td>
        </tr>
        <tr class="row-odd"><td><p>null</p></td>
        <td><p>None</p></td>
        </tr>
        </tbody>
        </table>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Dumping JSON
        """
    )
    return


@app.cell
def _(json, person_1):
    with open('files/directory.json', 'w') as f_1:
        json.dump(person_1, f_1)
    return


@app.cell
def _(person_1):
    import pandas as pd
    directory_df = pd.DataFrame.from_dict(person_1, orient='index')
    return (directory_df,)


@app.cell
def _(directory_df):
    directory_df.to_json('files/directory.json', orient='records' )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
