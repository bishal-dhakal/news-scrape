from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
import time

browser = Selenium()

def work():
    try:
        browser.open_available_browser("https://ceotab.com/category/entertainment/", maximized=True)
        time.sleep(3)

        title_el_xpath ='//header[@class="entry-header"]//a'
        title_els = browser.find_elements(title_el_xpath)

        for i in title_els:

            full_article = browser.get_element_attribute(i,'href')
            browser.go_to(full_article)
            print('hello')
            time.sleep(3)
            browser.go_to('https://ceotab.com/category/entertainment/')
            print('feri')

        browser.close_all_browsers()
    except:
        pass


@task
def minimal_task():
    work()
