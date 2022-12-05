# Importing the required packages 

import json
import urllib
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io
import requests
import time 
import pprint


chrome_options = Options()
chrome_options.binary_location="../Google Chrome"
chrome_options.add_argument("start-maximized")

range = 10

driver= webdriver.Chrome()
url = "https://en.wikipedia.org/wiki/Software_metric"


driver.get(url)
# time.sleep(100)
# driver.implicitly_wait(30)
result = "return window.performance.getEntries();"
result_2= driver.execute_script(result)
s = "".join(str(x) for x in result_2)
output = s.replace("\'", "\"")

print(result_2)
# time.sleep(100)
driver.quit()

with open("csv_file.csv", "w") as csv_file:
    csv_file.write(output)
   