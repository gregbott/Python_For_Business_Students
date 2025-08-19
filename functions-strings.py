import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        2/2/2022
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Functions
        A *function* is a discrete set of instructions typically designed to receive one or more values and return a value. A function call receives values called *arguments* or *parameters* and it typically *returns* a value or object.

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Built-in functions
        For example, the print() function takes an argument and sends output to the console.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Print() and Input()
        The ```print()``` function displays messages and is sometimes used as simple debugging method. 

        The print function underwent major changes from Python 2 to Python 3 and is written differently depending on the version. Python 2 omits the parentheses (e.g., ```print a```) while Python 3 requires them (e.g., ```print(a)``` ).

        Calling the print function without an argument results in a blank line.
        """
    )
    return


@app.cell
def _():
    print()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You will often print string literals such as:
        """
    )
    return


@app.cell
def _():
    print("Data loading complete.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Or using a variable:
        """
    )
    return


@app.cell
def _():
    a = 'apple'
    print(a)
    return


@app.cell
def _():
    print("The print() function did this.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The ```print()``` function also takes parameters such as the ```sep``` and ```end``` parameters, which overrides the default separator with the specified separator and the end of line character.
        """
    )
    return


@app.cell
def _():
    print("Item 1","Item 2", sep="|")
    return


@app.cell
def _():
    print("This \"entire\" \t sentence is on", end=" ")
    print("one line.")
    print("hi")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The type() function takes a value or object and returns its type.
        """
    )
    return


@app.cell
def _():
    # Print and Type functions 
    print(type(3.141))
    return


@app.cell
def _():
    # Print the highest value using the max() function. This is a function within a function.
    print(max(1,10,3,4,5))
    return


@app.cell
def _():
    # Print the longest word. Note that the len function is applied to each item 
    #   in the list and the high number is returned.
    words = ['apple', 'court', 'banana','z'] # words is a list. See the Data Structures section in Part 3.
    print(max(words))
    print(max(words, key=len))
    return


@app.cell
def _():
    #Display the number of characters (including the white space) in "Hello, world!"
    len('Hello, world!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        To obtain input from the user, use the input() function.
        """
    )
    return


@app.cell
def _():
    user_name = input("What is your name?")
    print("Hi, ", user_name)
    return


@app.cell
def _():
    user_age = input("How old are you?")
    print(user_age, type(user_age))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Type Converstion Functions

        Python includes functions to convert values from one data type to another. 

        For example, when requesting a number value from a user you may need to convert the resulting string input to an number type such as int.
        """
    )
    return


@app.cell
def _():
    # Input values are strings. Convert strings to appropriate number type, if necessary.
    # Enter decimal value....error.

    tirepressure = int(input("Input current tire pressure:"))

    if tirepressure < 32:
        print("Add air to tire.")
    else:
        print(f"At {tirepressure} psi the tire does not require additional air pressure.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Misc Functions
        Below are common functions and explanations of how they work and when you might use them.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Accessing functions in modules

        One of the strengths of the Python language is the large number of modules available to it. To add functionality to your program, you make modules available using the import keyword. Below we import the math module and the random module.

        """
    )
    return


@app.cell
def _():
    # Get colume of a sphere using radius (r)

    import math

    def get_sphere_volume(r):
        """Returns volume of a sphere given the radius (r)."""
    
        #Use the pi constant from the math module 
        volume = (4/3) * math.pi * r**3
        return volume
    return get_sphere_volume, math


@app.cell
def _(get_sphere_volume):
    #Call the function to find the volume of a sphere with a radius of 2.
    get_sphere_volume(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Generating random numbers
        To generate random numbers, use the random module. Note that this module is not designed for cryptographic use. 
        """
    )
    return


@app.cell
def _():
    # NameError if random module is not imported
    import random


    # Print 10 numbers between 1 and 100 (inclusive)
    for x in range(10):
        print(x,random.randint(1,101))
    return (random,)


@app.cell
def _(random):
    help(random.randint)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Finding the slope of a line

        Using the numpy polyfit function, np.polyfit(), you and find and return the slope and intercept of a given line with the set of coordinates of a line defined as arrays.

        The following code uses the np.polyfit() function to calculate the slope of a given line in Python.
        """
    )
    return


@app.cell
def _():
    import numpy as np
    x_1 = [1, 2, 3, 4, 5, 6]
    y = [100, 110, 120, 110, 150, 170]
    slope, intercept = np.polyfit(x_1, y, 1)
    print(f'The slope is {slope}, and the intercept is {intercept}.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Creating your own Functions
        Use the def keyword to define custom functions. Empty parentheses following the function name indicate the function takes no arguments.
        """
    )
    return


@app.function
def print_lyrics():
    """ Prints lumberjack lyrics. How cool! """
    print("I'm a lumberjack and I'm okay")
    return "something else"


@app.cell
def _(els):
    def sum(a, b):
        if a == 2:
            return 7
        elif b == 3:
            return 10
        els
        c = a + b
        return c * 3
    y_1 = sum(2, 3)
    print(y_1)
    return (sum,)


@app.cell
def _():
    x_2 = print_lyrics()
    return (x_2,)


@app.cell
def _(x_2):
    type(x_2)
    x_2
    return


@app.cell
def _():
    def repeat_lyrics():
        print_lyrics()
        print_lyrics()
    
    repeat_lyrics()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Docstrings
        Docstrings (documentation strings) provide a helpful and convenient method of
        displaying documentation with Python modules, functions, classes, and methods. 

        An object's docsting is defined by including a string constant as the first
        statement in the object's definition and can be viewed by calling help(function).
        """
    )
    return


@app.cell
def _():
    help(print_lyrics)
    return


@app.cell
def _():
    print('hi')
    print("""

    hi""")
    return


@app.cell
def _(print_stuff):
    help(print_stuff)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Passing values
        Functions defined with arguments accept values. 
        """
    )
    return


@app.cell
def _():
    def print_stuff(mystuff):
        """ Prints the string passed to it.
            Takes a single string argument.
    
        """
        print(mystuff)
        return mystuff*5

        # I put this here so it would print neat stuff
    newstuff = "really cool stuff"
    print_stuff()
    return (print_stuff,)


@app.cell
def _(print_stuff):
    x_3 = print_stuff('hello')
    return (x_3,)


@app.cell
def _(x_3):
    print(x_3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Optional arguments
        The parameter in the previous function is required. Attempting to run the function without the parameter results in an error.

        In addition to required positional arguments, Python allows optional arguments. All required positional arguments must precede optional arguments.
        """
    )
    return


@app.cell
def _():
    def print_stuff_1(my_stuff='no stuff'):
        print(my_stuff)
    print_stuff_1()
    return (print_stuff_1,)


@app.cell
def _(print_stuff_1):
    print_stuff_1('goodwill stuff')
    return


@app.cell
def _():
    # Function using keyword and default arguments
    def calc_tip(amount, percentage=.10):
        """ Calculate a tip based on an amount. 15% is default. """
        tip = amount * percentage
        return tip

    my_tip = calc_tip(55,.20)

    print(my_tip)
    return (calc_tip,)


@app.cell
def _(calc_tip):
    print(calc_tip(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### \*args and \*\*kwargs
        The \* symbol (by convention \*args) enables a variable number of positional arguments to be passed to a function. 
        """
    )
    return


@app.cell
def _(sum):
    # Passing a variable number of parameters
    def print_grades(*args):
        number_of_grades = len(args)
        print(f"length = {number_of_grades}")
        sum_of_grades = sum(args)
        avg_grade = sum_of_grades/number_of_grades
        print(args, type(args))
        print(f"Average grade = {avg_grade}")
    
    print_grades(88,99,56,100,92,100,0)
    return (print_grades,)


@app.cell
def _(print_grades):
    print_grades(88,82,99,97,89,100,84,96,92,92,90)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Using ```*args``` is by convention, not by requirement. Though others might expect to see it, so it may be useful to stick with the convention.
        """
    )
    return


@app.cell
def _(sum):
    def print_grades_1(*grades):
        number_of_grades = len(grades)
        sum_of_grades = sum(grades)
        avg_grade = sum_of_grades / number_of_grades
        print(grades)
        print(f'Average grade = {avg_grade}')
    print_grades_1(88, 99, 56, 100, 92)
    print_grades_1(88, 82, 99, 97, 89, 100, 84, 96, 92, 92, 90)
    return


@app.cell
def _():
    def print_grades_2(*grades):
        for grade in grades:
            print(grade)
            if grade == 100:
                print('Wow, a perfect score!!')
    print_grades_2(88, 99, 56, 100, 92)
    return (print_grades_2,)


@app.cell
def _(print_grades_2):
    print_grades_2(88, 82, 99, 97, 89, 100, 84, 96, 92, 92, 90)
    return


@app.cell
def _():
    def print_grades_3(*grades):
        for grade in grades:
            print(grade)
    print_grades_3(88, 99, 56, 100, 92)
    grades = input('Enter grades separated by a comma:')
    grades = grades.split(',')
    print_grades_3(*grades)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Using **kwargs
        The \*\* symbol (by convention \*\*kwargs) enables a variable number of *key word* arguments to be passed to a function.
        """
    )
    return


@app.cell
def _():
    # Passing a variable number of parameters
    def show_grades(**kwargs):
    
        print(f"kwargs = {kwargs}")
    
        print("Student - Grade")
        for key, value in kwargs.items():
            print(f"{key} - {value}")
        print() #blank line

    show_grades(Alice=[88,100],Joe=99,Jevontae=56,Subha=100,Kelly=92)
    return (show_grades,)


@app.cell
def _(show_grades):
    show_grades(Stewart=100,Mark=105,Joe=95,Eric=75)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## What is the Dot Operator?
        Just about everything in Python is an object. The dot operator enables you to access attributes (statements) and methods (function) associated with the object. 

        Press <TAB> after a dot to see a list of methods and properties associated with the object.

        In the following code, a dot operator is used to access the pi property of the math object:
        ```Python
        <a_python_object.do_something()>
        - or -
        <a_python_object.access_an_attribute>

        # Attribute example:
        volume = (4/3) * math.pi * r**3

        # Method example:
        print("Hello".upper())
        ```
        """
    )
    return


@app.cell
def _(math):
    r =5
    volume = (4/3) * math.pi * r**3

    print(f"volume = {volume}")
    return


@app.cell
def _():
    # Using the upper() method on a string via the dot operator
    print("Hello!".upper())
    return


@app.cell
def _(math):
    #What other functions are available in the math module? Use the dir() function to list a directory of math attributes.
    dir(math)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Lambda/Anonymous functions
        A lambda function, also called an anonymous function, behaves like a regular function, but is declared as a single-line function with no name (hence the term 'anonymous'). It can have any number of arguments, but only one expression.
        """
    )
    return


@app.cell
def _():
    # Regular function calc_tip
    def area_circle(r):
        """ Calculate the area of a circle. """
        area = 3.1415927 * r * r
        return area

    area_circle(4)
    return


@app.cell
def _():
    # lambda version of area_circle()
    #   To use the anonymous function, set it equal to a variable  
    get_area = lambda x: 3.1415927 * x
    get_area(4)
    return


@app.cell
def _():
    # Using lambda inline
    customers = ['Will Hawkins', 'Stewart Pickard', 'John Davis Roberts', 'Will Roberts', 'Eric Devlin', 'R. Joe Bechtold']

    # Key is the sorting critera, split on the space, get the last element, convert it to lowercaseand then sort the list
    customers.sort(key=lambda x: x.split(" ")[-1].lower())

    # Print the newly sorted list
    print(customers)
    return


@app.cell
def _():
    # Even or odd example
    (lambda x: x % 2 and 'odd' or 'even')(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Void and Return Functions
        Functions that do not return values are called void functions.
        """
    )
    return


@app.cell
def _():
    def addtwo(a,b):
        """ Returns the sum of two numbers."""
        added = a + b
        return added

    z = addtwo(1,2) * 10
    print("hi")
    return addtwo, z


@app.cell
def _(z):
    print(z)
    return


@app.cell
def _(addtwo):
    print(addtwo(3,5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## strptime and strftime functions
        ```strptime``` is short for *parse time* while the ```strftime``` function means is *formatting time*. Both are part of the Python ```datetime``` module though ```strftime``` is also part of the ```date``` and ```time``` modules also.

        ```strptime``` is the opposite of ```strftime``` though they use, conveniently, the same formatting specification, which can be found here (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

        ```strptime``` parses a string and outputs a ```datetime``` object.

        For example, say you inherited a database where the date was stored as an integer in the format YYYYMMDD, aka 20230131. To analyze these values, you'll need to convert them from a integer to a ```datetime``` object using ```strptime```.
        """
    )
    return


@app.cell
def _():
    from datetime import datetime

    int_date = 20230131

    date_obj = datetime.strptime(str(int_date), "%Y%m%d")
    date_obj
    return date_obj, datetime


@app.cell
def _(date_obj):
    date_obj.strftime("%Y-%m-%d")
    return


@app.cell
def _(datetime):
    year = datetime.now().strftime("%Y")
    print("year:", year)

    month = datetime.now().strftime("%m")
    print("month:", month)

    day = datetime.now().strftime("%d")
    print("day:", day)

    time = datetime.now().strftime("%H:%M:%S")
    print("time:", time)

    date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print("date and time:",date_time)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using datetime functions
        """
    )
    return


@app.cell
def _():
    from datetime import datetime, date

    founded = date(1831, 4, 18)
    days_ago = date.today() - founded

    print(f"The University of Alabama was founded {days_ago.days:,} days ago!")
    return (datetime,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Magic functions


        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # TimeIt magic function
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Environment variables
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        env_name = %env CONDA_DEFAULT_ENV
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        print(env_name)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        env_dict = %env
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        env_dict # All environemnt information
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        env_dict['PWD'] # Get the working directory
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        %env
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # String Operations
        Text in Python is represented by a string. A string is an immutable array of unicode characters. This means that once defined, they cannot be changed. You can access (but not change) characters one at a time using the bracket [] operator.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Strings are arrays
        Because strings are stored as an array, you may access characters using array notation.
        """
    )
    return


@app.cell
def _():
    x_4 = 'Guardians of the Galaxy Vol. 1'
    print(x_4[0:6])
    return (x_4,)


@app.cell
def _(x_4):
    print(x_4[-5:])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Strings are immutable
        However, like tuples strings cannot be changed.
        """
    )
    return


@app.cell
def _(x_4):
    print(x_4[29])
    x_4[29] = '2'
    return


@app.cell
def _():
    x_5 = 'Guardians of the Galaxy Vol. 2'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Escape characters and raw strings
        Prefix a string with ‘r’ or ‘R’ to force Python to treat backslash (\) as a literal character.
        E.g., Windows file paths

        | Escape Character | Prints as |
        |------------------|-----------|
        | \\' | Single quote
        | \\" | Double quote
        | \\t | Tab
        | \\n | Newline (line break)
        | \\ | Backslash


        """
    )
    return


app._unparsable_cell(
    r"""
    # Error - unexpected escape characters
    file_path = \"c:\users\gregb\documents\python_projects\"
    print(file_path)
    """,
    name="_"
)


@app.cell
def _():
    # Escaping backslash for file name
    file_path = "c:\\users\\gregb\\documents\\python_projects"
    print(file_path)
    return


@app.cell
def _():
    file_path_1 = 'c:\\users\\gregb\\documents\\python_projects'
    print(file_path_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using single, double, and triple quotes
        You may use either single, double, or triple quotes. Use double or triple quotes when a string contains a single apostrophe, double apostrophe or both.
        """
    )
    return


@app.cell
def _():
    #Single quotes specify a string.
    howdy = 'hello, world!'
    print(howdy)
    return (howdy,)


@app.cell
def _():
    #Double quotes also specify a string.
    statement = "I'm a Python programmer."
    print(statement)
    return


@app.cell
def _():
    # Triple quotes specify a string AND can span lines.
    prov_12_16 = """A fool's annoyance is known at once,
    but the prudent overlooks an insult."""
    print(prov_12_16)
    return


@app.cell
def _():
    #To print quotes, you can use the escape character (\)
    as_good_as_it_gets = 'Sell crazy someplace else. We\'re all stocked up here.'
    print(as_good_as_it_gets)
    return


@app.cell
def _():
    #Triple quotes are helpful when you want to display single or double quotes within a string without using an escape character.
    cannoli = """Clamenza said, \"Leave the gun, take the cannoli.\" It's one of my 'fav' movie quotes. """
    print(cannoli)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## String Capitalization
        """
    )
    return


@app.cell
def _(howdy):
    # Capitalize the first word
    print(howdy.capitalize())
    return


@app.cell
def _(howdy):
    # Capitalize each word
    print(howdy.title())
    print("this is title case".title())
    return


@app.cell
def _(howdy):
    # Capitalize each word
    print(howdy.upper())
    print("this is all capps".upper())

    #Use upper() to compare strings ignoring case
    myfavfruit = "Kiwi"

    if myfavfruit.upper() == "KIWI":
        print("That's my fav!")
    else:
        print("Not my fav")
    return


@app.cell
def _():
    book_title = "THE UNOFFICIAL GUIDE TO ETHICAL HACKING"

    # Lowercase
    print(book_title.lower())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## String Concatenation

        Use the '+' operator to join strings.
        """
    )
    return


@app.cell
def _():
    first_name = "Gregory"
    middle_initial = "J"
    last_name = "Bott"

    full_name = first_name + " " + middle_initial + " " + last_name + ", Ph.D."
    print(full_name)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Removing white space
        A common task when working with data is to remove white space (spaces, tabs, newlines) from the beginning and end of a string. To remove white space use the **strip** methods:

        ```Python

        strip()
        lstrip()
        rstrip()

        ```


        """
    )
    return


@app.cell
def _():
    # value is preceded by three tabs and followed by a line break
    data_column = "\t\t\t     100.00           \n"
    print(f"Before stripping, the data_column string {data_column} is {len(data_column)} characters long.\n")
    print(f"After using the lstrip(), the data_column string {data_column.lstrip()} is {len(data_column.lstrip())} characters long.\n")
    print(f"After using the rstrip(), the data_column string {data_column.rstrip()} is {len(data_column.rstrip())} characters long.\n")
    print(f"After using the strip(), the data_column string {data_column.strip()} is {len(data_column.strip())} characters long.\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Format Operator
        To substitute values from variables or functions into a string, use the *format operator* %. 

        Do not confuse % with modulus operator. In the statement, 4 % 2 = 0 '%' is the modulus operator. 

        Instead of using the % operator between integers as in the modulus operator, the *format operator* is used within a string.
        <br>%d = signed integer decimal
        <br>%s = string
        <br>%f = float

        For more conversion types, go to https://docs.python.org/3/library/stdtypes.html#old-string-formatting
        """
    )
    return


@app.cell
def _():
    b_of_b_on_wall = 5
    beverage = "beer"

    for bottle_num in range(5,0,-1):
        print("%d bottles of %s on the wall, %d bottles of %s." % (bottle_num, beverage, bottle_num, beverage))
        print("Take one down and pass it around, %d bottles of %s on the wall." % (int(bottle_num)-1, beverage))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using str.format()
        The format operator is a good option, but when you have multiple placeholders in a string, code becomes less readable. 

        One advantage of the str.format() method is that you can use the replacement fields in any order. Simply use their index values.
        """
    )
    return


@app.cell
def _():
    name = "Greg"
    age = "82"

    print("Hello, {}. You are {}.".format(name, age))
    return


@app.cell
def _():
    name_1 = 'Greg'
    age_1 = '82'
    print('Hello, {1}. You are {0}.'.format(age_1, name_1))
    return


@app.cell
def _():
    # Formatting numbers
    print("You won ${:,.4f}".format(312.57))
    return


@app.cell
def _():
    # Use dictionary values
    person = {'name': 'Greg', 'age': 82}
    print("Hello, {name}. You are {age}.".format(**person))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using f-Strings
        Beginning with Python 3.6, you can use f-strings ("formatting string literals") to embed expressions in strings. The syntax for f-Strings is similar to str.format() but results in more readable code. Use the curly braces to enclose expressions that should be evaluated within the string.
        """
    )
    return


@app.cell
def _():
    name_2 = 'Greg'
    age_2 = '82'
    print(f'Hello, {name_2}. You are {age_2}.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Formatting f-strings
        You can also format integers and floats within f-strings. Include a separator and specify the number of decimal places to print.
        """
    )
    return


@app.cell
def _(math):
    formatted_pi = f"Value of pi: {math.pi:.8f}"
    print(formatted_pi)

    lottery_value = 12000000

    print(f'The lottery has reached ${lottery_value:,.2f}!')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Currency and date formatting functions
        Because currency and date formats vary by locale, a recommended way of formatting currency and dates is to use the ```locale``` module. The ```locale``` module accesses the region-specific symbols for date and currency rules configured in your operating system and applies it to the value format.

        ```Python
        currency = "${:,.2f}".format(amount)
        ````
        """
    )
    return


@app.cell
def _():
    import locale

    # Set the desired locale (e.g., US)
    locale.setlocale(locale.LC_ALL, '')

    # Define the float value
    amount = 1234.56789

    # Format the float as currency
    formatted_amount = locale.currency(amount)

    print(f" USD = {formatted_amount}")
    return


@app.cell
def _():
    amount_1 = 1233.673477
    currency = '${:,.4f}'.format(amount_1)
    print(currency)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Splitting and Joining strings
        """
    )
    return


@app.cell
def _():
    # Below is a database record exported using the pipe symbol ("|") to seprate fields
    exported_record = "Quin J. Alford|Proin Company|Ap #664-5782 Felis St.|Butte|35565|MT|-72.72653, -167.07764|4716 4071 8086 1415|436|eu@pellentesque.net"
    print("original data:")
    print(exported_record)
    print()

    #Split the data at each pipe symbol. The result of the split function is a Python list (essentially an array)
    exported_record = exported_record.split("|")
    print("converted to a list: ")
    print(exported_record)
    print()
    return (exported_record,)


@app.cell
def _(exported_record):
    #Print the first and last member of the list. Acess the first element (element 0), and the last element (-1).
    #The second to last element would be accessed using [-2].
    print("Name: " + exported_record[0], "   email: " + exported_record[-1] +"\n")

    #Join the list by comma and store in exported_record
    exported_record_csv = ",".join(exported_record)
    print(exported_record_csv)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Find() method for strings
        """
    )
    return


@app.cell
def _():
    gburg_text = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."

    #Find first instance of a word, find(value, start default = 0, end default = end of string)
    find_pos = gburg_text.find("score")
    print(find_pos)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
