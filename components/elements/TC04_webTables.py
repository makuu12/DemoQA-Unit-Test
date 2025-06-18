from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
        self.driver.find_element(By.ID, "submit").click()
        
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
        
        # search_box = self.driver.find_element(By.XPATH, "//input[@id='searchBox']")
        # search_box.send_keys(Keys.CONTROL + "a") 
        # search_box.send_keys(Keys.DELETE)
        
        tRow = self.driver.find_element(By.XPATH, "//*[@class='rt-tr-group'][1]")
        text = tRow.text
        
        print(f"Test 1: {'PASSED' if "Alden" in text else 'FAILED'}")

    def editData(self): # Edit a data from the item
        self.driver.find_element(By.XPATH, "//span[@id='edit-record-1'][1]").click()
        
        text_fields = [
            webTables.txt1,
            webTables.txt2,
            webTables.txt3,
            webTables.txt4,
            webTables.txt5,
            webTables.txt6 
        ]

        for field_xpath in text_fields:
            field = self.driver.find_element(By.XPATH, field_xpath)
            field.send_keys(Keys.CONTROL + "a") 
            field.send_keys(Keys.DELETE)
        
        time.sleep(5)
        self.driver.find_element(By.XPATH, webTables.txt1).send_keys("Spongebob")
        self.driver.find_element(By.XPATH, webTables.txt2).send_keys("Squarepants")
        self.driver.find_element(By.XPATH, webTables.txt3).send_keys("spongebob@gmail.com")
        self.driver.find_element(By.XPATH, webTables.txt4).send_keys("23")
        self.driver.find_element(By.XPATH, webTables.txt5).send_keys("25000")
        self.driver.find_element(By.XPATH, webTables.txt6).send_keys("Finance")
        
        self.driver.find_element(By.XPATH, "//button[@id='submit']").click()
        
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='searchBox']").send_keys("Spongebob")
        
        tRow = self.driver.find_element(By.XPATH, "//*[@class='rt-tr-group'][1]")
        text = tRow.text
        
        print(f"Test 1: {'PASSED' if "Spongebob" in text else 'FAILED'}")
        
    def deleteData(self): # Search from the list data
        self.driver.find_element(By.XPATH, "//span[@id='delete-record-2']").click() # delete alden in the record
        
    def GetRecords(self): # Get all items from the table
        items = self.driver.find_elements(By.XPATH, "//*[@class='rt-tr-group']")
        for row in items:  
            cols = row.find_elements(By.CLASS_NAME, "rt-td")  # Get columns within the current row
            
            row_text = " | ".join([col.text.strip() for col in cols])  # Join column texts with " | "
            print(row_text)  # Print full row text

    def changeRows(self): # Change number of rows
        Opt = self.driver.find_element(By.XPATH, "//select[@aria-label='rows per page']")
        time.sleep(3)
        select = Select(Opt)
        select.select_by_visible_text("20 rows")
        
        rows = self.driver.find_elements(By.XPATH, "//*[@class='rt-tr-group']")
        items = len(rows)
        print(f"Test 1: {'PASSED' if items == 20 else 'FAILED'}")
        
    def AddMultipleRecords(self):  # Add multiple rows
        test_data = [
            ("Alice", "Smith", "alice.smith@example.com", "28", "25000", "HR"),
            ("Bob", "Johnson", "bob.johnson@example.com", "35", "32000", "Finance"),
            ("Charlie", "Brown", "charlie.brown@example.com", "40", "45000", "Engineering"),
            ("Diana", "Prince", "diana.prince@example.com", "30", "50000", "Marketing"),
            ("Ethan", "Hunt", "ethan.hunt@example.com", "38", "55000", "Security"),
            ("Fiona", "Davis", "fiona.davis@example.com", "25", "23000", "Design"),
            ("George", "White", "george.white@example.com", "29", "27000", "Operations"),
            ("Hannah", "Miller", "hannah.miller@example.com", "31", "29000", "Sales"),
            ("Ian", "Wright", "ian.wright@example.com", "27", "26000", "Support"),
            ("Jane", "Doe", "jane.doe@example.com", "24", "22000", "Research")
        ]

        for data in test_data:
            component = self.driver.find_element(By.ID, "addNewRecordButton")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", component)
            component.click()
            time.sleep(2)

            self.driver.find_element(By.XPATH, webTables.txt1).send_keys(data[0])  # First Name
            self.driver.find_element(By.XPATH, webTables.txt2).send_keys(data[1])  # Last Name
            self.driver.find_element(By.XPATH, webTables.txt3).send_keys(data[2])  # Email
            self.driver.find_element(By.XPATH, webTables.txt4).send_keys(data[3])  # Age
            self.driver.find_element(By.XPATH, webTables.txt5).send_keys(data[4])  # Salary
            self.driver.find_element(By.XPATH, webTables.txt6).send_keys(data[5])  # Department
        
            component = self.driver.find_element(By.ID, "submit")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", component)
            component.click()
            time.sleep(2)

            

    def nextprev(self): # Test the next and prev button
        # Add the AddMultipleRecords function first
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Previous')]").click()


if __name__ == "__main__":
    w = webTables()
    w.setup()
    time.sleep(5)
    w.AddMultipleRecords()
