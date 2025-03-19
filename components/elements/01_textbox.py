from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class textbox:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")
        
    def fillUp_Form(self):
        vName = "mark"
        vEmail = "mark@gmail.com"
        vCAdd = "test"
        vPAdd = "test"
        self.driver.find_element(By.XPATH, "//input[@id='userName']").send_keys(vName)
        self.driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(vEmail)
        self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(vCAdd)
        self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(vPAdd)
        time.sleep(5)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
        
        time.sleep(5)
        main = self.driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
        name = main.find_element(By.XPATH, "//p[@id='name']")
        email = main.find_element(By.XPATH, "//p[@id='email']")
        cAdd = main.find_element(By.XPATH, "//p[@id='currentAddress']")
        pAdd = main.find_element(By.XPATH, "//p[@id='permanentAddress']")
        
        print(f"Name: {'PASSED' if name.text == f'Name:{vName}' else 'FALSE'}")
        print(f"Email: {'PASSED' if email.text == f'Name:{vEmail}' else 'FALSE'}")
        print(f"Contact Address: {'PASSED' if cAdd.text == f'Name:{vCAdd}' else 'FALSE'}")
        print(f"Permanent Address: {'PASSED' if pAdd.text == f'Name:{vPAdd}' else 'FALSE'}")


if __name__ == "__main__":
    t = textbox()
    t.setup()
    time.sleep(3)
    t.fillUp_Form()