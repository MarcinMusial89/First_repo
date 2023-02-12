from selenium import webdriver
import time
import datetime

now_timestamp = datetime.datetime.now()
screenshot = 'screenshot' + now_timestamp.strftime('_%H%M%S') + '.png'
driver = webdriver.Firefox()
driver.get('http://www.saucedemo.com')
print('Nazwa strony ', driver.title)
user_box = driver.find_element('id', 'user-name')
pass_box = driver.find_element('id', 'password')
user_box.clear()
pass_box.clear()
user_box.send_keys('standard_user')
pass_box.send_keys('secret_sauce')
log_button = driver.find_element('id', 'login-button')
log_button.click()

#standard_user secret_sauce

driver.get_screenshot_as_file(screenshot)

time.sleep(2)
driver.quit()

