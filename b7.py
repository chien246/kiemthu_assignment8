from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('http://practice.automationtesting.in/')
driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
driver.find_element_by_id('reg_email').send_keys('a@gmail.com')
driver.find_element_by_id('reg_password').send_keys(
    'abc123dsgs#$$^$^^$^dgdggddhtrhh')
time.sleep(5)
document = driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form')
document.click()

button = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]')
button.click()

alertText = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[1]/ul/li').get_attribute('innerHTML')

try:
	assert "Please login" in alertText
	print('OK')
	time.sleep(2)
	drievr.close()

except Exception as e:
	raise e