from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class raduobutton:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/radio-button")
    
    def clickYes(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()
        time.sleep(4)
        label = self.driver.find_element(By.XPATH, "//span[@class='text-success']")
        text = label.text
        data = "Yes"
        print(f"Test 1: {'PASSED' if text == f'Name:{data}' else 'FALSE'}")
    
    def clickImpressive(self):
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Impressive']").click()
        time.sleep(4)
        label = self.driver.find_element(By.XPATH, "//span[@class='text-success']")
        text = self.driver.execute_script("return arguments[0].textContent;", label).strip()
        print(text)
        data = "Impressive"
        print(f"Test 2: {'PASSED' if text == f'Name:{data}' else 'FALSE'}")
        
    def clickNo(self): # Still not working
        print("Enable 'No' button then select")
        rbNo = self.driver.find_element(By.XPATH, "//div[@class='custom-control disabled custom-radio custom-control-inline']")
        self.driver.execute_script("arguments[0].click();", rbNo)
        # rbNo.click()
        label = self.driver.find_element(By.XPATH, "//span[@class='text-success']")
        text = label.text
        data = "No"
        print(f"Test 2: {'PASSED' if text == f'Name:{data}' else 'FALSE'}")

if __name__ == "__main__":
    rb = raduobutton()
    rb.setup()
    time.sleep(4)
    rb.clickYes()
    time.sleep(4)
    rb.clickImpressive()
    time.sleep(4)
    rb.clickNo()

