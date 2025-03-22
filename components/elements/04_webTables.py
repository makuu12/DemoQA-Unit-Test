from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class webTables:
    txt1 = "//input[@id='firstName']"
    txt2 = "//input[@id='lastName']"
    txt3 = "//input[@id='userEmail']"
    txt4 = "//input[@id='age']"
    txt5 = "//input[@id='salary']"
    txt6 = "//input[@id='department']"
    
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/webtables")
        
    def AddWithoutData(self):
        error = "rgb(220, 53, 69)" # = #dc3545
        
        self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        
        time.sleep(2)

        text_fields = [
            webTables.txt1,
            webTables.txt2,
            webTables.txt3,
            webTables.txt4,
            webTables.txt5,
            webTables.txt6 
        ]

        all_valid = True 

        for field_xpath in text_fields:
            field = self.driver.find_element(By.XPATH, field_xpath)
            border_color = field.value_of_css_property("border-color").strip()
            # print(f"Field: {field_xpath} -> Border Color: {border_color}")  # Debugging

            if border_color != error:
                all_valid = False
                
        print(f"Test 1: {'PASSED' if all_valid else 'FAILED'}")
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='close']").click()

    def AddWithInvalidData(self): # Click add and submit with invalid data
        self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, webTables.txt1).send_keys("")
        self.driver.find_element(By.XPATH, webTables.txt2).send_keys("")
        self.driver.find_element(By.XPATH, webTables.txt3).send_keys("Doe")
        self.driver.find_element(By.XPATH, webTables.txt4).send_keys("sad")
        self.driver.find_element(By.XPATH, webTables.txt5).send_keys("sad")
        self.driver.find_element(By.XPATH, webTables.txt6).send_keys("")
        
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='close']").click()

    def AddWithData(self): # Click add and submit with valid data
        self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, webTables.txt1).send_keys("John")
        self.driver.find_element(By.XPATH, webTables.txt2).send_keys("Doe")
        self.driver.find_element(By.XPATH, webTables.txt3).send_keys("Doe@gmail.com")
        self.driver.find_element(By.XPATH, webTables.txt4).send_keys("22")
        self.driver.find_element(By.XPATH, webTables.txt5).send_keys("18000")
        self.driver.find_element(By.XPATH, webTables.txt6).send_keys("IT")
        
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()

    def search(self): # Search from the list data
        self.driver.find_element(By.XPATH, "//input[@id='searchBox']").send_keys("alden")
        
        search_box = self.driver.find_element(By.XPATH, "//input[@id='searchBox']")
        search_box.send_keys(Keys.CONTROL + "a") 
        search_box.send_keys(Keys.DELETE)
        
        tRow = self.driver.find_element(By.XPATH, "//*[@class='rt-tr-group'][1]")
        text = tRow.text.lower()
        
        print(f"Test 1: {'PASSED' if "alden" in text else 'FAILED'}")

    def editData(self): # Edit a data from the item
        self.driver.find_element(By.XPATH, "//span[@id='edit-record-1'][1]").click()
        
    def submitForm():
        print("Delete a data from the item")
        
    def submitForm():
        print("Get all items from the table")

    def submitForm():
        print("Change number of rows")
        


if __name__ == "__main__":
    w = webTables()
    w.setup()
    time.sleep(5)
    w.search()