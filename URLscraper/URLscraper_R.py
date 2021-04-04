'''
A web scraper to collect all URLs from rechtsprechung-im-internet.de.
Here, a "spider" is needed to navigate the database properly and get all URLs.
Could need a re-run and a creation of several URL lists to be merged at the end
(due to result visualization limit of the database).

Insert location of your Firefox driver
'''

import urllib3
from urllib3.util import Retry
from selenium import webdriver
import time

# insert location of your Firefox (or other browser's) driver below
driver = webdriver.Firefox(executable_path=r"\geckodriver-v0.28.0-win64\geckodriver.exe")


retries = Retry(connect=10, read=5, redirect=10)
http = urllib3.PoolManager(retries=retries)

'''setting filepath for output file'''
path_output = r""
starting_page_1900to2020 = "https://www.rechtsprechung-im-internet.de/jportal/portal/t/puj/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXYV3nxQABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEEboj5bbS95ohxV6qlJYUe8AAABA7uuPhmHIsG2jxKFv8yqnrE8zMbNFdiHFYV2t1Vv5%2BMX76WMgIskV%2BFLRrRqGNZwpPgrDZ6zJiwy0FEgp31qyJAAUJOCRpM%2BjQ0JPvr%2FrL2hRs7aGn98%3D&sugportalport=8080&sughashcode=988504563854828511814400006481283373430001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=1900&dateTo=2020&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=suchen"

def click_next():
    '''clicking on "weiter" (next page) button'''
    driver.find_element_by_xpath('//*[@title="weiter"]').click()
    time.sleep(0.5)

lista_URLs = []
'''here put the link from where the scraping was interrupted'''
driver.get(starting_page_1900to2020) #first time set to starting_page_1900to2020, then insert URL of new date-based search (after scraping the initial 15.000 URLs)
for i in range(700): #database only shows 15.000 results for each query, divided into 700 pages
    click_next()
    elements = driver.find_elements_by_css_selector("[title*='Treffer Langtext']")
    for element in elements:
        lista_URLs.append(element.get_attribute("href"))
    txt = "\n".join(lista_URLs)
    with open(path_output, "w", encoding="utf-8") as file:
        file.write(txt)

print("Done")





