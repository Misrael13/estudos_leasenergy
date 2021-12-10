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
    click2 = browser.find_element(By.ID, 'header-search-section').click()
    txt.send_keys(Keys.ENTER)

valor = scraping('https://www.globo.com/', 'agricultura')
