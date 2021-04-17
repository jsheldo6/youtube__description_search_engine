
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

# unittest is a package for testing in python
# this is by default included in python
import unittest
import time

class HomeTest(unittest.TestCase):

    # override method setup
    def setUp(self):
        #automatically executed before test starts
        PATH="chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_title(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.assertIn("381 Youtube Search",self.driver.title)

    def test_link(self):
        self.driver.get("http://127.0.0.1:5000/")
        link = self.driver.find_element_by_link_text("link")
        link.send_keys(Keys.RETURN)
        self.assertIn("Query",self.driver.page_source)
        self.assertIn("no search results",self.driver.page_source)

if __name__ =="__main__":
    unittest.main()
