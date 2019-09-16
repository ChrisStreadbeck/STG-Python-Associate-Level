import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")

        try:
            self.driver.find_element(By.ID, "input-search").send_keys('nissan skylinegtq', Keys.ENTER)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))

            # self.driver.findElement(By.XPATH, "//select[@aria-controls=\"serverSideDataTable_length\"]").click()
            dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
            dropdown.find_element(By.XPATH, "//option[. = '100']").click()
            self.driver.find_element(By.NAME, "serverSideDataTable_length").click()

            # to find the wait spinner
            self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable_processing\"]")
            WebDriverWait(self.driver, 60).until(
                EC.invisibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_processing\"]")))

            model_list = self.driver.find_elements(By.XPATH, "//span[@data-uname=\"lotsearchLotmodel\"]")

        except:
            self.driver.save_screenshot("../screenshots/error.png")
            print("Screenshot saved to the screenshots folder")


if __name__ == '__main__':
    unittest.main()
