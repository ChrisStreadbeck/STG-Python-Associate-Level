import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")
        self.driver.find_element(By.ID, "input-search").send_keys('exotics', Keys.ENTER)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))
        self.assertIn("PORSCHE", element.text)


if __name__ == '__main__':
    unittest.main()
