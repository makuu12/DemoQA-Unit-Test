from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os

class DondownloadUpload:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/upload-download")
    
    def downloadFile(self): # Download file
        self.driver.find_element(By.XPATH, "//a[@id='downloadButton']").click()
    
    def uploadFile(self): # Upload file
        file_input = self.driver.find_element(By.XPATH, "//input[@id='uploadFile']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", file_input)
        file = os.path.abspath("components/resources/1x1.png")
        file_input.send_keys(file)
        print("file imported")
        
if __name__ == "__main__":
    du = DondownloadUpload()
    du.setup()
    time.sleep(5)
    du.uploadFile()