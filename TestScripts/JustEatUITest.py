__author__ = "Priya Rajendira"
from selenium import webdriver
import unittest
#import HTMLTestRunner

""" By using Python Unittest framework this automation script successfully search and display the nearby restaurants in the area based on the postcode  """

class SearchPostCode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_searchPostCode(self):
        #load url
        self.driver.get("https://www.just-eat.co.uk")

        #passing the postcode search field
        self.driver.find_element_by_name("postcode").send_keys("AR51 1AA")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        searchResult=self.driver.find_element_by_xpath("//h1[@class='c-searchHeader']")
        #searchlist =self.driver.find_element_by_xpath("//h3[@class='c-listing-item-title']")
        searchInfo=self.driver.find_element_by_xpath("//div[@class='c-listing-item-info']")

        #display the number of search results
        print(searchResult.text)
        #print(searchlist.text)

        #display the sample search result info
        print(searchInfo.text)

    #Checking the page title by using assertion
    def test_title(self):
        self.assertEqual("Restaurants and takeaways in Area51, AR51 | Just Eat", self.driver.title)

    def test_altText(self):
        self.assertTrue()
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #use HTMLTestRunner to print the report, due to the version issues couldn't import HTMLTstRunner
    #unittest.main(testRunner=HTMLTestRunner.HTMLTestRuner(output='C:/Users/admin/PycharmProjects/SeleniumTest/Reports'))