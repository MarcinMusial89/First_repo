from selenium import webdriver
import time
import datetime
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

def make_screenshot(driver):
    teraz = datetime.datetime.now()
    screenshot = 'screenshot' + teraz.strftime('_%H%M%S') + '.png'
    driver.get_screenshot_as_file('./Snapshot/' + screenshot)

def czekaj_na_id(element_id):
    timeout = 10
    timeout_message = f'Element of id {element_id} nie pojawil sie w czasie {timeout} s.'

    lokalizator = ('id', element_id) #szukanie pod id konkretnej wartosci
    znaleziono = excon.visibility_of_element_located(lokalizator) #patyk do dzgania strony
    #obiekt bedzie pytany, czy jest OK, a w odpowiedzi bedzie zalzecod tego,czy elemnt jest widoczny
    oczekiwator = WebDriverWait(ddriver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)


ddriver = webdriver.Firefox()
ddriver.get('http://www.saucedemo.com')
try:
    login_button = czekaj_na_id('login-buttonm')
except TimeoutException:
    print('Nie znaleziono')
    #raise #pokaz blad pomimo except
else:
    print('Znaleziono')
finally:
    make_screenshot(ddriver)
    time.sleep(2)
    ddriver.quit()