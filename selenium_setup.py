from selenium import webdriver
import os

def SetupSelenium_Linux():
	binary = '/usr/bin/firefox'
	options = webdriver.FirefoxOptions()
	options.binary = binary
	options.add_argument('start-maximized')
	options.add_argument('--headless')
	# prefs = {"profile.managed_default_content_settings.images": 2}
	# options.add_experimental_option("prefs", prefs)
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--ignore-ssl-errors')
	browser = webdriver.Firefox(options=options, executable_path='/content/geckodriver')
	return browser

def SetupSelenium_Win():
	browser = webdriver.Chrome()
	chrome_options = webdriver.ChromeOptions()

	prefs = {"profile.managed_default_content_settings.images": 2}
	chrome_options.add_experimental_option("prefs", prefs)
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--ignore-ssl-errors')
	browser = webdriver.Chrome(options=chrome_options)

	return browser

def SetupBrowser():
	if os.name == 'nt':
		return SetupSelenium_Win()
	else:
		return SetupSelenium_Linux()
