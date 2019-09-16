import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()
        webelements = self.driver.find_elements(By.XPATH, '//*[@ng-if=\"popularSearches\"]//a')

        make = []
        link = []
        for x in webelements:
            make.append(x.text)
            link.append(x.get_attribute("href"))

        two_d_array = zip(make, link)

        for each in two_d_array:
            self.driver.get(each[1])
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
            self.assertIn(each[0], element.text)
            print(f'{each[0]} was in {each[1]}')


if __name__ == '__main__':
    unittest.main()
