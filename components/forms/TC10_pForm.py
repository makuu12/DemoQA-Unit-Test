from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
import pyautogui


class practiceForm:
    
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = EdgeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        
    def fillUp_Form(self):
        self.driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("John")
        self.driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Doe")
        self.driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("jdoe@gmail.com")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Male'][1]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='userNumber']").send_keys("9091234567")

        # Datepicker is not working for now
        # time.sleep(5)
        # bdate = self.driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
        # date_value = "01 Jan 2000"
        # self.driver.execute_script("document.getElementById('dateOfBirthInput').value = arguments[0]", date_value)
        # time.sleep(2)
        # bdate.send_keys(Keys.RETURN)
        # print("date entered")
        time.sleep(5)
        
        subjects = self.driver.find_element(By.CLASS_NAME, "subjects-auto-complete__value-container")
        # subjects.click()
        time.sleep(5)
        subjects.driver.find_element(By.ID, "subjectsInput").send_keys("Eng", Keys.ENTER)
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//label[normalize-space()='Sports']").click()

        file_input = self.driver.find_element(By.XPATH, "//input[@id='uploadPicture']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", file_input)
        file = os.path.abspath("components/resources/1x1.png")
        file_input.send_keys(file)
        time.sleep(3)

        
        
        self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("trytry")

        Opt = self.driver.find_element(By.XPATH, "//div[contains(text(),'Select State')]")
        time.sleep(3)
        select = Select(Opt)
        select.select_by_visible_text("NCR")

        Opt = self.driver.find_element(By.XPATH, "//div[contains(text(),'Select City')]")
        time.sleep(3)
        select = Select(Opt)
        select.select_by_visible_text("Delhi")

        submit = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit)
        submit.click()
        
    def test_data(self):
        time.sleep(5)

        
        main = self.driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
        name = main.find_element(By.XPATH, "//p[@id='name']")
        email = main.find_element(By.XPATH, "//p[@id='email']").text
        cAdd = main.find_element(By.XPATH, "//p[@id='currentAddress']").text
        pAdd = main.find_element(By.XPATH, "//p[@id='permanentAddress']").text
        
        print("Test Data")
        print(f"Test 1: {'PASSED' if name.text == f'Name:{self.vName}' else 'FALSE'}")
        print(f"Test 2: {'PASSED' if email == f'Email:{self.vEmail}' else 'FALSE'}")
        print(f"Test 3: {'PASSED' if cAdd == f'Current Address :{self.vCAdd}' else 'FALSE'}")
        print(f"Test 4: {'PASSED' if pAdd == f'Permananet Address :{self.vPAdd}' else 'FALSE'}")

if __name__ == "__main__":
    t = practiceForm()
    t.setup()
    time.sleep(3)
    t.fillUp_Form()
    # t.test_data()