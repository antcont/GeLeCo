'''
A web scraper to collect all URLs from rechtsprechung-im-internet.de.
Here, a "spider" is needed to navigate the database properly and get all URLs.
Could need a re-run and a creation of several URL lists to be merged at the end
(due to result visualization limit of the database).

Insert location of your Firefox driver
'''

import argparse, urllib3, time, os, sys
from urllib3.util import Retry
from selenium import webdriver

parser = argparse.ArgumentParser(description="A web scraper to collect all URLs from rechtsprechung-im-internet.de. "
                                             "\n")
args = parser.parse_args()

# insert location of your Firefox (or other browser's) driver below
webdriver_path = os.path.join(sys.path[0], "geckodriver.exe")
driver = webdriver.Firefox(executable_path=webdriver_path)

retries = Retry(connect=10, read=5, redirect=10)
http = urllib3.PoolManager(retries=retries)

#  setting filepath for output file
startFrom = ["https://www.rechtsprechung-im-internet.de/jportal/portal/t/rgi/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkus%2BNeABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEPIzHmb1Q2PDzvkDoHoEnlkAAABAkOiLYkBk7bCxGEm1XYZYgBmPD8iS7HV5yiYOzlVixBLyDc8QGGsr59zpf30mo2ep3pxhXG20DDiJIUHKjEVP3AAU2H0cO8d%2FFqiC%2FXCaAwgM6aJA%2BX0%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2010&dateTo=2011&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=suchen",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rgk/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkutAG6ABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEFYe3U929LbQ7SpXMCS%2FuAMAAABAnx9pSecf8qoVsAnRDNiKjbEeBy8ZIC4Q7nyAi4gkFvydOvg%2BncjKJ4CYN4v6BjdoE89cTXsWqoSZjelH9Oi37gAURSTLrjUGP6rNJiMWKntYaxvBESk%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2011&dateTo=2012&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche.x=0&standardsuche.y=0",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rkr/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkut9CYABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEEYg1eul2VQL15HKeVQ8ufcAAABAYM6QX3%2B5eBq9xvPCrz6TYF5ysbFb1xIcuZMSDIVcZdYvC3JQLmlgotCAPFrSntNTNuPc99rbDhq0%2F9AZvoPDcAAUTQQzRmo5ky3WjR2uEAIU0p1oM6o%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=&dateTo=&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&rqfcb=103331300&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rky/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkut%2B7uABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEN8bfRExlE2NUGO2W7jtDXUAAABAsdQPYoUeADph6WijZI7JxhSPd7KIJ%2FkWu3dBQcbY1IT%2Bsq8HsP9aMYB4wE2ziCg4DKQkNnkbleioeagdUuOVGQAUvuTtXLmDb7Gd3Mb8SjSOKotF2Q8%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2013&dateTo=2014&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rl4/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuuFZ7ABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEHKrfFSO%2F1AOwTCwNLoLRtkAAABA2QnULjmE1eBTyTwIZ8I1G%2B60fWM%2B%2FHBTHcIyYrnd4FAKwxAfvp60LlYhidR%2FHnjo2M0nlRtDRbuJuXpUBPRsqQAU0OXpXIP3oXo%2FHrNEBvWFgutC5Ks%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2014&dateTo=2015&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rlj/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuuL4MABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEHY70S7RtkdzuXlA1Jd%2FeIUAAABAvqVjPbOlZf6YixVMlxKm1TzyzkQ%2F%2F7PKqhATCZtODJY6s%2BSgqGEbOFPmAs4dXYgwx2W1i4tYsApW%2FKHgafRAWwAU1vvv52dA4%2Bc%2Fsffj4UPSEeVZpOg%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2015&dateTo=2016&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/roc/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuusfoABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEA9RJSzRld2qLAvQogqZFNUAAABAtfEVwfc1WSNkqvKeGJUSuV0FSHEnxrOqypP%2F%2FuHbpVl%2BIogRs55jlJ9T2H2NtsDo9e6r6wTIdtMygfa4Wu120QAUTVH3GNFa%2BMWpZW2vIO2kcsZ8UxM%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2016&dateTo=2017&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rp9/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuu7ckABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAENiKXBboFKRmB5co%2BbQU4akAAABADtpQi%2FAxzzmmlm%2B3AOuLAp%2FNEXXtIC2nPyEtPIAAP4CtlDFHpxVSXYWGxVT2nUUKP5dWSNVT0GZaHIVcQItMogAUn%2FEq0DTpflk4E1gnkJe4Mlvyd7A%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2017&dateTo=2018&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rpf/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuu9yJABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEGU6R1B9Ah%2FWet1O2ewQcEoAAABAqn5m01%2FtRU9X3SzMzbZJQUsvA1XlvXL6DK4%2Fsr49%2BGenf8E3lQwl%2BcP%2BIuvIdKugTOqSZTT7rX3TRMSQZIBpfAAUDWZgwPD53PkmI8n8mTQ%2BM9FTbPo%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2018&dateTo=2019&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche.x=0&standardsuche.y=0",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rps/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuvGGIABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAENN4Y9FGz1Pgd6jB3%2BQ%2BX%2BQAAABAKz0dclrPluT%2BkGlgWUwgwNUSJqkWjD2fNPdEEvaisY9KpD7oAsLRghSw33RIhUTins6Z8IQWU9ffSZOQi4sEHAAU9F1cShVfNsyzSfJHFskhwIaPln8%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2019&dateTo=2020&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern",
             "https://www.rechtsprechung-im-internet.de/jportal/portal/t/rqn/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkuvYjqABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEJVKlrHXFHOgv0w1BgdZYCAAAABA2%2FtYeNyeeSN6igfQVOkiEZhuK%2Fe12uaLcZETEyqOaR3L3BXW5xbOLi9C3gkscmxAyz8xWFJt1bbh00WVPiyBcQAUf3ec4dnEa1uE6zA7ya5yDSPyANc%3D&sugportalport=8080&sughashcode=-620594919789082084967272876330485839330001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=2020&dateTo=2021&desc=court_author&query=&desc=filenumber&sug_filenumber=&query=&standardsuche=Suche+verfeinern"
             ]

def click_next():
    '''
    clicking on "weiter" (next page) button
    '''
    driver.find_element_by_xpath('//*[@title="weiter"]').click()
    time.sleep(0.5)


lista_URLs = []
for url in startFrom:
    driver.get(url)  # first time set to starting_page_1900to2020, then insert URL of new date-based search (after scraping the initial 15.000 URLs)
    for i in range(700):  # database only shows 15.000 results for each query, divided into 700 pages
        click_next()
        elements = driver.find_elements_by_css_selector("[title*='Treffer Langtext']")
        for element in elements:
            lista_URLs.append(element.get_attribute("href"))


with open("URL_list_R.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(lista_URLs))

print("Done")





