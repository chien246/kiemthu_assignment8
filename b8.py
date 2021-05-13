from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('https://the-internet.herokuapp.com/')
driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[21]/a').click()
driver.find_element_by_id('username').send_keys('tomsmith')
driver.find_element_by_id('password').send_keys('SuperSecretPassword')
driver.find_element_by_xpath('//*[@id="login"]/button/i').click()

try:
	assert "The Internet" in driver.title
	print(driver.title)
	print('OK')
	time.sleep(2)
	driver.close()

except Exception as e:
	print(e) 


