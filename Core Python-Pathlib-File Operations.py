import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # File Operations

        Use the open() function to read(r), append (a), or write (w) to a file. Opening a file returns a file handle, not the actual data in the file. After opening the file you can read or write to it. When you are finished with the file, ensure it is closed. Failing to close a file may lead to memory issues, inaccessible files, and possibly data loss.
        """
    )
    return


@app.cell
def _():
    import os
    os.listdir()
    return (os,)


@app.cell
def _(os):
    # use the os module to access operating system information such as the current working directory (getcwd())

    # Create (or overwrite) a file
    # If no path is specified, the file will be created in the current working directory

    # If the file exists, opening with the "w" parameter will overwrite a file of the same name
    #   if present in the same folder. To append instead of overwriting, use the "a" mode.
    f = open("demofile.txt", "w")

    f.write("This is the first line of the file.\n")

    # Be sure to close your file. Failure to do so will cause problems.
    f.close()

    # Get the current directory
    print(os.getcwd())
    return


@app.cell
def _():
    # magic command not supported in marimo; please file an issue to add support
    # %cat demofile.txt
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using the With statement for opening files
        One advantage to using the With statement is that files you open using this method are automatically closed.
        """
    )
    return


@app.cell
def _():
    with open('demofile.txt', 'a') as f_1:
        f_1.write('This is the second line.\n')
    return


app._unparsable_cell(
    r"""
    # magic command not supported in marimo; please file an issue to add support
    # %cat demofile.txt

    /home/documents/../../
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Using pathlib
        Handling files and folders programmatically can be really difficult. You may need to locate and work with all files with a particular extension, recursively process folders, identify the parent folder of a file or folder, and so on. One of the most powerful modules for file and folder management is pathlib.

        As the name implies, pathlib creates paths. It provides an object-oriented approach to handle file system path and file operations.

        Some of the things you can do:
        1. Create a path object representing a file or a directory path. This enables you to check if it exists, create it if not, find the parent directory, etc.
        2. Perform path operations regardless of platform. Windows, Linux, and Mac have differences in their file systems. Pathlib helps provide a consistent interface across platforms and does not require the developer to query the underlying file system or operating system when performing file system operations.
        3. Path manipulation: join paths, resolve paths, or normalize paths (aka convert a ".." into an absolute path).
        4. File manipulation: you can also read files, write files, list directory contents, and check file permissions.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        [![anatomy_of_PosixPath.png](attachment:2a9acbe3-eb89-4cc1-81fe-b014ba2ba4cb.png)

        https://miguendes.me/python-pathlib is an excellent site for ```pathlib``` examples.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ![anatomy_of_WindowsPath.png](attachment:47a2b213-80d0-4cf1-be75-8ef70e13b713.png)
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Get the current working directory
        """
    )
    return


@app.cell
def _():
    import pathlib
    my_path = pathlib.Path.cwd()
    print(my_path.name)
    return my_path, pathlib


@app.cell
def _(my_path):
    my_path.parent
    return


@app.cell
def _(my_path):
    my_path.drive
    return


@app.cell
def _(my_path):
    # recursively list all files and directories
    my_files_dirs = my_path.iterdir() # iterdir() returns a generator
    my_files_dirs
    return


@app.cell
def _(my_path):
    my_files_dirs_1 = list(my_path.iterdir())
    my_files_dirs_1
    return (my_files_dirs_1,)


@app.cell
def _(my_files_dirs_1):
    my_files_dirs_1[10].name
    return


@app.cell
def _(my_files_dirs_1):
    my_files_dirs_1[10].suffix
    return


@app.cell
def _(my_files_dirs_1):
    my_files_dirs_1[10].stem
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Get the home folder
        The pathlib module provides an easy way to locate the user's home folder. 
        """
    )
    return


@app.cell
def _(pathlib):
    # Get the home folder for the current user
    home_path = pathlib.Path.home()
    print(home_path)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Finding all files of a particular type is accomplished by using Pathlib and the glob (global) module. 
        """
    )
    return


@app.cell
def _(pathlib):
    ofc_dropbox_path = pathlib.Path('/mnt/internal-data/Dropbox')
    return (ofc_dropbox_path,)


@app.function
def show_tree(directory):
    print(f'+ {directory}')
    
    # Limited to Python notebooks
    for path in sorted(directory.rglob('*.ipynb')):
        depth = len(path.relative_to(directory).parts)
        indent = '    ' * depth
        print(f'{'  '} + {path.relative_to(directory).parts}')


@app.cell
def _(ofc_dropbox_path):
    show_tree(ofc_dropbox_path)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Checking if Path exists and creating a folder
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```Python
        parents = True
        ```
        creates all folders in the path as needed.

        ```Python
        exist_ok = False
        ```
        by default, raises FileExistsError if the target directory already exists.
        """
    )
    return


@app.cell
def _(pathlib):
    all_py_files = pathlib.Path.home().rglob('*.py')
    return (all_py_files,)


@app.cell
def _(all_py_files):
    all_py_files_1 = [file.name for file in all_py_files]
    return (all_py_files_1,)


@app.cell
def _(all_py_files_1):
    len(all_py_files_1)
    return


@app.cell
def _(all_py_files_1):
    all_py_files_1[:50]
    return


@app.cell
def _(pathlib):
    # Create a directory in the current working directory
    pathlib.Path.cwd().joinpath('HW101').mkdir()
    return


@app.cell
def _(pathlib):
    # ERROR: Attempt to create a directory when it already exists
    pathlib.Path.cwd().joinpath('HW101').mkdir()
    return


@app.cell
def _(pathlib):
    if pathlib.Path.cwd().joinpath('HW101').exists():
        hw_path = pathlib.Path.cwd().joinpath('HW101').exists()
        print("did not create directory--already exists!")
    else:
        pathlib.Path.cwd().joinpath('HW101').mkdir()
        print("created directory")
    return


@app.cell
def _(pathlib):
    # This can be accomplished in a single line
    #     'parents=True' - create the parent folder(s) if they don't exist. Default is 'False', which raises an error if parent doesn't exist
    pathlib.Path.cwd().joinpath('HW102').mkdir(parents=True, exist_ok=True)
    return


@app.cell
def _(pathlib):
    folder_name = 'HW101'
    hw_path_1 = pathlib.Path.cwd().joinpath(folder_name).exists()
    try:
        pathlib.Path.cwd().joinpath(folder_name).mkdir()
    except FileExistsError:
        print(f'{folder_name} exists.')
    else:
        print(f'{folder_name} created.')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Reading files
        There are several ways to read data from a file. Some of the methods to read a file include: reading a specified number of characters, reading line-by-line, or a reading number of lines.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Reading an entire file
        """
    )
    return


@app.cell
def _(pathlib):
    gettysburg_txt = pathlib.Path('files/gettysburg.txt')
    gettysburg_txt.read_text() # Displays line characters, store in variable then print to process escape characters
    return (gettysburg_txt,)


@app.cell
def _(gettysburg_txt):
    getty_content = gettysburg_txt.read_text()
    print(getty_content)
    return


@app.cell
def _(file_path):
    with open(file_path,"r") as fh_getty:
        n = 100
        #read() will access the entire file. Not a good option for large files.
        print(fh_getty.read(n)) # Read the first n characters
    return


@app.cell
def _(file_path):
    with open(file_path, 'r') as fh_getty_1:
        print(fh_getty_1.readline())
        print(fh_getty_1.readline())
        print(fh_getty_1.readline())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You can also use the built-in file functions of Python to read files.
        """
    )
    return


@app.cell
def _(file_path):
    with open(file_path, 'r') as fh_getty_2:
        x = fh_getty_2.readlines()
        print(x[5])
    return


@app.cell
def _(file_path):
    with open(file_path, 'r') as fh_getty_3:
        line_number = 0
        for x_1 in fh_getty_3:
            print(str(line_number) + ': ' + x_1)
            line_number = line_number + 1
    return


@app.cell
def _(pathlib):
    customer_file = pathlib.Path(r'files/fake_customer_list.txt')
    with open(customer_file, 'r') as fh_customers:

        for line in fh_customers:
            #print(line)
            customer_list = line.strip().split("|")
            full_name = customer_list[0]
            email = customer_list[-1]
            print(full_name + " -- " + email)
    return


@app.cell
def _(os):
    # List files in the current directory 
    import pprint as pp # 'pretty prints' the output in a column
    pp.pprint(os.listdir(os.getcwd()))
    return


@app.cell
def _(os):
    # 'Magic' command to list files in current directory
    os.listdir()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Use the CSV module to read a file
        """
    )
    return


@app.cell
def _(pathlib):
    ms_store = pathlib.Path('files/Microsoft_Store.csv')
    return (ms_store,)


@app.cell
def _(ms_store):
    import pprint as pp
    import csv
    with open(ms_store, 'r') as f_2:
        reader = csv.reader(f_2)
        your_list = list(reader)
    return (your_list,)


@app.cell
def _(pp_1, your_list):
    pp_1.pprint(your_list[:99])
    return


@app.cell
def _(your_list):
    len(your_list)
    return


@app.cell
def _(your_list):
    import pandas as pd
    df_lyrics = pd.DataFrame(your_list, columns=your_list[0])
    return df_lyrics, pd


@app.cell
def _(df_lyrics, pd):
    print(df_lyrics.shape)
    with pd.option_context('display.max_seq_items', None):
        print(df_lyrics.head(5000))
    return


@app.cell
def _(your_list):
    print(your_list[0])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Writing to a File
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Use Pandas to Read a file
        Although built-in file operations in Python may be useful for trivial matters, Pandas and Numpy are much more effective for reading, shaping, and analyzing data. Using these libraries is beyond the scope of this course, however, you should be aware of these libraries. See the Pandas notebook for more information.
        """
    )
    return


@app.cell
def _(pathlib, pd):
    file_path = pathlib.Path('files/2017_instacart_products.csv.gz')
    df = pd.read_csv(file_path)
    df.head()
    return df, file_path


@app.cell
def _(df):
    # Use the describe function to display descriptive statistics for numerical fields (even if that doesn't make sense...)
    df.describe()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
