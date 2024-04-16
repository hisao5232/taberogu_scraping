from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from time import sleep

chrome_options=Options()
#chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options=chrome_options)

driver.get("https://tabelog.com/")
sleep(1)


i=1

HREF_LIST=[]
while True:
    HREFS=driver.find_elements(By.CSS_SELECTOR, "")
    for HREF in HREFS:
        HREF_TITLE=HREF.get_attribute("href")
        HREF_LIST.append(HREF_LIST)
    print("[INFO] HREF_LIST :", HREF_LIST)
    try:
        driver.find_element(By.XPATH, '').click
        i += 1
        if i==5:
            break
    except:
        break
