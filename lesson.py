import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user_name = driver.find_element(By.ID,'user-name')
# user_name = driver.find_element(By.NAME,'user-name')
# user_name = driver.find_element(By.XPATH,'//*[@id="user-name"]')
# user_name = driver.find_element(By.CSS_SELECTOR,'[data-test="username"]')
password = driver.find_element(By.CSS_SELECTOR,'#password')
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')
user_name.send_keys('standard_user')
password.send_keys('secret_sauce')
button_login.click()






time.sleep(3)
# driver.close()