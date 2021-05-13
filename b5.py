from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.set_window_size(500,350)
try:
	assert "http://practice.automationtesting.in/" in driver.current_url
	print(driver.current_url)
	print('OK')
	time.sleep(2)
	driver.close()

except Exception as e:
	print(e) 