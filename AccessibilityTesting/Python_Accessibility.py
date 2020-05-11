from selenium import webdriver
from axe-selenium-python import Axe
#unable to install axe-selenium packages due to the pip version

import time
import unittest
import json

""" Tis script check the accessibility testing issues and logs all the accessibility issues on justEat.json file """
class test_accessibility(unittest.TestCase):
    with open('C:/Users/admin/PycharmProjects/SeleniumTest/AccessibilityTesting/URLEntries.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())


        driver = webdriver.Chrome(executable_path='../Drivers/geckodriver.exe')

        for i in data['urls']:
            driver.get(i["urls"])
            axe = Axe(driver)

            #inject axe-core javascript into page.
            axe.inject()

            #Run axe accessibility checks.
            results = axe.run()

            #write results to file
            axe.write_results(results, i["file"])

        driver.close()

    if __name__ =="__main__":
        unittest.main()