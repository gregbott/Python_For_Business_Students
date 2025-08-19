import marimo

__generated_with = "0.14.17"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Using Selenium to Control the Browser
        Use ```selenium``` in combination with a browser driver to control a browser. This combination of driver and Selenium is one method to test web browsers and also helpful when it is difficult or impossible to scrape data using only Beautiful soup and requests.

        > Note: If using Linux, avoid using the Flatpak installation of Chrome. Use the .deb instead.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Get Selenium-Controlled Instance of Chrome Browser
        Below is an example of how you would programmatically send login information to MyBama.

        First, find copy the url and then import web driver, start an instance of Chrome and then pass the URL using the ```get``` method.
        """
    )
    return


@app.cell
def _():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    import bs4
    return By, Service, bs4, webdriver


@app.cell
def _(Service, webdriver):
    # path = '/usr/bin/chromedriver'
    path = './chromedriver' # In current folder
    # path = '/usr/local/bin/chromedriver'
    # path = r'c:\chromedriver\chromedriver.exe' # Windows
    service = Service(executable_path=path)
    browser = webdriver.Chrome(service=service)
    return (browser,)


@app.cell
def _(browser):
    browser.delete_all_cookies()
    return


@app.cell
def _(browser):
    browser.get('https://finance.yahoo.com/quote/AAPL')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Locate the target elements
        To log into MyBama you'll need to enter an ID and password. Use the Inspect Element of your browser to locate the specific element that provides the input box for ID and password. 

        For example, drill down the hierarchy until only the myBama ID box is highlighted when you are mousing over its corresponding element.
        ```HTML
        <input class="required" id="username" size="25" tabindex="1" type="text" accesskey="u" autocomplete="off" 
               autocorrect="off" autocapitalize="off" spellcheck="false" name="username" value="">
        ```
        Notice the tag name (input) and the id (username). We can use these to uniquely locate the form box and place a value inside of it.

        However, before we locate that exact tag, let's look at some methods to find elements.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Finding Elements on the Page
        WebDriver objects provide two primary methods for locating elements.
        1. find_element (singular)
        2. find_elements (plural)

        Using the singular option returns the *first* element on the page. Using the plural option returns a list of WebElement_* objects.

        For example, using the myBama login page, we can locate the following.

        There are many different methods by which you can find elements on a page.
        * by tag
        * by ID
        * by class name
        * using CSS selectors
        * using XPath notation

        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Use named parameters
        """
    )
    return


@app.cell
def _(browser):
    # Click the 3 month view
    browser.find_element(by='id',value='tab-3m').click()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Use the By object with ID attribute
        """
    )
    return


@app.cell
def _(By, browser):
    # Click the Year-To-Date view
    browser.find_element(By.ID,'tab-YTD').click()
    return


@app.cell
def _(By, browser):
    # Change to the Advanced Chart view
    browser.find_element(By.CLASS_NAME,'advchartlabel').click()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Take a screenshot and display it
        """
    )
    return


@app.cell
def _(browser):
    adv_chart_png = browser.get_screenshot_as_png()
    return (adv_chart_png,)


@app.cell
def _(adv_chart_png):
    from IPython.display import display, Image
    display(Image(data=adv_chart_png))
    return


@app.cell
def _(adv_chart_png):
    # You could also save the screenshot as a file
    with open ('adv_chart.png', 'wb') as fh:
        fh.write(adv_chart_png)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Find Elements using XPath
        You can also use the XPath notation to locate elements. One way to obtain the XPath selector is to use the Inspect feature of your browser, point to Copy, and then choose XPATH.
        """
    )
    return


@app.cell
def _(browser):
    browser.get('https://mybama.ua.edu')
    return


@app.cell
def _(By, browser):
    print(browser.find_element(By.XPATH,'//*[@id="username"]').get_attribute("id"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Find Elements using CSS
        You can also use CSS to locate elements. One way to obtain the CSS selector is to use the Inspect feature of your browser, point to Copy, and then choose "Copy selector".
        """
    )
    return


@app.cell
def _(By, browser):
    print(browser.find_element(By.CSS_SELECTOR,'#username').get_attribute("id"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Find element by Class Name
        You can also find elements by class name. If a class name has spaces in it, those are multiple class names. For example, the Submit button has the following class: ```btn btn-block btn-submit```. You may select that button using any of the three different class names. You may NOT use the entire contents ```btn btn-block btn-submit```. To click the button, add the .click() method after the element.

        ```Python
        browser.find_element(By.CLASS_NAME, 'btn-submit').get_attribute("name").click()
        ```
        """
    )
    return


@app.cell
def _(By, browser):
    # Choose only one of the class names to locate the HTML element
    print(browser.find_element(By.CLASS_NAME,'mdc-text-field__input').get_attribute("style"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Find Elements by Link and partial Link
        """
    )
    return


@app.cell
def _(By, browser):
    links = browser.find_elements(By.PARTIAL_LINK_TEXT,'Student')
    for link in links:
        print(link.text)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Exceptions when locating Elements
        If you attempt to locate an element that does not exist, Python will raise a ```NoSuchElementException``` error. To trap that error, first import it from selenium.common.exceptions and then use a try...except block. You could also trap it generically, of course (e.g., just a try...except block without using NoSuchElementException).
        """
    )
    return


@app.cell
def _(browser):
    browser.get('https://mybama.ua.edu')
    return


@app.cell
def _(By, browser):
    # ERROR - Element does not exist.
    print(browser.find_element(By.ID, 'duo_password').get_attribute("name"))
    return


@app.cell
def _(By, browser):
    from selenium.common.exceptions import NoSuchElementException

    try:
        print(browser.find_element(By.ID,'duo_password').get_attribute("name"))
    except NoSuchElementException as no_element_err:
        print(no_element_err)

    print("continue scraping...")
    return


@app.cell
def _():
    import json
    with open('info.json', 'r') as filehandle:
        credentials = json.load(filehandle)
    return (credentials,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Check if an element is visible
        For elements that are present on the page, you can check whether or not they are displayed to the user. Note that if you attempt to check if a non-existent element is displayed, you'll still raise a NoSuchElementException error.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Paginating Example
        """
    )
    return


@app.cell
def _(browser):
    # Open job site
    browser.get('https://careers.ua.edu/jobs/search')
    return


@app.cell
def _(By, browser):
    row_tags = list(browser.find_elements(By.TAG_NAME,'tr'))
    return (row_tags,)


@app.cell
def _(row_tags):
    row_tags[0].text
    return


@app.cell
def _(By, browser):
    tables = browser.find_elements(By.CLASS_NAME, 'table')
    print(len(tables))
    return


@app.cell
def _(browser, bs4):
    page_html = bs4.BeautifulSoup(browser.page_source)
    return (page_html,)


@app.cell
def _(page_html):
    page_html
    return


@app.cell
def _(page_html):
    post_body = page_html.find(attrs = {'class':'even'})
    return (post_body,)


@app.cell
def _(post_body):
    post_body
    return


@app.cell
def _(By, row_tags):
    for row_tag in row_tags:
        col_tags = row_tag.find_elements(By.TAG_NAME,'td')
        for col_tag in col_tags:
            print(col_tag.text, sep=" ")
        print('-'*80)
    return


@app.cell
def _(By, browser):
    next_href = browser.find_element(By.PARTIAL_LINK_TEXT,'›')
    return


@app.cell
def _(By, browser):
    next_href_1 = browser.find_element(By.CLASS_NAME, 'next_page')
    return (next_href_1,)


@app.cell
def _(next_href_1):
    cn_class = next_href_1.get_attribute('class')
    cn_class
    return (cn_class,)


@app.cell
def _(cn_class, next_href_1):
    print(f'cn_class =  {cn_class}')
    if 'disabled' not in cn_class:
        next_href_1.click()
    else:
        print('done')
    return


@app.cell
def _(By, browser):
    rows = browser.find_elements(By.TAG_NAME, 'tr')
    return (rows,)


@app.cell
def _(By, rows):
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        for col in cols:
            print(col.text, end = "|")
        print()
        print('-'*40)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Filling Out and Submitting Forms
        To send text to input elements on a form, first find the element then invoke the send_keys method passing the text you want to enter into the form field.
        """
    )
    return


@app.cell
def _(browser):
    browser.get('https://mybama.ua.edu')
    return


@app.cell
def _(By, browser):
    browser.find_element(By.ID,'username').clear()
    return


@app.cell
def _(By, browser, credentials):
    browser.find_element(By.ID,'username').send_keys('gjbott')
    browser.find_element(By.ID,'password').send_keys(credentials['Password'])
    return


@app.cell
def _(By, browser):
    browser.find_element(By.CLASS_NAME, 'mdc-button').click()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Sending Special Keys
        Selenium also supports sending special keys such as directional keys (UP, DOWN, RIGHT, LEFT), as well as the ESCAPE, DELETE, TAB, BACK_SPACE, HOME, END, PAGE_DOWN, and PAGE_UP keys.
        """
    )
    return


@app.cell
def _(browser):
    # ROBOT Detected!!
    browser.get('https://wsj.com')
    return


@app.cell
def _(browser):
    browser.get('https://espn.com')
    return


@app.cell
def _(By, browser):
    # First, get an element on the page
    from selenium.webdriver.common.keys import Keys
    htmlElem = browser.find_element(By.TAG_NAME,'html')
    return Keys, htmlElem


@app.cell
def _(Keys, htmlElem):
    htmlElem.send_keys(Keys.PAGE_DOWN)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Delaying actions
        Automated actions happen very quickly. Sometimes too quickly for a browser to handle. There are several methods to force your browser to wait. One simple method is to sleep for X number of seconds.
        """
    )
    return


@app.cell
def _(Keys, htmlElem):
    import time
    htmlElem.send_keys(Keys.HOME)
    time.sleep(2) # Wait 2 seconds
    htmlElem.send_keys(Keys.END)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Clicking Browser Buttons
        You may also want to use the standard Back, Forward, Refresh and Quit buttons on a browser.
        """
    )
    return


@app.cell
def _(browser):
    # Go back
    browser.back()
    return


@app.cell
def _(browser):
    browser.forward()
    return


@app.cell
def _(browser):
    browser.current_url
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Ending your session
        Selenium provides a ```close``` and ```quit``` method. The former closes a window, but leaves the session in memory, quit closes all windows and deletes the session.
        """
    )
    return


@app.cell
def _(browser):
    # Quit and end session
    browser.quit()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
