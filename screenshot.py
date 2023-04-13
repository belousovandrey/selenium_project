import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService                    # mozilla
from webdriver_manager.firefox import GeckoDriverManager                            # mozilla
from selenium.webdriver.chrome.service import Service as ChromeService              #Chrome
from webdriver_manager.chrome import ChromeDriverManager                            #Chrome

# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))      # mozilla
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))           #Chrome
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
login_standard_user = 'standard_user'
password_all = 'secret_sauce'
user_name = driver.find_element(By.ID, 'user-name')
user_name.send_keys(login_standard_user)
# time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE)
# user_name.send_keys('r')
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys(password_all)
password.send_keys(Keys.RETURN)
now_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = 'screenshot' + now_data + '.png'
driver.save_screenshot('./screen/' + name_screenshot)


