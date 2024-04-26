#https://github.com/TaukirSumer/KM_Scrape.git

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

# Set Chrome options (optional)
options = Options()
options.headless = True  

driver = webdriver.Chrome(options=options)
driver.get("https://www.msamb.com/ApmcDetail/APMCPriceInformation#DistrictCommodityGird")
driver.maximize_window()
time.sleep(5)

element = driver.find_element(By.ID,"APMCTitle")
element.click()
time.sleep(3)

element1 = driver.find_element(By.XPATH,"//a[@title='District Commodity Wise']")
element1.click()
time.sleep(3)

dropdown_element=driver.find_element(By.NAME,'drpDistrictCommodity')
dropdown_select = Select(dropdown_element)
time.sleep(5)
print("End")
dropdown_select.select_by_visible_text('WARDHA')
time.sleep(15)


tbody = driver.find_element(By.XPATH,'//*[@id="tblDistrictCommodityGird"]')

listt=[]

for tr in tbody.find_elements(By.XPATH,'//tr'):
    rows =[item.text for item in tr.find_elements(By.XPATH,'.//td')]
    listt.append(rows)


headers = ["Commodity", "Variety", "Unit", "Quantity", "Low Rate", "High Rate", "Modal"]

df = pd.DataFrame(listt, columns=headers)

df.to_excel("output.xlsx", index=False)

driver.quit()