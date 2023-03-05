from selenium import webdriver
import time
import json

def scrape_website(url, class_name):
    # create a new browser window
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    # navigate to the website
    driver.get(url)

    # wait for 5 seconds to let the page load
    time.sleep(5)

    # locate the elements with the class name
    elements = driver.find_elements_by_xpath(f"//a[@class='{class_name}']")

    # create an empty list to store the data
    data = []

    # iterate through the elements and get the href and text
    for element in elements:
        title = element.text
        link = element.get_attribute("href")

        # create a dictionary with the data
        item = {"title": title, "link": link}

        # add the dictionary to the data list
        data.append(item)

    # write the data to a json file
    with open("data.json", "w") as f:
        json.dump(data, f)

    # close the browser
    driver.quit()

# usage:
scrape_website("https://WEBSITE_URL/", "Link--primary")
