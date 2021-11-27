# Import all modules
from selenium import webdriver # It is used to interact with the web page - login and logout functionality, click any button, and other things
from bs4 import BeautifulSoup  # bs4 is used for passing text as HTML and then performing actions - finding html tags or list tags
import time
import csv

# Url for website
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("/Users/Rajjo/Python/C127/chromedriver")
browser.get(START_URL)
time.sleep(10)

# Scraping the data function
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # Find the tags for retrieving the data
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            # Enumerate is used to return index along with the elements
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        # XPath can be used to navigate through elements and attributes in an xml document
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:\
        # Make a csv file
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
