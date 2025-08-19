import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Error Handling

        Types of errors:
        1. Syntactical
        2. Logical
        3. Runtime

        Robust programs anticipate and gracefully handle unexpected situations and errors. For example, when asking a user to input a number, a robust program gracefully handles unexpected or erroneous input. Another examples include attempting to open a file or connect to a database. When the interpreter encounters an error, execution stops and an Exception object is accessible.

        ```Python
        try:
            # run code
        except Exception:
            # run this code if there is an error
        else:
            # Run this code if there are no errors
        finally:
            # Always run this code
        ```

        Error handling enables the developer to gracefully respond to exceptions in code. Without error handling, users will be confronted with error output they may not understand and that stops execution. 

        Instead, use error handling to communicate resolution steps to the user and continue execution or exit gracefully.

        The ```pass``` statement is a null statement. It does nothing and is discarded by the interpreter. 
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Syntax Errors
        These are not exceptions and will not be handled by a try...except block.
        """
    )
    return


app._unparsable_cell(
    r"""
    # Syntatical error
    print('Hello, world)
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If an exception occurs outside of a try...except block, it is "unhandled" and stops the processing of your code. This is typically an undesirable outcome.
        """
    )
    return


@app.cell
def _():
    # Error: File Does not exist
    with open("demo_file.txt", 'r') as f:
        f.read()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using Try...Except
        If an exception is raised within a try...except block, you can decide how you want to handle it. 

        The code below traps all general errors.
        """
    )
    return


@app.cell
def _():
    try:
        with open('does_not_exist.txt', 'r') as f_1:
            f_1.read()
        print('line after open file')
    except Exception as e:
        print(f'An exception was raised: {e}')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Handling specific errors
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The code below ONLY traps ```FileNotFoundError``` exceptions.

        What would happen if an exception other than ```FileNotFoundError``` was raised?
        """
    )
    return


@app.cell
def _():
    try:
        with open('does_not_exist.txt', 'r') as f_2:
            f_2.read()
        print('line after open file')
    except FileNotFoundError as e:
        print('File not found.')
    print('hello world')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        When handling multiple exceptions, sort your exception handling with the most specific at the top and the more general towards the bottom. Otherwise, the specific exceptions will never be caught.


        """
    )
    return


@app.cell
def _():
    try:
        with open('demofile.txt', 'r') as f_3:
            f_3.read()
    except FileNotFoundError as fnf:
        print('Please input the correct path and file name.\n', fnf)
    except NameError as e:
        print(e)
    return


@app.cell
def _():
    5/0
    return


@app.cell
def _():
    my_list = [1,2,3]
    try:
        # 5/0
        #
        # with open("notyourfile.txt", 'r') as f:
        #      text = f.read()
    
        # print(my_list[3])

        # x = uuuu
    
        print('hi')
    except FileNotFoundError as e:
        print("File not found. Please check the file path and try again.")
    except ZeroDivisionError as e:
        print("Attempting to divide by zero!")
    except NameError as e:
        print("name error")
    except Exception as e:
        print("all other errors caught here:", e)
        print(e.with_traceback)
    else:
        print("ran without exception")
    finally:
        print('\ndo logging here')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using Else and Finally
        Use the ```else``` clause to run code if NO errors are thrown.
        Code in the ```finally``` block always runs--irrespective of whether an exception was caught. Use ```finally``` to do clean-up, close files, write data to disk, etc.
        """
    )
    return


@app.cell
def _():
    try:
        with open('demofile.txt', 'r') as f_4:
            f_4.read()
        newfile = ''
    except FileNotFoundError as e:
        print(e, '\n\nPlease input the correct path and file name.\n')
    except NameError as e:
        print(e)
    else:
        print('No exceptions thrown.\n')
    finally:
        print('Opening file process completed.\n')
    return


@app.cell
def _():
    # You can also raise errors manually (outside try-except)

    x = "hello"

    if not type(x) is int:
        raise TypeError("Only integers are allowed")
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Raising Exceptions
        Use ```raise`` to create custom exceptions. For example, your code may demand that only an integer be provided for a specific function. 

        Get the type of the variable and if it is not an integer, raise an exception and inform the user.
        """
    )
    return


@app.cell
def _(x):
    # Manually raising an error inside try..except
    try:
        if not type(x) is int:
            raise TypeError("Only integers are allowed") 
    except Exception as e:
        print(e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Making Assertions
        Use the ```AssertionError``` exception to verify that certain conditions are being met and to take action if they are not met.
        """
    )
    return


@app.cell
def _():
    import sys

    current_os = sys.platform

    # MacOS = 'darwin'
    acceptable_os = ['win32','darwin']

    try:
        assert(current_os in acceptable_os)
    except AssertionError:
        print(f"This program only runs on Windows and Mac operating systems.")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
