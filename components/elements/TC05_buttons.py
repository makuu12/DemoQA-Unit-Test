from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class buttons:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/buttons")
    
    def doubletClick(self): # Double click the button
        button = self.driver.find_element(By.ID, "doubleClickBtn")
        
        actions = ActionChains(self.driver)
        actions.double_click(button).perform()
        
        time.sleep(1)
        m = self.driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']").text
        print(f"Test 1: {'PASSED' if m == 'You have done a double click' else 'FAILED'}")
    
    def rightClick(self): # Right click the button
        button = self.driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
        
        actions = ActionChains(self.driver)
        actions.context_click(button).perform()
        
        m = self.driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
        print(f"Test 1: {'PASSED' if m == 'You have done a right click' else 'FAILED'}")
        
    def normalClick(self): # Click the third button
        button = self.driver.find_element(By.XPATH, "(//button[normalize-space()='Click Me'])[1]").click()
        
        m = self.driver.find_element(By.XPATH, "//p[@id='dynamicClickMessage']")
        print(f"Test 1: {'PASSED' if m == 'You have done a dynamic click' else 'FAILED'}")
        
if __name__ == "__main__":
    b = buttons()
    b.setup()
    time.sleep(5)
    b.doubletClick()
    b.rightClick()
    b.normalClick()