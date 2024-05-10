from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://tabelog.com/")
time.sleep(2)

driver.find_element(By.ID,"sk").send_keys("焼肉")
driver.find_element(By.ID,"js-global-search-btn").click()
time.sleep(3)

shop_list_elem=driver.find_elements(By.CSS_SELECTOR,"div > h3 > a.list-rst__rst-name-target")
href=shop_list_elem[0].get_attribute("href")
print(href)
driver.get(href)
time.sleep(2)

shop_name=driver.find_element(By.CLASS_NAME,"display-name").text
print(shop_name)

ster=driver.find_element(By.CLASS_NAME,"rdheader-rating__score-val-dtl").text
print(ster)

address=driver.find_element(By.CLASS_NAME,"rstinfo-table__address").text
print(address)

price=driver.find_element(By.CLASS_NAME,"rdheader-budget__price-target").text
print(price)

janru=driver.find_element(By.CSS_SELECTOR," table.c-table > tbody > tr > td > span").text
print(janru)

time.sleep(2)

driver.quit()