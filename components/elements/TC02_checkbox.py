from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

class checkbox:
    def __init__(self):
        self.driver = None
        
    def setup(self):
        options = EdgeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/checkbox")
        
    def ExpandAll(self):
        
        box = self.driver.find_element(By.XPATH, "//button[@title='Expand all']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", box)
        box.click()

    def CollapseAll(self):
        self.driver.find_element(By.XPATH, "//button[@title='Collapse all']").click()
        
    def ExpandCollapse(self): # Expand and Collapse and uncollapse manually
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//button[@title='Toggle'])[1]").click()
        self.driver.find_element(By.XPATH, "(//button[@title='Toggle'])[2]").click()
        self.driver.find_element(By.XPATH, "(//button[@title='Toggle'])[3]").click()
        self.driver.find_element(By.XPATH, "(//button[@title='Toggle'])[4]").click()
        
    def SelectUnselectAll(self):
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-uncheck'])[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='rct-icon rct-icon-check'])[1]").clicck()
        
    def Branches(self): # (Desktop, Documents, Downloads)
        # Select all branches manually
        time.sleep(3) 
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Desktop')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Documents')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()

        # Unselect all branches
        self.driver.find_element(By.XPATH, "(//button[@title='Toggle'])[1]").click()
        time.sleep(2)      
        self.driver.find_element(By.XPATH, "(//button[@title='Toggle'])[1]").click()                 
    
    def SubBranches(self): # (Notes, Workspace, Word File.doc)
        time.sleep(3)  
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Notes')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'WorkSpace')]").click()

        self.driver.find_element(By.XPATH, "//span[contains(text(),'Downloads')]").click()
        self.driver.find_element(By.XPATH, "//li[3]//span[1]//button[1]//*[name()='svg']").click()

        self.driver.find_element(By.XPATH, "//span[contains(text(),'Word File.doc')]").click()
        
        output = self.driver.find_element(By.XPATH, "//div[@id='result']")
        expected_text = "You have selected :\nnotes\nworkspace\nreact\nangular\nveu\nwordFile"
        if output.text.strip() == expected_text.strip():
            print(True)
        else:
            print(False)
        
        # Unselect items manually 
        time.sleep(3)  
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Notes')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'WorkSpace')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Word File.doc')]").click()

if __name__ == "__main__":
    c = checkbox()
    c.setup()
    c.ExpandAll()
    c.CollapseAll()
    c.ExpandCollapse()
    c.SelectUnselectAll()
    # c.Branches()
    # c.SubBranches()