"""This application calculates URL web console performance"""
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
import csv

myDictionary = defaultdict(list)
count = 1


class Measure_Performance:
    """This class has methods which perform the URL performance tests and produces the required reports"""
    def run(self):
        global count
        while count <= 10:

            # Webdriver configuration
            chrome_driver = webdriver.Chrome()
            web_url = "https://en.wikipedia.org/wiki/Software_metric"
            chrome_driver.get(web_url)
            output_query = chrome_driver.execute_script(
                "return window.performance.getEntries();"
            )
            chrome_driver.quit()
            
            for i in output_query:
                if i is not None:
                    myDictionary[i["name"]].append(i["duration"])
            count = count + 1

        for name, duration in myDictionary.items():
            if name is not None and duration is not None:
                myDictionary[name] = sum(duration) / float(len(duration))

            # This creates a JSON output file 
        with open("json_output.json", "w", encoding="utf-8") as json_file:
            json_object = json.dumps(myDictionary, indent=4)
            json_file.write(f'\n {{\n "avg_duration": {json_object}}}\n')
        
            # This creates a csv file
        with open("csv_output.csv", 'w') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in myDictionary.items():
                writer.writerow([key, value])


if __name__ == "__main__":
    myObj = Measure_Performance()

    myObj.run()
