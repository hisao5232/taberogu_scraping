from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options=Options()
#chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options=chrome_options)

def search(keyword):
    driver.get("https://tabelog.com/")
    elem=driver.find_element(By.ID,"sk")
    elem.send_keys(keyword)
    elem.send_keys(Keys.ENTER)
    #driver.find_element(By.ID,"js-global-search-btn").click()
    sleep(2)
    page_nation()

def page_nation():
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR,"li.c-pagination__item > a.c-pagination__arrow--next").click()
        except:
            break

if __name__ == "__main__":
    search("焼肉")