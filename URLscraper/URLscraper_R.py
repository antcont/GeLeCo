'''
A web scraper to collect all URLs from rechtsprechung-im-internet.de.
'''

import argparse, urllib3, time, os, sys
from urllib3.util import Retry
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

parser = argparse.ArgumentParser(description="A web scraper to collect all URLs from rechtsprechung-im-internet.de.")
args = parser.parse_args()

webdriver_path = os.path.join(sys.path[0], "geckodriver.exe")
driver = webdriver.Firefox(executable_path=webdriver_path)

retries = Retry(connect=10, read=5, redirect=10)
http = urllib3.PoolManager(retries=retries)

#  a list of the URLs of the search page for each 2-years' court decisions
startFrom = ["https://www.rechtsprechung-im-internet.de/jportal/portal/t/rgi/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkus%2BNeABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEPIzHmb1Q2PDzvkDoHoEnlkAAABAkOiLYkBk7bCxGEm1XYZYgBmPD8iS7HV5yiYOzlVixBLyDc8QGGsr59zpf30mo2ep3pxhXG20DDiJIUHKjEVP3AAU2H0cO8d%2FFqiC%2FXCaAwgM6aJA%2BX0%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2010&dateTo=2011&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=suchen",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/73/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXk0OZNhABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAENJ72UgSI%2FRuQBwtAWWXFtgAAABAVECE3dmpapAYeoy4cGOdCgPlpjJrpQSfGzfCbqhB5N9AmTO2%2FQPwTXfphprbTOWUBip5nlJHeUmh9flaM5h%2F0QAUE2s%2Bcs2mSWEyPwVEIHds%2FFLluvc%3D&sugportalport=8080&sughashcode=-981779126532556343564171258191437896920001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2012&dateTo=2013&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche.x=0&standardsuche.y=0",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rl4/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuuFZ7ABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEHKrfFSO%2F1AOwTCwNLoLRtkAAABA2QnULjmE1eBTyTwIZ8I1G%2B60fWM%2B%2FHBTHcIyYrnd4FAKwxAfvp60LlYhidR%2FHnjo2M0nlRtDRbuJuXpUBPRsqQAU0OXpXIP3oXo%2FHrNEBvWFgutC5Ks%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2014&dateTo=2015&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/roc/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuusfoABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEA9RJSzRld2qLAvQogqZFNUAAABAtfEVwfc1WSNkqvKeGJUSuV0FSHEnxrOqypP%2F%2FuHbpVl%2BIogRs55jlJ9T2H2NtsDo9e6r6wTIdtMygfa4Wu120QAUTVH3GNFa%2BMWpZW2vIO2kcsZ8UxM%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2016&dateTo=2017&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rpf/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuu9yJABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEGU6R1B9Ah%2FWet1O2ewQcEoAAABAqn5m01%2FtRU9X3SzMzbZJQUsvA1XlvXL6DK4%2Fsr49%2BGenf8E3lQwl%2BcP%2BIuvIdKugTOqSZTT7rX3TRMSQZIBpfAAUDWZgwPD53PkmI8n8mTQ%2BM9FTbPo%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2018&dateTo=2019&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche.x=0&standardsuche.y=0",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rqn/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuvYjqABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEJVKlrHXFHOgv0w1BgdZYCAAAABA2%2FtYeNyeeSN6igfQVOkiEZhuK%2Fe12uaLcZETEyqOaR3L3BXW5xbOLi9C3gkscmxAyz8xWFJt1bbh00WVPiyBcQAUf3ec4dnEa1uE6zA7ya5yDSPyANc%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2020&dateTo=2021&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern"
             ]

def click_next():
    '''
    clicking on "weiter" (next page) button
    '''
    driver.find_element_by_xpath('//*[@title="weiter"]').click()
    time.sleep(3)


list_URLs = []
counter = 0
for url in startFrom:
    driver.get(url)
    for i in range(700):  # database only shows 15.000 results at most for each query, divided into 700 pages

        try:
            click_next()
            elements_len = len(driver.find_elements_by_css_selector("[title*='Treffer Langtext']"))
            for index in range(elements_len):
                list_URLs.append(driver.find_elements_by_css_selector("[title*='Treffer Langtext']")[index].
                                 get_attribute("href"))  # re-find elements to avoid StaleElementReferenceException
                counter += 1
                print("\r", counter, " URLs collected", end="")

        except NoSuchElementException:
            # when all texts from the current selection have been displayed and the "weiter" button is not activated
            break    # next URL in startFrom list

        except Exception as exc:  # usually due to staleness (new page may not have been loaded before scraping)
            #print("\n", exc.args, "\n")
            try:
                time.sleep(5)
                elements_len = len(driver.find_elements_by_css_selector("[title*='Treffer Langtext']"))
                for index in range(elements_len):
                    list_URLs.append(driver.find_elements_by_css_selector("[title*='Treffer Langtext']")[index].
                                     get_attribute("href"))
                    counter += 1
                    print("\r", counter, " URLs collected", end="")

            except:
                raise

list_URLs = (list(set(list_URLs)))  # deduplicating

with open("URL_list_R.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(list_URLs))

print("\r", counter, "URLs collected.")
print("URL list created.")





