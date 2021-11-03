import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('window-size=800,400')

navegador = webdriver.Chrome(options=options)

navegador.get('https://www.loja.panini.com.br')

sleep(2)

input_place = navegador.find_element_by_tag_name('input')
input_place.send_keys('berserk')
input_place.submit()

