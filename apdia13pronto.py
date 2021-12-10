import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from time import sleep

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)

def scraping(url, pesq):
    browser.get(url)
    url = BeautifulSoup(browser.page_source, 'html.parser')
    searchbtn = browser.find_element(By.ID, 'header-search-section').click()
    inp = browser.find_element(By.ID, 'header-search-input')
    sleep(3.0)
    txt = inp.send_keys(pesq)
    sleep(3.0)
    inp2 = browser.find_element(By.ID, 'header-search-input')
    inp2.send_keys(Keys.RETURN)
    text1 = browser.find_element(By.TAG_NAME, 'p')
    text2 = browser.find_element(By.CLASS_NAME, 'widget--info__description')
    print(text2.text)
    return text2 



valor = scraping('https://www.globo.com/', 'agricultura')
