from selenium import webdriver
import time
import datetime

now_timestamp = datetime.datetime.now()
screenshot = 'screenshot' + now_timestamp.strftime('_%H%M%S') + '.png'
ddriver = webdriver.Firefox()
ddriver.get('http://www.saucedemo.com')
print('Nazwa strony ', ddriver.title)
user_box = ddriver.find_element('id', 'user-name')
pass_box = ddriver.find_element('id', 'password')
user_box.clear()
pass_box.clear()
user_box.send_keys('standard_user')
pass_box.send_keys('secret_sauce')
log_button = ddriver.find_element('id', 'login-button')
log_button.click()

#standard_user secret_sauce

ddriver.get_screenshot_as_file(screenshot)

time.sleep(2)
ddriver.quit()

