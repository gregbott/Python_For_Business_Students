import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Python Fundamentals

        Prepared by:**Gregory** J. Bott, Ph.D.
        (Sources: Dr. Nick Freeman, Python for Everyone, Charles Severance; A Whirlwind Tour of Python, Jake Vanderplas)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Why should a business student learn Python?

        Information is the lifeblood of <del>nearly</del> every organization. The purpose of this notebook is the help business students master the fundamental concepts and skills required to effectively use Python. Python skills are in high demand. One reason for this demand is Python's ability to efficiently acquire, manipulate, analyze and visual data. However, prior to performing data analytic tasks, business students must learn the fundamentals.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Data Analysis is Part of *Every* Job
        It's not just data scientists or data analytics that need analysis skills. Nearly every job intersects with data. It's highly likely that even if your job doesn't have "analyst" or "scientst" in the title, you'll still benefit from understanding how to acquire, handle, manipulate, and report data.

        > ### Deloitte: "...skills that were highly appreciated in Deloitte and projects were Java, Python/R..."

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Python skills are in high demand

        2021 Developer Survey by StackOverflow

        ![](./images/MostWantedLanguages.jpg)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Programming Teaches Problem solving

        The ability to think critically and solve problems is a general life skill. Proble solving applies to the all facets of life. In this course you'll learn Python syntax and structures, but more importantly you'll learn to abstract a problem and code a solution. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Python is the new Excel
        Business rightly assume that you have solid Excel skills. However, the new expectation is that you already possess the skills necessary to handle data acquisition, analysis, and visualization. And alothough this can arguably still be done in Excel, Python's tools and libraries are exponentially more efficient. 

        Python is the new Excel. (see https://www.fincad.com/blog/python-new-excel)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## About the Python language
        (Sources: Wikipedia, Dr. Nickolas K. Freeman)

        >Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, and a syntax that allows programmers to express concepts in fewer lines of code, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.

        >Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of its features support functional programming and aspect-oriented programming (including by metaprogramming and metaobjects (magic methods)). Many other paradigms are supported via extensions, including design by contract and logic programming.

        >The language's core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:

        > - Beautiful is better than ugly
        > - Explicit is better than implicit
        > - Simple is better than complex
        > - Complex is better than complicated
        > - Readability counts

        > Rather than having all of its functionality built into its core, Python was designed to be highly extensible. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, another programming language that espoused the opposite approach.

        > While offering choice in coding methodology, the Python philosophy rejects exuberant syntax (such as that of Perl) in favor of a simpler, less-cluttered grammar. As Alex Martelli put it: "To describe something as 'clever' is not considered a compliment in the Python culture." Python's philosophy rejects the Perl "there is more than one way to do it" approach to language design in favor of "there should be one—and preferably only one—obvious way to do it".

        >Python's developers strive to avoid premature optimization, and reject patches to non-critical parts of CPython that would offer marginal increases in speed at the cost of clarity. When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter.

        >An important goal of Python's developers is keeping it fun to use. This is reflected in the language's name—a tribute to the British comedy group Monty Python—and in occasionally playful approaches to tutorials and reference materials, such as examples that refer to spam and eggs (from a famous Monty Python sketch) instead of the standard foo and bar.

        >A common neologism in the Python community is *pythonic*, which can have a wide range of meanings related to program style. To say that code is pythonic is to say that it uses Python idioms well, that it is natural or shows fluency in the language, that it conforms with Python's minimalist philosophy and emphasis on readability. In contrast, code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.

        >Users and admirers of Python, especially those considered knowledgeable or experienced, are often referred to as Pythonists, Pythonistas, and Pythoneers
        # What is a Program?

        > ## A program is a sequence of instructions that specified how to perform a computation. 

        ## Building Blocks of Nearly Every Language
        * **input** - get data--from user via keyboard, from sensors, from other programs, from databases, etc.
        * **output** - display results in the console on the screen, on paper, to another program, a web page, etc.
        * **math** - perform mathematical operations (addition, multiplication, etc.)
        * **conditional execution** - check for certain values or states and run the appropriate code
        * **repetition** - repeatedly perform some action a certain number of times
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Python is interpreted, not compiled.
        Programming languages generally fall into one of two categories: Compiled or Interpreted. With a compiled language, code you enter is reduced to a set of machine-specific instructions before being saved as an executable file. With interpreted languages, the code is saved in the same format that you entered. Compiled programs generally run faster than interpreted ones because interpreted programs must be reduced to machine instructions at runtime. However, with an interpreted language you can do things that cannot be done in a compiled language. For example, interpreted programs can modify themselves by adding or changing functions at runtime. It is also usually easier to develop applications in an interpreted environment because you don't have to recompile your application each time you want to test a small section. (source: http://www.vanguardsw.com/dphelp4/dph00296.htm)
        <br>

        ![image](images/python_interpreted.png)

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Setting Up Your Environment and Getting Started
        <a id="Setting_up_your_environment"> </a>


        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Installing Anaconda
        Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing that aims to simplify package management and deployment. Package versions are managed by the package management system conda. (source: Wikipedia) The Spyder IDE is one of packages included in Anaconda.

        **Miniconda** provides the Python interpreter and the conda package manager. If you don't want the preinstalled packages that come with Anaconda, you can install Miniconda and install the packages you want yourself.

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Starting Jupyter Lab

        If you wish to control the starting folder (home folder) of Jupyter Lab, then following these instructions.

        1. Open Anaconda Prompt
        2. Navigate to starting folder (e.g., cd G:).
        3. Type ```jupyter lab``` and press ENTER
           > <b>Note: The Home Folder is the starting folder of the Anaconda prompt.</b>
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Choosing a Python IDE

        ### Jupyter Notebook and Jupyter Lab
        Jupyer Notebook and Lab are the best IDEs for learning and documenting Python code. They are also a solid method to provide Python code and results to non-Python programmers. We will make extensive use of Jupyter Lab in this course.

        ### Spyder
        Spyder is a simple IDE that is useful for learning Python. It is included with the install of Anaconda and supported in this course. You may find Spyder the best choice for completing assignments. If an automatic grading environment is being used, you may find it faster to write, debug, and test code in Spyder and then paste it into the automatic grading environment.

        ### VS Code
        Visual Studio Code is also available with Anaconda, though it is not installed by default. VS Code is perhaps the best overall choice for an IDE, however, Spyder offers a more straightforward initial user experience for the beginner. 

        ### Sublime Text
        A highly functional and extensible text editor often used by Pythonistas.

        ### PyCharm
        If you would like an IDE with a deep feature set, Pycharm is a good choice. They offer special licensing for academia.

        You are welcome to use any of these IDEs for this class. You are also welcome to use a different IDE, but we cannot support all IDEs, so if you choose an IDE besides these two, we'll give you best effort support, but you may be on your own making a different IDE work.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Notebook Basics

        As with any tool in your professional arsenal, you should be intimately acquainted with the IDE (Jupyter Lab in our case) features and functions.

        Some of the Jupyter Lab concepts with which you should be familiar include:
        * Command vs edit mode within a notebook
        * Differences between cell types
        * The selection and role of the kernel, restarting the kernel
        * Running a cell, an entire notebook, or a group of cells
        * Navigating, cuting, pasting, joining and separating cells
        * Common notebook keyboard shortcuts (creating, deleting, cut/copy/paste, join, split, show line numbers, etc.)
        * Locating the notebook in the file system and accessing data from the file system
        * Clear one cell output, clear all output
        * Use a console within a notebook
        * Check for package and version using console and grep
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Python Coding basics

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Python is case-sensitive
        Most components in Python are case-sensitive (e.g., statements, variable names, file names, etc.). Windows is generally case-insensitive.
        """
    )
    return


@app.cell
def _(myvar):
    # ERROR: 'myvar' is not defined (case problem)
    MyVar = 1
    print(MyVar)
    print(myvar)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Use proper indentation
        White space in many languages has little or no meaning. However, using Python, improper indentation will generate a syntax error:
        """
    )
    return


@app.cell
def _():
    # Error: statements following an if statement must be indented.
    if 4 > 1:
        print("4 is greater than 1")
        print("hi")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Comment your code

        Make a habit of clearly commenting your code...even if the purpose of the code seems obvious. Even for code you have written yourself, it is often difficult to remember why you chose to implement something in a specific way. 

        Start a comment using the hash (#) symbol 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Printing values
        You will often print output. The print() function is versatile.
        """
    )
    return


@app.cell
def _():
    # Basic usage
    print("Hello, world!")

    # Print items separated by commas (default separator is a space ' ')
    print('North','South','East','West')

    # You can specify the seprator
    print('North','South','East','West', sep='--')

    # Default end is a new line (\n), you may change that also
    print("This is the first line. ", end='')
    print("Also on same line.")

    # Print variable and concatenate
    x = 'apple'
    print(x)
    print('fuit: ' + x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Variables, Expressions, and Types

        Python is a *dynamically typed* language. A programming language is said to be dynamically typed, or just 'dynamic', when the majority of its type checking is performed at run-time as opposed to at compile-time.

        Python is also *strongly typed* as the interpreter keeps track of all variables types. Again, it's also very dynamic as it rarely uses what it knows to limit variable usage. In Python, it's the program's responsibility to use built-in functions like isinstance() and issubclass() to test variable types and correct usage. Python tries to stay out of your way while giving you all you need to implement strong type checking.

        The difference between a strongly typed language and a weakly typed language is basically that a strongly typed language checks the type of a variable before performing an operation on it, whereas a weakly typed language does not.
        [Source: Wiki.Python.org](https://wiki.python.org/moin/Why%20is%20Python%20a%20dynamic%20language%20and%20also%20a%20strongly%20typed%20language)
        """
    )
    return


@app.cell
def _():
    #Store a float in the variable a
    a = 3.141
    print(a, type(a))
    return


@app.cell
def _():
    a_1 = ['apple', 3.141, 'banana']
    print(a_1, type(a_1))
    return


@app.cell
def _():
    a_2 = 'apple'
    print(a_2, type(a_2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Variables in Python
        Variables store values. Variable names can be as long as you want, can contain letters and numbers, but must not begin with a number or be a Python keyword (e.g., true, for, from, lambda).

        > **Python is case-sensitive.** unit_cost is not the same as Unit_cost. 

        By convention variable names are lower case and use the underscore character to separate words. 

        earnings_after_tax <br>
        default_gateway
        """
    )
    return


@app.cell
def _(fruit):
    # Variables are case-sensitive --> Error
    Fruit = "apple"
    print(fruit)
    return


app._unparsable_cell(
    r"""
    # illegal -- must not start with a number
    76trombones = 0
    """,
    name="_"
)


@app.cell
def _():
    although_difficult_to_use_this_is_a_valid_variable = 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using Variables to Store User Input

        Use variables to store input from users. To get input from the user Python provides a built-in function **input** that captures input from keyboard as a string.
        """
    )
    return


@app.cell
def _():
    # Get card total from user and store in CardTotal 
    card_total = input("Card total?")
    print(f"CardTotal type is: {card_total}.")
    return (card_total,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### input() function
        Used to get data from the user. Always returns a string, so you must cast if you are working with numbers.
        """
    )
    return


@app.cell
def _(card_total):
    type(card_total)
    return


@app.cell
def _(card_total):
    # Error -- CardTotal is str
    if card_total > 21:
        print("Busted")
    else:
        print("Hit me")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Comparison operators

        You are probably already familiar with the comparison operators.
        * x and y are variable names
        ```Python
        x > y
        x >= y
        x < y
        x <= y
        x == y # Use double-equal to test for equality (single equal sign is for assignment), True if x is same as y
        x != y # test for inequality, True if x is different than y
        ```
        """
    )
    return


@app.cell
def _(card_total):
    # Must cast to appropriate value type (int)
    if int(card_total) > 21:
        print("Busted")
    else:
        print("Hit me")
    return


@app.cell
def _(card_total):
    print("Hello", "how are you?", card_total, sep="||")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Basic Data Types in Python

        ### Integers
        ---
        A number with no fractional part. 

        ![image](./images/int-number-line.svg)

        #### Includes: 
        * the counting numbers {1, 2, 3, ...}, 
        * zero {0}, 
        * and the negative of the counting numbers {-1, -2, -3, ...}

        We can write them all down like this: {..., -3, -2, -1, 0, 1, 2, 3, ...}

        Examples of integers: -16, -3, 0, 1, 198

        Integer size is limited only by your machine.
        """
    )
    return


@app.cell
def _():
    bigInt = 1234568901234568901234568901234568901234564568901234568901234568901234568901234568901234568901234568900

    print(bigInt + 1)

    print(type(bigInt))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Float type
        * Platform dependent
        * Typically equivalent to IEEE754 64-bit C double
        * Smallest float is effectively 2.225 x 10^-308
        """
    )
    return


@app.cell
def _():
    type(1.0)
    return


@app.cell
def _():
    b = 2

    print("b = {} and is type {}".format(b, type(b)))
    return


@app.cell
def _():
    b_1 = 2 * 1.1
    print('b = {} and is type {}'.format(b_1, type(b_1)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Boolean type
        ---
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        What evaluates to `True`?
        * Non-zero values
        * Non-empty data structures (lists, dicts, tuples)
        * Non-empty strings

        What evaluates to `False`?
        * Zero
        * Empty data structures
        * Empty strings
        * NoneType values (aka `None`)
        """
    )
    return


@app.cell
def _():
    false_values = [0, '', None, [], {}]

    for val in false_values:
        print(bool(val), end=", ")
    return


@app.cell
def _(is_fte):
    # Error = the boolean value must be capitalized (True, not true or TRUE)
    if is_fte == True:
        print("Full-time")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Non-zero values evaluate to ```True``` while 0 (zero) evaluates to ```False```.
        """
    )
    return


@app.cell
def _():
    hours_worked = 0
    #hours_worked = 37
    #hours_worked = 'yes'

    if hours_worked:
        print("Need to calculate payroll.")

    if not hours_worked:
        print("No hours worked or invalid value.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #### Logic Operators on boolean values
        a and b are boolean values

        ```Python
        not a # True if a is False, False if a is True
        a and b # Both a and b must be True for statement to be True
        a or b # Either a or b must be True for statement to be True
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### String Type
        A string is a sequence of characters. 

        Values enclosed within quotation marks (single, double, or triple-double) are strings.
        """
    )
    return


@app.cell
def _():
    s = 'Monty Python'
    return (s,)


@app.cell
def _(s):
    # use len() function to get the length of a string
    print(len(s))

    # Print part of a string, a slice
    print(s[0:5])

    print(s[6])
    return


@app.cell
def _(s):
    # Strings are immutable (Can't change 'Python' to 'Jython')
    s[6] = "J"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### None type

        The null keyword is available in languages such as C++ and Java. Null means empty. It is not equivalent to a zero-length string nor is it equivalent to zero (0). In Python, the None type  is the keyword equivalent to Null. None (the type) is not equivalent to the string, "None". In my humble opinion, None is more logical than null. None means the object is nothing, non-existent. 

        #### Why use None?

        When instantiating (creating) an object, you may need to check to see if the instantiation was successful or not. If the creation of the new object failed, the object will return a None type.

        ---
        """
    )
    return


@app.cell
def _():
    # None is not the "None" string. It is a class type.
    print(None == "None")
    print(type(None))
    return


@app.cell
def _(MyDatabase, db_database, db_host, db_password, db_user):
    #Source: https://www.pythoncentral.io/python-null-equivalent-none/
    database_connection = None
 
    # Try to connect (none of the variables for the connect have values...)
    try:
        database = MyDatabase(db_host, db_user, db_password, db_database)
        database_connection = database.connect()
    except:
        pass
 
    if database_connection is None:
        print('The database could not connect')
    else:
        print('The database could connect')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Complex numbers
        ---
        A Complex Number is a combination of a Real Number and an Imaginary Number. [1]

        ![image](./images/complex-example.svg)

   
        """
    )
    return


@app.cell
def _():
    print("3i is of type: " + str(type(3j)))
    print(7 + 3j)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
   
        The "unit" imaginary number (like 1 for Real Numbers) is i, which is the square root of −1.   

        ![image](./images/imaginary-square-root.svg)

        > **Except in Python, "j" is used instead of "i".**
        """
    )
    return


@app.cell
def _():
    1j * 1j == -1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Converting values between types

        Often you may need to convert from values from one type to another. For example, you may need to convert the values received from the input() function from string to an int or a float.
        """
    )
    return


@app.cell
def _():
    user_number = input("Enter a number and I'll tell you if it is even or odd:\n")
    print(type(int(user_number)))
    return


@app.cell
def _():
    #Source: https://gist.github.com/jfpuget/60e07a82dece69b011bb -- Jean-François Puget¶

    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import colors
    # '%matplotlib inline' command supported automatically in marimo


    def mandelbrot_image(xmin,xmax,ymin,ymax,width=12,height=12,maxiter=80,cmap='hot'):
        dpi = 72
        img_width = dpi * width
        img_height = dpi * height
        x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    
        fig, ax = plt.subplots(figsize=(width, height),dpi=72)
        ticks = np.arange(0,img_width,3*dpi)
        x_ticks = xmin + (xmax-xmin)*ticks/img_width
        plt.xticks(ticks, x_ticks)
        y_ticks = ymin + (ymax-ymin)*ticks/img_width
        plt.yticks(ticks, y_ticks)
    
        norm = colors.PowerNorm(0.3)
        ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm)
    
    def mandelbrot(c,maxiter):
        z = c
        for n in range(maxiter):
            if abs(z) > 2:
                return n
            z = z*z + c
        return 0

    def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        n3 = np.empty((width,height))
        for i in range(width):
            for j in range(height):
                n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter)
        return (r1,r2,n3)

    mandelbrot_image(-2.0,0.5,-1.25,1.25,maxiter=80,cmap='gnuplot2')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Order of Operations
        <a id="Setting_up_your_environment"> </a>

        The order of evaluation of expressions with more than one operator follows *rules of precedence* -- PEMDAS

        * **Parentheses**
        * **Exponentiation**
        * **Multiplication and Division**
        * **Addition and Subraction**
        * **Left to Right** - operators with the same precedence are evaluated left to right
        """
    )
    return


@app.cell
def _():
    # Exponentiation, then Multiplication
    3*1**3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Operators
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Modulo operator
        <a id="modulus_operator"> </a>

        In computing, the modulo operation finds the remainder after division of one number by another (sometimes called modulus). Given two positive numbers, a (the dividend) and n (the divisor), a modulo n (abbreviated as a mod n) is the remainder of the Euclidean division of a by n.

        """
    )
    return


@app.cell
def _():
    # Divide 7 by 3
    7/3
    return


@app.cell
def _():
    # Floor division
    7 // 3 # (2 is the quotient, 1 is the remainder)
    return


@app.cell
def _():
    # Return the remainder or modulus
    7 % 3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Assignment vs. Comparison
        ---
        In Python, assignment of a value to a variable is accomplished using a single equal sign. 

        Comparison is performed using a double equal sign.

        """
    )
    return


@app.cell
def _():
    x_1 = 7
    print(x_1)
    x_1 = 1000
    print(x_1)
    return (x_1,)


@app.cell
def _(x_1):
    if x_1 == 7:
        print('Lucky Seven')
    else:
        print('You lose!')
    return


@app.cell
def _():
    # Error when adding string and integer
    userinput = "5"

    sum = 7 + int(userinput)
    print(sum)
    return (userinput,)


@app.cell
def _(userinput):
    sum_1 = 7 + int(userinput)
    print('sum = {}'.format(sum_1))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        [1]: Source: https://www.mathsisfun.com
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Variable Scope - LEGB
        When using variables, you must understand its scope. By scope we are referring the visibility of variables--in which parts of your program can access or change the variable. For example, if a variable is global, every part of your program can access it. However, variables used within a function should generally not be available outside the function.

        Python looks for variables in this order:
        * Local
        * Enclosing
        * Global
        * Built-in
        """
    )
    return


@app.cell
def _():
    # Local scope

    y = "outside of function"

    def my_function():
        y = "inside function scope" # y is local to function--not available after function ends
        print(y)

    my_function()

    print(y) # Prints enclosed y variable
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Conditional Execution

        In Python, use the if statement to perform decision-making by allowing conditional execution of a statement or group of statements based on the value of an expression.

        Remember that Python requires indentation to designate the start and end of code blocks. 

        <condition> has a value of True or False

        ```Python
        if <condition>:
            <expression>
            <expression>
        ``` 
        """
    )
    return


@app.cell
def _():
    CardTotal = 22
    if CardTotal > 21:
        print("busted!")
    return


@app.cell
def _():
    deal_again = input("deal again?")
    if deal_again == 'yes':
        print("dealing again...")
        # code here that deals again...
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Conditionals with multiple expressions
        The ```if``` statement may be follwed by an ```else``` clause. The ```else``` clause will only be excecuted when the ```if``` statement evaluates to ```False```.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You can use an ```if...else``` statement to execute a set of statements based on whether the value of a variable is even or odd.

        ![image](\images\if-then-elselogic.jpg)

        The basic if statement form:

        ```Python
        if expr:
            ''statement''
        else:
            ''statement''
        ```
        """
    )
    return


@app.cell
def _():
    x_2 = 9
    if x_2 % 2 == 0:
        print('x is even')
    else:
        print('x is odd')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Logical Operators
        """
    )
    return


@app.cell
def _():
    shave = True
    haircut = False

    if shave and haircut:
        print("You know the secret knock!")
    else:
        print("You're not one of us.")
    return


@app.cell
def _():
    shave_1 = False
    haircut_1 = True
    if shave_1 or haircut_1:
        print('You know the secret knock!')
    else:
        print("You're not one of us.")
    return


@app.cell
def _():
    #BOTH statements must be true to satisfy the statement and print True
    if 1 < 10 and -2 > -7:
        print(True)
    else:
        print(False)
    return


@app.cell
def _():
    #Only ONE expression must be true to satisfy the statement and print True
    if 100 < 10 or -2 > -7:
        print(True)
    else:
        print(False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Chained Conditionals

        If more then two possibilities exist, one way to programmatically express this is using elif.
        """
    )
    return


@app.cell
def _():
    x_3 = 8
    y_1 = 5
    if x_3 > y_1:
        print('x is greater than y')
    elif y_1 > x_3:
        print('y is greater than x')
    else:
        print('x and y are equal')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Nested Conditionals

        You can also nest one conditional inside another conditional. Consider the previous example:
        """
    )
    return


@app.cell
def _():
    x_4 = 2
    y_2 = 3
    if x_4 == y_2:
        print('x and y are equal')
    elif x_4 < y_2:
        print('x is less than y')
    else:
        print('x is greater than y')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Grouping comparison operators
        Comparison operators can be grouped.
        """
    )
    return


@app.cell
def _():
    x_5 = 111
    if 0 < x_5 < 10:
        print('x is a positive single-digit number')
    elif x_5 < 0:
        print('x is a negative number')
    elif x_5 >= 10:
        print('x is a positive two-digit number')
    return


@app.cell
def _():
    x_6 = 1
    y_3 = 2
    z = 6
    if x_6 < y_3 < z:
        print(x_6)
        print(y_3)
        print(z)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Operators and Operands
        <a id="operators_and_operands"> </a>
        Operators are special symbols that represent computations like addition and multiplication. The values the operator is applied to are called operands.
        The operators +, -, *, /, and ** perform addition, subtraction, multiplication, division, and exponentiation, as in the following examples:

        """
    )
    return


@app.cell
def _():
    #Addition and subtraction
    20+33-10
    return


@app.cell
def _():
    # Five squared
    5**2
    return


@app.cell
def _():
    # Multiplication
    (3+2)*(9+2)
    return


@app.cell
def _():
    # Division
    100/25
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Iteration (looping)
        Computers are very good and doing repetitive tasks. You will use iteration for many operations in Python. For example, you may loop through records in a database or examine lines in text file. 

        Two methods for iterating are the While statement and the For loop. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## While statement

        Computers are well-suited to repeat operations very quickly. Use the While statement to repeat a series of steps until a condition is met. Use when the number of iterations is not known.

        ```Python
        while <condition>:
            <expression>
            <expression>
            ...
        ```
        """
    )
    return


@app.cell
def _():
    n = 0
    while n < 7:
        print("day " + str(n))
        n = n + 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## For Loop
        Use the For Loop when you have a specific number of iterations or you are iterating through a collection of items (e.g., lines in a text file).

        ```Python
        for <variable> in range(<value>):
            <expression>
            <expression>
            ...
        ```

        * On first loop, <variable> starts with smallest value
        * On each loop, <variable> is incremented (or decremented if negative step)
        * At <value> - 1, loop is complete
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Range Function

        ```Python
        range(start, stop, step)
        ```
        Default values: start = 0, step = 1

        Range increments until value is stop - 1.
        """
    )
    return


@app.cell
def _():
    for x_7 in range(11):
        print(x_7, end=' ')
    return


@app.cell
def _():
    for x_8 in range(10, 0, -1):
        print(x_8, end=' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        A counter variable can be used in either the For Loop or the While loop, but the counter variable must be initialized prior to its use.
        """
    )
    return


@app.cell
def _():
    z_1 = 0
    for y_4 in range(1, 11):
        z_1 = z_1 + 1
        print(z_1, end=' ')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Looping through items

        In addition to using the ```range()``` function or the ```while``` statement, you can also loop through a collection of objects such as the files in the working directory. Note that we do not need to obtain the number of items (files, in this case) present in the collection (folder). We simply ask Python to iterate through them.
        """
    )
    return


@app.cell
def _():
    import os
    files = os.listdir()
    for x_9 in files:
        print(x_9)
    return (os,)


@app.cell
def _(os):
    root_folder = os.path.expanduser('~')
    for root, dirs, files_1 in os.walk(root_folder):
        for name in files_1:
            print(os.path.join(root, name))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Break, Continue and Pass statements
        """
    )
    return


@app.cell
def _():
    total_loops = 0
    for x_10 in range(1, 101):
        for y_5 in range(1, 6):
            total_loops = total_loops + 1
            if y_5 == 5:
                break
    print(x_10, y_5, 'total loops = ', total_loops)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Break
        Use the ```break``` statement to exit a loop. Break exits the current loop, so if you have a nested loop and wish to exit both, you'll need to provide two break statements, one for each loop.
        """
    )
    return


@app.cell
def _():
    for num in range(1,11):
        if num == 7:
            break
        print(num)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Continue
        Use the ```continue``` statement to interrupt and then resume processing in a loop. Note that the print() function is not called when num equals 7.
        """
    )
    return


@app.cell
def _():
    for num_1 in range(1, 11):
        if num_1 == 7:
            continue
        print(num_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Pass
        """
    )
    return


@app.cell
def _():
    for num_2 in range(1, 11):
        if num_2 == 7:
            pass
        print(num_2)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
