
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import sqlite3
from datetime import datetime

binary = '/usr/bin/firefox'
options = webdriver.FirefoxOptions()
options.binary = binary
options.add_argument('start-maximized')
options.add_argument('--headless')
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
browser = webdriver.Firefox(options=options, executable_path='/usr/bin/geckodriver')


soup = bs(browser.page_source, features="lxml")
conn = sqlite3.connect('RG-DB.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Pages (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT)')

cur.execute('INSERT OR IGNORE INTO Pages (url, html) VALUES ( ?, ? )', ( url, browser.page_source) )


while True:
    cur.execute('SELECT id,url FROM Pages WHERE html is NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cur.fetchone()
        # print row
        fromid = row[0]
        url = row[1]
    except:
        print('No unretrieved HTML pages found')
        many = 0
        break
        
    try:
        browser.get(url)
        soup = bs(browser.page_source, features="lxml")
        cur.execute('UPDATE Pages SET html=? WHERE url=?', (browser.page_source, url ))
        conn.commit()
    except:
        cur.execute('UPDATE Pages SET html=? WHERE url=?', (-1, url ))
    
    try:
        match = soup.find_all('a')
        for i in match:
            try:
                if i['href'].startswith('https://www.researchgate.net/profile'):
                    cur.execute('INSERT OR IGNORE INTO Pages (url, html) VALUES ( ?, NULL )', ( i['href'], ) )
                    conn.commit()
            except KeyError:
                pass
    except AttributeError:
        pass

