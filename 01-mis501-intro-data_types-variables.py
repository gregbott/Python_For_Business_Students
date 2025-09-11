import marimo

__generated_with = "0.15.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/01-Core Python-Variables-Iteration-Conditionals.slides.json",
)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Python Fundamentals""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## About the Python language
    (Sources: Wikipedia)

    >Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, and a syntax that allows programmers to express concepts in fewer lines of code, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.

    >Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of its features support functional programming and aspect-oriented programming (including by metaprogramming and metaobjects (magic methods)). Many other paradigms are supported via extensions, including design by contract and logic programming.
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    >The language's core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:

    > - Beautiful is better than ugly
    > - Explicit is better than implicit
    > - Simple is better than complex
    > - Complex is better than complicated
    > - Readability counts
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    > Rather than having all of its functionality built into its core, Python was designed to be highly extensible. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, another programming language that espoused the opposite approach.

    > While offering choice in coding methodology, the Python philosophy rejects exuberant syntax (such as that of Perl) in favor of a simpler, less-cluttered grammar. As Alex Martelli put it: "To describe something as 'clever' is not considered a compliment in the Python culture." Python's philosophy rejects the Perl "there is more than one way to do it" approach to language design in favor of "there should be one—and preferably only one—obvious way to do it".

    >Python's developers strive to avoid premature optimization, and reject patches to non-critical parts of CPython that would offer marginal increases in speed at the cost of clarity. When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter.

    >An important goal of Python's developers is keeping it fun to use. This is reflected in the language's name—a tribute to the British comedy group Monty Python—and in occasionally playful approaches to tutorials and reference materials, such as examples that refer to spam and eggs (from a famous Monty Python sketch) instead of the standard foo and bar.

    >A common neologism in the Python community is *pythonic*, which can have a wide range of meanings related to program style. To say that code is pythonic is to say that it uses Python idioms well, that it is natural or shows fluency in the language, that it conforms with Python's minimalist philosophy and emphasis on readability. In contrast, code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.

    >Users and admirers of Python, especially those considered knowledgeable or experienced, are often referred to as Pythonists, Pythonistas, and Pythoneers
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # What is a Program?

    > A program is a sequence of instructions that specified how to perform a computation. 

    ## Building Blocks of Nearly Every Language
    * **input** - get data--from user via keyboard, from sensors, from other programs, from databases, etc.
    * **output** - display results in the console on the screen, on paper, to another program, a web page, etc.
    * **math** - perform mathematical operations (addition, multiplication, etc.)
    * **conditional execution** - check for certain values or states and run the appropriate code
    * **repetition** - repeatedly perform some action a certain number of times
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Python is classified as an interpreted language.
    Programming languages generally fall into one of two categories: Compiled or Interpreted. With a compiled language (C, C++, Rust), code you enter is reduced to a set of machine-specific instructions before being saved as an executable file. With interpreted languages, the code is saved in the same format that you entered. Compiled programs generally run faster than interpreted ones because interpreted programs must be reduced to machine instructions at runtime. However, with an interpreted language you can do things that cannot be done in a compiled language. For example, interpreted programs can modify themselves by adding or changing functions at runtime. It is also usually easier to develop applications in an interpreted environment because you don't have to recompile your application each time you want to test a small section. (source: http://www.vanguardsw.com/dphelp4/dph00296.htm)

    ![Alt text](public/python_interpreted.png)
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Python Coding Basics

    ### Python is case-sensitive
    Most components in Python are case-sensitive (e.g., statements, variable names, file names, etc.). Windows is generally case-insensitive.
    """
    )
    return


@app.cell
def _():
    # ERROR: uncomment to raise error
    # myVar = 0
    # print(myvar)
    return


@app.cell
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
    # ERROR: uncomment to raise error
    # if 4 > 1:
    # print("4 is greater than 1")
    # print("hi")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Comment your code

    Make a habit of clearly commenting your code...even if the purpose of the code seems obvious. Even for code you have written yourself, it is often difficult to remember why you chose to implement something in a specific way. 

    Start a comment using the hash (#) symbol
    """
    )
    return


@app.cell
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

    print("This is the first line. ", end='')
    print("Also on same line.")

    # Print variable and concatenate
    x = 'apple'
    print(x)
    print('fuit: ' + x)
    return


if __name__ == "__main__":
    app.run()
