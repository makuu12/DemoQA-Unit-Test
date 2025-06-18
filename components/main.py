import time
from selenium import webdriver
from elements.TC01_textbox import textbox
from elements.TC02_checkbox import checkbox
from elements.TC03_radiobutton import raduobutton
from elements.TC05_buttons import buttons
from elements.TC06_links import links
from elements.TC07_brokenLinkImages import linkImg
from elements.TC08_File import DondownloadUpload 

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
# dapat demoqa lang then dapat ipupunta lang sa mga  menu



t = textbox()
t.setup()
time.sleep(3)
t.fillUp_Form()
t.test_data()

# Output:
# Name:mark
# Email:mark@gmail.com
# Current Address :test
# Permananet Address :test

rb = raduobutton()
rb.setup()
time.sleep(4)
rb.clickYes()
time.sleep(4)
rb.clickImpressive()
time.sleep(4)
rb.clickNo()











