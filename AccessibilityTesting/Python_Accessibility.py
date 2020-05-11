from selenium import webdriver
from axe_selenium_python import Axe
import unittest
import json

""" Tis script check the accessibility testing issues and logs all the accessibility issues on justEat.json file """


class test_accessibility(unittest.TestCase):
    with open('C:/Users/admin/PycharmProjects/SeleniumTest/AccessibilityTesting/URLEntries.json', encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')

    for i in data['urls']:
        driver.get(i["url"])
        axe = Axe(driver)

        # inject axe-core javascript into page.
        axe.inject()

        # Run axe accessibility checks.
        results = axe.run()

        # write results to file
        axe.write_results(results, i["file"])

        driver.close()

    if __name__ == "__main__":
      unittest.main()
