from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.fullscreen_window()
try:
	assert "Automation Practice Site" in driver.title
	print(driver.title)
	print('OK')
	time.sleep(2)
	driver.close()

except Exception as e:
	print(e) 

