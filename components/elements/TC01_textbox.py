from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import time


class textbox:


    vName = "mark"
    vEmail = "mark@gmail.com"
    vCAdd = "test"
    vPAdd = "test"
    
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = EdgeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")
        
    def fillUp_Form(self):
        self.driver.find_element(By.XPATH, "//input[@id='userName']").send_keys(self.vName)
        self.driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(self.vEmail)
        self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(self.vCAdd)
        self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(self.vPAdd)
        time.sleep(5)
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
    t = textbox()
    t.setup()
    time.sleep(3)
    t.fillUp_Form()
    t.test_data()