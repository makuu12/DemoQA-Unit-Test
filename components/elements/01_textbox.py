from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class textbox:
    # -------------- Usage -------------- #
    # from TC01_LogIn import Login
    
    # l = Login() 
    # l.setup()           
    # l.login()           
    # l.close()  
    # -------------- Usage -------------- #
    
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
        vCAdd = ""
        vPAdd = ""
        self.driver.find_element(By.XPATH, "//input[@id='userName']").send_keys(vName)
        self.driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(vEmail)
        self.driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(vCAdd)
        self.driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(vPAdd)
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        
        
        main = self.driver.find_element(By.XPATH, "//div[@class='border col-md-12 col-sm-12']")
        name = main.find_element(By.XPATH, "//p[@id='name']")
        # email = main.find_element(By.XPATH, "//p[@id='email']")
        # cAdd = main.find_element(By.XPATH, "//p[@id='currentAddress']")
        # pAdd = main.find_element(By.XPATH, "//p[@id='permanentAddress']")
        
        print(f"Name: {'PASSED' if name.text == 'Name:{vName}' else 'FALSE'}")
        # print(f"Email: {'PASSED' if name.text == 'Name:{vEmail}' else 'FALSE'}")
        # print("Email: PASSED" if email.text == "Email:sad" else "The text is not correct.")
        # print("Email: PASSED" if cAdd.text == "Current Address:sad" else "The text is not correct.")
        # print("Email: PASSED" if pAdd.text == "Permanent Address:sad" else "The text is not correct.")


if __name__ == "__main__":
    t = textbox()
    t.setup()
    time.sleep(3)
    t.fillUp_Form()