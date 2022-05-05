from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID,'price'), '100'))

    button_book = browser.find_element_by_css_selector("#book")
    button_book.click()

    x = browser.find_element_by_css_selector('#input_value').text
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
