import json
import urllib
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io
from statistics import mean
from collections import defaultdict
import requests
import time 
import pprint

myDict = defaultdict(list)
count = 1


class Measure_Performance:
    def run(self):
        global count
        while count <= 10:

            chrome_options = Options()
            chrome_options.binary_location="../Google Chrome"
            chrome_options.add_argument("start-maximized")
            chrome_driver = webdriver.Chrome()
            url = "https://en.wikipedia.org/wiki/Software_metric"
            chrome_driver.get(url)
            out_query = chrome_driver.execute_script(
                "return window.performance.getEntries();"
            )
            chrome_driver.quit()

            for i in out_query:
                if i is not None:
                    myDict[i["name"]].append(i["duration"])
            count = count + 1

        for name, duration in myDict.items():
            if name is not None and duration is not None:
                myDict[name] = sum(duration) / float(len(duration))

        with open("json_output.json", "w", encoding="utf-8") as csv_file:
            json_object = json.dumps(myDict, indent=4)
            csv_file.write(f'\n {{\n "avg_duration": {json_object}}}\n')


if __name__ == "__main__":
    myObj = Measure_Performance()

    myObj.run()