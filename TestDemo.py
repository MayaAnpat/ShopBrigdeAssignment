#Question No3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pytest
@pytest.fixture()
def setUp():
    driver = webdriver.Chrome(executable_path="C:\Drivers\ChromeDriver\chromedriver_win32\chromedriver.exe")
    return driver

def test_validateDropDown(setUp):
    driver = setUp
    driver.get("https://jt-dev.azurewebsites.net/#/SignUp")
    driver.implicitly_wait(10)
    drpElement=driver.find_element(By.XPATH,"//div[@placeholder='Choose Language']//span[@class='ui-select-match-text pull-left']").click()
    time.sleep(5)
    drpElements = driver.find_elements(By.XPATH, "//div/a")
    print(len(drpElements))
    actualDropDown = []
    for element in drpElements:
        actualDropDown.append(element.text)
    actualDropDown.pop(0)
    expectedDropDown = ['English', 'Dutch']
    for i in actualDropDown:
        assert i in expectedDropDown, "Validation fail"
        print("validation pass")
    driver.close()
def test_validateOtherfield(setUp):
    driver = setUp
    driver.get("https://jt-dev.azurewebsites.net/#/SignUp")
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"name").send_keys("Maya")
    driver.find_element(By.XPATH, "//*[@id='orgName']").send_keys("Maya Anapt")
    driver.find_element(By.ID,"singUpEmail").send_keys("mayaanpat13@gmail.com")
    driver.find_element(By.XPATH,"//span[@class='black-color ng-binding']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@class='form-group custom-form-group']").click()
    driver.close()