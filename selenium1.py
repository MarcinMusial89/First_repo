from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://google.com')
print('Nazwa strony ', driver.title)
button1_accept = driver.find_element('id', 'L2AGLb')
button1_accept.click()
search_box = driver.find_element('name', 'q')
search_box.send_keys('Czy jutro jest niedziela handlowa')
search_button = driver.find_element('name', 'btnK')
search_button.submit()
#time.sleep(3)
#driver.quit()

