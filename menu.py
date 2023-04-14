import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService              #Chrome
from webdriver_manager.chrome import ChromeDriverManager                            #Chrome


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))           #Chrome
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
login_standard_user = 'standard_user'
password_all = 'secret_sauce'
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys(login_standard_user)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')

button_login.click()


menu =  driver.find_element(By.CSS_SELECTOR, '#react-burger-menu-btn')
menu.click()

time.sleep(3)