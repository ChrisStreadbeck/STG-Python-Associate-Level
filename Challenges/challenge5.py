import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.maximize_window()
        self.driver.get("https://www.copart.com")
        self.driver.find_element(By.ID, "input-search").send_keys('porsche', Keys.ENTER)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "tbody")))

        # self.driver.findElement(By.XPATH, "//select[@aria-controls=\"serverSideDataTable_length\"]").click()
        dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
        dropdown.find_element(By.XPATH, "//option[. = '100']").click()
        self.driver.find_element(By.NAME, "serverSideDataTable_length").click()

        # to find the wait spinner
        self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable_processing\"]")
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_processing\"]")))

        # find Models - returns an array
        model_list = self.driver.find_elements(By.XPATH, "//span[@data-uname=\"lotsearchLotmodel\"]")
        damaged_car_list = self.driver.find_elements(By.XPATH, "//span[@data-uname=\"lotsearchLotdamagedescription\"]")

        # add models to list
        models_list = []
        for model in model_list:
            models_list.append(model.text)
            count = [[model, models_list.count(model)] for model in set(models_list)]
        print(count)

        # find damaged list - only want => ("REAR END", "FRONT END", "MINOR DENT/SCRATCHES", "UNDERCARRIAGE")
        damages = {
            "REAR END": 0,
            "FRONT END": 0,
            "MINOR DENT/SCRATCHES": 0,
            "UNDERCARRIAGE": 0,
            "All Other": 0
        }

        for damage_type in damaged_car_list:
            if damage_type.text == "REAR END":
                damages["REAR END"] += 1
            elif damage_type.text == "FRONT END":
                damages["FRONT END"] += 1
            elif damage_type.text == "MINOR DENT/SCRATCHES":
                damages["MINOR DENT/SCRATCHES"] += 1
            elif damage_type.text == "UNDERCARRIAGE":
                damages["UNDERCARRIAGE"] += 1
            else:
                damages["All Other"] += 1
        for attribute, value in damages.items():
            print(f'{attribute} : {value}')


if __name__ == '__main__':
    unittest.main()