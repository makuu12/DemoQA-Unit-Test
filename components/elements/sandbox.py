from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FormValidator:
    ERROR_COLOR = "rgb(220, 53, 69)"  # Equivalent to #dc3545

    @staticmethod
    def validate_fields(driver, field_xpaths):
        """
        Checks if all specified fields have a red border (error validation).
        
        :param driver: Selenium WebDriver instance
        :param field_xpaths: List of XPaths for the input fields
        :return: True if all fields show an error, False otherwise
        
        usage
        fields = [list of text]
        result = FormValidator.validate_fields(driver, fields)
        """
        all_valid = True  # Assume all fields have an error

        for field_xpath in field_xpaths:
            field = driver.find_element(By.XPATH, field_xpath)
            border_color = field.value_of_css_property("border-color").strip()

            if border_color != FormValidator.ERROR_COLOR:
                all_valid = False  # If any field is not red, set to False

        return all_valid
    
    @staticmethod
    def clear_fields(driver, field_xpaths):
        """
        Checks if all specified fields have a red border (error validation).
        
        :param driver: Selenium WebDriver instance
        :param field_xpaths: List of XPaths for the input fields
        :return: True if all fields show an error, False otherwise
        
        usage:
        fields = [list of text]
        result = FormValidator.clear_fields(driver, fields)
        """

        for field_xpath in field_xpaths:
            field = driver.find_element(By.XPATH, field_xpath)
            field.send_keys(Keys.CONTROL + "a") 
            field.send_keys(Keys.DELETE)
    


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
        
    # Old ver
    # def AddWithoutData(self):
    #     error = "rgb(220, 53, 69)" # = #dc3545
        
    #     self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
    #     self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
    #     fName = self.driver.find_element(By.XPATH, webTables.txt1)
    #     lName = self.driver.find_element(By.XPATH, webTables.txt2)
    #     mail = self.driver.find_element(By.XPATH, webTables.txt3)
    #     age = self.driver.find_element(By.XPATH, webTables.txt4)
    #     salary = self.driver.find_element(By.XPATH, webTables.txt5)
    #     dept = self.driver.find_element(By.XPATH, webTables.txt6)
    #     border_color = fName.value_of_css_property('border-color')
    #     time.sleep(5)
        
    #     border_color = fName.value_of_css_property("border-color").strip()

    #     print(border_color)

    #     if border_color == error:
    #         print(False)
    
    def AddWithoutData(self):
        error = "rgb(220, 53, 69)" # = #dc3545
        
        self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        
        time.sleep(2)

        fields = [
            webTables.txt1,  # First Name
            webTables.txt2,  # Last Name
            webTables.txt3,  # Email
            webTables.txt4,  # Age
            webTables.txt5,  # Salary
            webTables.txt6   # Department
        ]
        result = FormValidator.validate_fields(self.driver, fields)
                
        print(f"Test 1: {'PASSED' if result else 'FAILED'}")

    
    def AddWithData(self):
        print("Click add and submit with valid data")
        self.driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']").click()
        
        
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        
    def editData(self): # Edit a data from the item
        self.driver.find_element(By.XPATH, "//span[@id='edit-record-1'][1]").click()
        fields = [
            webTables.txt1,  # First Name
            webTables.txt2,  # Last Name
            webTables.txt3,  # Email
            webTables.txt4,  # Age
            webTables.txt5,  # Salary
            webTables.txt6   # Department
        ]
        result = FormValidator.clear_fields(self.driver, fields)
        
    def submitForm():
        print("Edit a data from the item")
        
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
    w.editData()