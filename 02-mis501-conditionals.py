import marimo

__generated_with = "0.15.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/mis501-conditionals.grid.json",
)


@app.cell
def _():
    import marimo as mo
    import random
    from pathlib import Path
    return Path, mo, random


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Conditionals""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Learning Objectives
    By the end of this lesson, students will be able to:

    - Master all forms of conditional statements in Python
    - Understand advanced conditional patterns and techniques
    - Apply functional programming concepts with conditionals
    - Use modern Python features for conditional logic
    - Handle errors and edge cases with proper conditional structures
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Basic Conditionals: The Foundation

    ### Simple `if` Statements
    The most basic form of conditional logic.
    """
    )
    return


@app.cell
def _():
    # Example 1: Basic if statement
    temperature = 97
    if temperature > 95:
        print("It's hot in Alabama!")

    # Example 2: Using variables in conditions
    age = 16
    if age >= 18:
        print("You can vote!")

    # Practice: Check if a number is positive
    number = 42
    if number > 0:
        print(f"{number} is positive!")
    return (age,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### `if-else` Statements
    Binary decisions - execute one block or another.
    """
    )
    return


@app.cell
def _(age, random):
    if age >= 18:
        print(f"At {age}, you can vote!")
    else:
        print(f"At {age}, you cannot vote yet.")

    # Example: Even or odd checker

    random_number = random.randint(1,100)

    if random_number % 2 == 0:
        print(f"{random_number} is even")
    else:
        print(f"{random_number} is odd")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### `elif` Statements
    Multiple conditions checked in sequence.
    """
    )
    return


@app.cell
def _():
    score = 85

    if score >= 90:
        print('checked') # sub-statements are only run if condition is met
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Comparison Operators""")
    return


@app.cell
def _():
    # Demonstration of all comparison operators
    a, b = 10, 20

    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}")  # Equal to
    print(f"a != b: {a != b}")  # Not equal to
    print(f"a > b: {a > b}")    # Greater than
    print(f"a < b: {a < b}")    # Less than
    print(f"a >= b: {a >= b}")  # Greater than or equal
    print(f"a <= b: {a <= b}")  # Less than or equal

    # Common mistake demonstration
    print("\n⚠️ Common Mistake Alert:")
    print("= is assignment, == is comparison!")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Evaluating True and False for Values""")
    return


@app.cell
def _():
    _my_list = [1,0,-1,'string value', 2.1, None]

    for item in _my_list:
        if item:
            print(f'{item} is True because non-zero and non-None values are True')
        else:
            print(f'{item} is False because zero and None values are False')
    return


@app.cell
def _(Path):
    dummy_file = Path('data/dummy_file.txt').exists()

    if dummy_file:
        print("file exists")
    else:
        print("file does not exist")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Logical Operators
    Combine multiple conditions for complex logic.
    """
    )
    return


@app.cell
def _():
    def _():
        # AND operator - both conditions must be True
        age = 25
        has_license = True

        if age >= 18 and has_license:
            print("You can drive!")
        else:
            print("You cannot drive.")

        # OR operator - at least one condition must be True
        temperature = 75
        weather = "sunny"

        if temperature > 70 or weather == "sunny":
            print("Great day for a picnic!")

        # NOT operator - reverses boolean value
        is_raining = False
        if not is_raining:
            print("No need for an umbrella!")

        # Complex logical combinations
        is_weekend = True
        has_money = True
        weather_good = True

        if (is_weekend and has_money) and (weather_good or not is_raining):
            return print("Perfect day for shopping!")


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Modern Python: Match-Case Statements (Python 3.10+)

    Python's equivalent to switch-case statements, but much more powerful.

    Python’s match-case statements, introduced in Python 3.10, are more powerful than traditional switch-case statements found in languages like C, Java, or JavaScript due to their support for pattern matching, which goes beyond simple value comparisons. Here’s a breakdown of why match-case is more versatile and expressive:

    **Pattern Matching Beyond Simple Values**

    _Switch-case_: Traditional switch-case statements (e.g., in C or Java) typically compare a single expression against constant values (e.g., integers, strings, or enums). They are limited to equality checks.

    _Match-case_: Python’s match-case supports structural pattern matching, allowing you to match against complex data structures like lists, tuples, dictionaries, or custom objects, not just single values. You can match based on the shape or structure of the data, not just its value.
    """
    )
    return


@app.cell
def _():
    def classify_number(n):
        match n:
            case x if x < 0:
                return "Negative"
            case 0:
                return "Zero"
            case x if x % 2 == 0:
                return "Positive even"
            case _:
                return "Positive odd"

    print(classify_number(4))  # Output: Positive even
    return


@app.cell
def _():
    def process_data(data):
        match data:
            case [_, "error", _]: # finds "error" in index 1 only
                return "Error found in list"
            case _:
                return "No error"

    print(process_data([1, "error", 3]))  # Output: Error found in list
    return


@app.cell
def _():
    def process_data_v2(data):
        match data:
            case [*items] if "error" in items: # finds "error" in any position
                return "Error found in list"
            case _:
                return "No error"

    print(process_data_v2([1, 2, "error", 3]))  # Output: Error found in list
    print(process_data_v2([1, 2, 3]))       # Output: No error
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Ternary Operator (Conditional Expression)

    A concise way to write simple if-else statements in one line.
    """
    )
    return


@app.cell
def _():
    def _():
        # Basic ternary operator examples
        age = 20
        status = "adult" if age >= 18 else "minor"
        print(f"Age: {age}, Status: {status}")

        # More examples
        a, b = 15, 10
        max_value = a if a > b else b
        print(f"Maximum of {a} and {b} is: {max_value}")

        score = 75
        result = "Pass" if score >= 60 else "Fail"
        print(f"Score: {score}, Result: {result}")

        # Nested ternary (use sparingly!)
        temperature = 85
        clothing = "shorts" if temperature > 80 else ("jacket" if temperature > 60 else "coat")
        print(f"Temperature: {temperature}°F, Wear: {clothing}")

        # Ternary in function calls
        numbers = [1, 2, 3, 4, 5]
        operation = "sum"
        result = sum(numbers) if operation == "sum" else max(numbers)
        return print(f"Operation '{operation}' on {numbers} = {result}")


    _()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Exception Handling
    Exception handling in Python manages errors that occur during program execution, preventing crashes and allowing graceful recovery. It uses a try-except structure to catch and handle exceptions (errors).

    _try block_: Contains code that might raise an exception.

    _except block_: Handles specific exceptions or a general exception if an error occurs.

    _else block_ (optional): Runs if no exception is raised in the try block.

    _finally block_ (optional): Executes regardless of whether an exception occurs, often used for cleanup (e.g., closing files).
    """
    )
    return


@app.cell
def _(divisor):
    # divisor = 2
    # divisor = 'not a number'
    # divisor = 0

    try:
        result = 10 / divisor  # Raises ZeroDivisionError
    except ZeroDivisionError: # more specific exception first
        print("Cannot divide by zero!")
    except Exception as e:
        print("error:", e)
    else: # runs when successful
        print("Division successful:", result)
    finally: # runs always
        print("Execution complete.")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Assertion Statements
    In Python, the assert statement is used to enforce conditions that must be true during program execution, primarily for debugging and testing. It checks if an expression evaluates to True; if not, it raises an AssertionError, halting execution (unless ignored in production). Below are real-world uses of assert statements:
    1. Debugging and Development
    2. Input Validation in APIs or Data Processing
    3. Testing and Quality Assurance
    4. Enforcing Invariants in Algorithms
    5. Data Integrity in Scientific Computing (e.g., 'matrix must be square')
    6. Configuration Validation
    7. Preventing Security Issues (e.g., authorized access)
    8. Ensuring Resource Availability

    - Assertions are typically used during development and testing, as they can be disabled in production (using Python’s -O or -OO flags), so they shouldn’t replace critical error handling (e.g., try-except).

    - They’re best for catching programmer errors (bugs) rather than handling user errors or expected runtime issues.

    - Overusing assertions for non-critical checks can clutter code, so they’re most effective for invariants or critical assumptions.
    """
    )
    return


@app.cell
def _():
    def process_user_data(age):
        assert isinstance(age, int) and 18 <= age <= 120, "Invalid age provided"
        print("Proceed with processing...")

    process_user_data(19)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
