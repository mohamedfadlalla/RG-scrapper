from selenium import webdriver
from bs4 import BeautifulSoup as bs

from datetime import datetime
start = datetime.now()
# some kind of code

# import pandas as pd

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
browser = webdriver.Chrome(options=chrome_options)

url = r'https://www.researchgate.net/profile/Mohamed-Elbadawi/research'


browser.get(url)

soup = bs(browser.page_source, features="lxml")

match = soup.find('div', class_='nova-legacy-o-stack__item')
title = match.text

#extracting publications
div = soup.find_all(class_='nova-legacy-e-link nova-legacy-e-link--color-inherit nova-legacy-e-link--theme-bare')
# for match in div:
#     print(match.text)
#     print()
    

#Additional affiliations
matches = soup.find_all(class_='nova-legacy-v-job-item__stack-item')
for match in matches:
    print(match.text)
    print()

print(datetime.now() - start)
browser.quit()
