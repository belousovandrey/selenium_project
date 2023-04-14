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
time.sleep(3)
user_name.clear()


time.sleep(3)