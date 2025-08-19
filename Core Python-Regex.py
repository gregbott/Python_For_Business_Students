import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Regular Expressions
        RegEx or regular expressions is a sequence of characters that match other strings or sets of strings, using a specialized syntax pattern. Python has a built-in package called re, which can be used to work with regular expressions. To use the re package, import re.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Raw Strings

        To avoid Python escaping the RegEx patterns, prefix the patter with 'r'.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Regex Cheat Sheet

        source: https://regexone.com

        For an excellent interactive tutorial, go to https://regexone.com/lesson/introduction_abcs

        To test and learn more about RegEx, https://regexr.com/ is also a helpful site.

        abc…	Letters<br>
        123…	Digits<br>
        \d	Any Digit<br>
        \D	Any Non-digit character<br>
        .	Any Character<br>
        \.	Period<br>
        [abc]	Only a, b, or c<br>
        [^abc]	Not a, b, nor c<br>
        [a-z]	Characters a to z<br>
        [0-9]	Numbers 0 to 9<br>
        \w	Any Alphanumeric character<br>
        \W	Any Non-alphanumeric character<br>
        {m}	m Repetitions<br>
        {m,n}	m to n Repetitions<br>
        \*	Zero or more repetitions<br>
        \+	One or more repetitions<br>
        ?	Optional character<br>
        \s	Any Whitespace<br>
        \S	Any Non-whitespace character<br>
        ^…$	Starts and ends<br>
        (…)	Capture Group<br>
        (a(bc))	Capture Sub-group<br>
        (.*)	Capture all<br>
        (abc|def)	Matches abc or def<br>
        """
    )
    return


@app.cell
def _():
    import re
    import pprint as pp
    import pathlib
    _email_header = 'Fire: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Return-Path: <postmaster@collab.sakaiproject.org> for <source@collab.sakaiproject.org>;Received: (from apache@localhost) Author:  stephen.marquard@uct.ac'
    _found_text = re.findall('From.+:', _email_header)
    print(_found_text)
    print('found text is of type', type(_found_text))
    return (re,)


@app.cell
def _(re):
    _email_header = 'Fire: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008 Return-Path: <postmaster@collab.sakaiproject.org> for <source@collab.sakaiproject.org>;Received: (from apache@localhost) Author:  stephen.marquard@uct.ac'
    _found_text = re.findall('\\d\\d:\\d\\d:\\d\\d', _email_header)
    print(_found_text)
    print('found text is of type', type(_found_text))
    author = re.findall('Author:\\s+\\S+', _email_header)
    print(author)
    return


@app.cell
def _(re):
    _mboxfile = open('data/mbox-short.txt', 'r')
    for _line in _mboxfile:
        _line = _line.rstrip()
        if re.search('^From:', _line):
            print(_line)
    _mboxfile.close()
    return


@app.cell
def _(re):
    _mboxfile = open('data//mbox-short.txt', 'r')
    all_emails_list = []
    for _line in _mboxfile:
        _line = _line.rstrip()
        _x = re.findall('[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\\.)+[A-Za-z]{2,}', _line)
        if len(_x) > 0:
            all_emails_list.extend(_x)
    print(len(all_emails_list))
    print(len(set(all_emails_list)))
    print(set(all_emails_list))
    return (all_emails_list,)


@app.cell
def _():
    mystring = 'hello, a my friend'
    mystring.title()
    return


@app.cell
def _(all_emails_list):
    list((set(all_emails_list)))
    return


@app.cell
def _(re):
    _mboxfile = open('files\\mbox-short.txt', 'r')
    all_emails_list_1 = []
    for _line in _mboxfile:
        _line = _line.rstrip()
        _x = re.findall('rev=.....', _line)
        if len(_x) > 0:
            all_emails_list_1.extend(_x)
    print(all_emails_list_1)
    all_revs_set = set(all_emails_list_1)
    print(len(all_revs_set))
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
