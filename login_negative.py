import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService                    # mozilla
from webdriver_manager.firefox import GeckoDriverManager                            # mozilla
from selenium.webdriver.chrome.service import Service as ChromeService              #Chrome
from webdriver_manager.chrome import ChromeDriverManager                            #Chrome

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))      # mozilla
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))           #Chrome
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
login_standard_user = 'standard_use'
password_all = 'secret_sauce'
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys(login_standard_user)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
button_login.click()

warring = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
value_warring = warring.text
assert value_warring == 'Epic sadface: Username and password do not match any user in this service'


time.sleep(3)
# driver.close()
