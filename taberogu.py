from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

chrome_options=Options()
#chrome_options.add_argument('--headless')
driver=webdriver.Chrome(options=chrome_options)

urls=[]
detail_list=[]

def search(keyword):
    driver.get("https://tabelog.com/")
    elem=driver.find_element(By.ID,"sk")
    elem.send_keys(keyword)
    elem.send_keys(Keys.ENTER)
    #driver.find_element(By.ID,"js-global-search-btn").click()
    sleep(2)
    s_hrefs=get_url()
    for s_href in s_hrefs:
        driver.get(s_href)
        sleep(2)
        get_detail()

    sleep(3)
    
    #page_nation()

    df=pd.DataFrame(detail_list)
    df.to_excel("taberogu_deta.xlsx")

def page_nation():
    while True:
        try:
            driver.find_element(By.CSS_SELECTOR,"li.c-pagination__item > a.c-pagination__arrow--next").click()
            sleep(2)
        except:
            break

def get_url():
    hrefs=driver.find_elements(By.CSS_SELECTOR,"a.list-rst__rst-name-target")
    for href in hrefs:
        url=href.get_attribute("href")
        urls.append(url)

    return urls

def get_detail():
    shop_name=driver.find_element(By.CSS_SELECTOR,"div.rstinfo-table__name-wrap").text
    ster=driver.find_element(By.CSS_SELECTOR,"span.rdheader-rating__score-val-dtl").text
    try:
        janru=driver.find_element(By.XPATH,"descendant::th[contains(text(),'ジャンル')]/following-sibling::td").text
    except:
        janru="なし"
    try:
        phone_num=driver.find_element(By.XPATH,"descendant::th[contains(text(),'予約・')]/following-sibling::td").text
    except:
        phone_num="なし"
    adress=driver.find_element(By.CSS_SELECTOR,"p.rstinfo-table__address").text
    try:
        hp=driver.find_element(By.CSS_SELECTOR,"p.homepage>a>span").text
    except:
        hp="なし"

    d_detail={'shop_name':shop_name,'評価（星）':ster,'ジャンル':janru,'電話番号':phone_num,'住所':adress,'ホームページ':hp}
    detail_list.append(d_detail)

if __name__ == "__main__":
    search("焼肉")