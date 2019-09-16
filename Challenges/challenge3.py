import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge3forloop(self):
        self.driver.get("https://www.copart.com")
        webelements = self.driver.find_elements(By.XPATH, '//*[@ng-if=\"popularSearches\"]//a')
        for x in webelements:
            print(x.text + " - " + x.get_attribute("href"))

    def test_challenge3WhileLoop(self):
        self.driver.get("https://www.copart.com")
        webelements = self.driver.find_elements(By.XPATH, '//*[@ng-if=\"popularSearches\"]/../div[3]//li/a')

        count = 0
        print(len(webelements))
        while count < len(webelements):
            print(webelements[count].text + " - " + webelements[count].get_attribute("href"))
            count = count + 1


if __name__ == '__main__':
    unittest.main()