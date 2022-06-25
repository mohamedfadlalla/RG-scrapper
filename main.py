##third party
import selenium_setup
from bs4 import BeautifulSoup as bs

##built in
import sqlite3
 
##local
import extraction as ex
import db.setup as db
from db.insert import InsertError
import API 




DB_NAME = 'RG-DB.sqlite'
RESUME = False

if RESUME == False:
	### kickstart crowlar
	browser = selenium_setup.SetupBrowser()
	conn2, cur2 = db.Setup(DB_NAME)

	url = r'https://www.researchgate.net/profile/Mohamed-Elbadawi/research'
	browser.get(url)
	soup = bs(browser.page_source, features="lxml")
	API.Collect(soup, cur2, url)
else:
	conn2, cur2 =db.ConnectDB(DB_NAME)
	browser = selenium_setup.SetupBrowser()


# error_l=[]
# conn = sqlite3.connect('RG-DB_colab.sqlite')
# cur = conn.cursor()
# cur.execute('SELECT id,url,html FROM Pages WHERE html is NOT Null  ORDER BY RANDOM()')
# row = cur.fetchone()
# soup = bs(row[2])
# API.Collect(soup, cur2, row[1])
# conn2.commit()



while True:
	try:
		cur2.execute('SELECT id, url FROM Globe WHERE status is 1  ORDER BY RANDOM() LIMIT 1')
		row = cur2.fetchone()
		url = row[1]
		print(url)
		browser.get(url)
		soup = bs(browser.page_source, features="lxml")
		API.Collect(soup, cur2, row[1])
		conn2.commit()

	except:
		try: 
			print(row[1])
			InsertError(cur2, url)
		except TypeError:
			break

print('exited while loop')
conn2.commit()
conn2.close()
