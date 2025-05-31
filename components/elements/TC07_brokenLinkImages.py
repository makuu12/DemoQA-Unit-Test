from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class linkImg:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/broken")
    
    def validImage(self): # Identify valid image
        valImg = self.driver.find_element(By.XPATH, "//img[1]")
        img_src = valImg.get_attribute("src")
        image_name = os.path.basename(img_src)
        # print(f"Test 1: {image_name}")
        print(f"Test 1: {img_src}")
        
    def brokenImage(self): # Identify broken image
        broImg = self.driver.find_element(By.XPATH, "//img[2]")
        img_src = broImg.get_attribute("src")
        image_name = os.path.basename(img_src)
        print(f"Test 2: {image_name}")
    
    def validLink(self): # Identify valid link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Click Here for Valid Link']").click()
        current_url = self.driver.current_url
        link = "https://demoqa.com/"
            
        print(f"Test 3: {True if current_url == link else False}")
        if current_url == link:
            self.driver.back()
            
    def brokenLink(self): # Identify broken link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Click Here for Broken Link']").click()
        current_url = self.driver.current_url
        link = "https://the-internet.herokuapp.com/status_codes/500"
        
        print(f"Test 4: {True if current_url == link else False}")
        if current_url == link:
            self.driver.back()

if __name__ == "__main__":
    li = linkImg()
    li.setup()
    time.sleep(5)
    li.validImage()
    time.sleep(2)
    li.brokenImage()
    time.sleep(2)
    li.validLink()
    time.sleep(2)
    li.brokenLink()