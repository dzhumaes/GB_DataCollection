# Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
# Логин тестового ящика: study.ai_172@mail.ru
# Пароль тестового ящика: NextPassword172#


import sys
import time

from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

_LOGIN = "study.ai_172@mail.ru"
_PASSWORD = "NextPassword172#"

def parse_email(driver):

    letter = dict()

    time.sleep(1)

    letter_contact = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CLASS_NAME, 'letter-contact')
        )
    ).get_attribute('title')

    letter_subject = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.XPATH, '//h2')
        )
    ).text

    letter_date = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.XPATH, '//div[@class="letter__date"]')
        )
    ).text

    letter_body = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable(
            (By.CLASS_NAME, 'letter__body')
        )
    ).text

    letter['sender'] = letter_contact
    letter['subject'] = letter_subject
    letter['date'] = letter_date
    letter['body'] = letter_body

    return letter

def main():

    client = MongoClient('127.0.0.1', 27017)
    db = client['mailDB']
    emails = db.emails

    s = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    driver.get('https://mail.ru/')

    entry = driver.find_element(By.XPATH, ".//button[contains(text(),'Войти')]")
    entry.click()
    time.sleep(3)

    iframe = driver.find_element(By.XPATH, "//iframe[contains(@class, '__iframe')]")
    driver.switch_to.frame(iframe)

    login = driver.find_element(By.XPATH, ".//input[@name = 'username']")
    login.send_keys(_LOGIN)
    login.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.NAME, 'password')))
    password = driver.find_element(By.NAME,'password')
    password.send_keys(_PASSWORD)
    password.send_keys(Keys.ENTER)

    driver.switch_to.default_content()

    first_letter = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(
            (By.CLASS_NAME, 'js-letter-list-item')
        )
    )
    first_letter.click()

    while True:
        email = parse_email(driver)
        try:
            emails.update_one(email, {'$setOnInsert': email}, upsert=True)

            button_next = WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable(
                    (By.CLASS_NAME, 'button2_arrow-down')
                )
            )
            button_next.click()
        except:
            print('All email letters are over')
            break

if __name__ == '__main__':
    sys.exit(main())