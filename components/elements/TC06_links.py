from selenium import webdriver
from selenium.webdriver.common.by import By

class buttons:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://https://demoqa.com/buttons")
    
    def newTab(self): # normal click link to new tab
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    # API calls link handlers
    def created(self): 
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    def noContent(self): 
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    def moved(self): 
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    def badRequest(self):
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    def unauthorized(self):
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    def forbidden(self):
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
    def notFound(self):
        button = self.driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
        
