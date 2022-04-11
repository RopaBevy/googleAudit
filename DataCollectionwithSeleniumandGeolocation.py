import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import time, os

# Set the driver path
driverpath ='./chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=driverpath, chrome_options=chrome_options)

def search_query(query, path):
    """
    This function can search Google by changing the location for 
    the search. Parameters:
    query - a string that contains the phrase that will be searched
    locationName - a string that is used to save the search results page
    coordinatesDict - a dictionary with the latitude, longitude, and accuracy
    """
    # Create a new instance of the driver for every search
    driver = webdriver.Chrome(executable_path=driverpath, 
                              options=chrome_options)
    
    # perform the search, because we need the location link to show
    url = f"https://google.com/search?q={query}"
    driver.get(url)

    sleep(2)

    # Access the content of the page
    htmlPage = driver.page_source
    
    with open(f"{path}/{query}.html", 'w', encoding='utf-8') as output:
        output.write(htmlPage)
        
    # close the instance
    driver.close()


def main():
    serp_path = 'serp_results'
    os.mkdir(serp_path)

    queries = []
    with open('rulhman_queries.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            q = row[0].lower().replace(' ', '+')
            queries.append(q)
    print(len(queries))
    for q in queries:
        search_query(q, serp_path)

if __name__ == '__main__':
    main()
