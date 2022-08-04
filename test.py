#test and calculate preformance

##third party
import selenium_setup
from bs4 import BeautifulSoup as bs

##built in
import sqlite3
from datetime import datetime

##local
import extraction as ex
import db.setup as db
from db.insert import InsertError
import API 


DB_NAME = 'RG-DB.sqlite'

browser = selenium_setup.SetupBrowser()
# conn2, cur2 = db.Setup(DB_NAME)

url = r'https://www.researchgate.net/publication/353246555_Anti-hepatitis_B_activities_of_Myanmar_medicinal_plants_a_narrative_review_of_current_evidence'
browser.get(url)
soup = bs(browser.page_source, features="lxml")

API.Collect_Email(soup)


