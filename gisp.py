import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import shutil
from time import sleep

searchterm = input('Input image tags via spacebar (besides it will be the name of the folder with images): ')
url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
browser = webdriver.Firefox(executable_path='/Volumes/Apple HD/Users/sm00th/Documents/Python/geckodriver/geckodriver')
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
counter = 0
succounter = 0

if not os.path.exists(searchterm):
    os.mkdir(searchterm)

for _ in range(500):
    browser.execute_script("window.scrollBy(0,10000)")

for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
    counter = counter + 1
    print("Total Count:", counter)
    print("Succsessful Count:", succounter)
    print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

    img = json.loads(x.get_attribute('innerHTML'))["ou"]
    imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
    
    try:
        response = requests.get(img, stream=True, headers=header)
        File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
        File.write(response.raw.read())
        File.close()
        succounter = succounter + 1
        del response
        sleep(5)
    except:
            print("can't get img")

print(succounter, "pictures succesfully downloaded")
browser.close()