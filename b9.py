from selenium import webdriver
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get('https://itmscoaching.herokuapp.com/form')
driver.find_element_by_id('first-name').send_keys('Binh')
driver.find_element_by_id('last-name').send_keys('Nguyen')
driver.find_element_by_id('job-title').send_keys('Tester')
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click() 
driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]').click()
driver.find_element_by_id('datepicker').send_keys('07/20/2011')
driver.find_element_by_xpath('/html/body/div/form/div/div[8]/a').click()
time.sleep(1)
alertText = driver.find_element_by_xpath('/html/body/div/div').get_attribute('innerHTML')

try:
	assert "The form was successfully submitted!" in alertText
	print('OK')
	time.sleep(2)
	driver.close()

except Exception as e:
	raise e
