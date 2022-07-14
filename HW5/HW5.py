import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from selenium.common import exceptions
import time

_LOGIN = "study.ai_172@mail.ru"
_PASSWORD = "NextPassword172#"

s = Service('../Lesson 5/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://mail.ru/')

entry = driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]")
entry.click()

login = driver.find_element(By.NAME, 'login')
login.send_keys(_LOGIN)
login.send_keys(Keys.ENTER)
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, 'password')))
password = driver.find_element(By.NAME,'password')
password.send_keys(_PASSWORD)
password.send_keys(Keys.ENTER)

# login = driver.find_element(By.NAME, 'username')
# login.send_keys("study.ai_172@mail.ru")
#
# nextButton = driver.find_element(By.XPATH, ".//button[contains(@data-test-id, 'next-button')]")
# nextButton.click()
#
# pwd = driver.find_element(By.NAME, 'password')
# pwd.send_keys("NextPassword172#")
#
# submit = driver.find_element(By.XPATH, ".//button[contains(@data-test-id, 'submit-button')]")
# submit.click()