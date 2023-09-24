from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
import time
import pandas as pd
from robot.libraries.BuiltIn import BuiltIn
import csv

browser = Selenium()


def work():
    try:
        browser.open_available_browser(
            "https://ceotab.com/category/entertainment/", maximized=True)
        time.sleep(4)

        title_el_xpath = '//header[@class="entry-header"]//a'
        image_xpath = '//div[@class="featured-image"]//img'
        header_xpath = '//header[@class="entry-header"]'
        time_xpath = '//div[@class="article-content clearfix"]//time[1]'
        content_xpath = '//div[@class="entry-content clearfix"]'
        previous_xpath = '//ul[@class="default-wp-page clearfix"]//li[@class="previous"]//a'

        links = []
        try:
            for i in range(17):
                try:
                    title_els = browser.find_elements(title_el_xpath)
                    for i in title_els:
                        full_article = browser.get_element_attribute(i, 'href')
                        links.append(full_article)
                    browser.click_element_when_clickable(previous_xpath)

                except:
                    title_els = browser.find_elements(title_el_xpath)
                    for i in title_els:
                        full_article = browser.get_element_attribute(i, 'href')
                        links.append(full_article)

            all_data = []
            for i in links:
                try:
                    browser.go_to(i)
                    header_text = browser.get_text(header_xpath)
                    time_data = browser.get_text(time_xpath)
                    content = browser.get_text(content_xpath)
                    image = browser.get_element_attribute(image_xpath, 'src')

                    data = [
                        header_text,
                        time_data,
                        content,
                        image
                    ]

                    all_data.append(data)

                    BuiltIn().log_to_console(data)


                except Exception as e:
                    print(e)

            
            df = pd.DataFrame(all_data)

            # Specify the CSV file name and write the DataFrame to it
            csv_filename = 'sample.csv'
            df.to_csv(csv_filename, index=False)
           

        except:
            pass

        browser.close_all_browsers()
    except:
        pass


@task
def minimal_task():
    work()
