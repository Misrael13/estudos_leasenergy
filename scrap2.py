import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

def scraping(url, el_src, el_type = By.ID):
    browser.get(url)
    BeautifulSoup(browser.page_source, 'html.parser')
    sleep(5.0)
    tag_enc2 = browser.find_element(el_type, el_src)
    return tag_enc2.text.replace(',' , '.')[:7]

valor1 = scraping('https://controlemais.com.br/monitoramento/medidor/1128', 'consumo-kwh')
sleep(1.5)
# valor2 = scraping('https://www.globo.com/', 'homeui-tc-podcasts', By.CLASS_NAME)
v1 = float(valor1)
print('\033[33m' 'o valor em kwh é', v1, '\033[m')
# print('\033[32m', valor2, '\033[m' )