from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Firefox()
    # говорим WebDriver ждать все элементы в течении 15 секунд
    browser.implicitly_wait(15)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    # открыть страницу в браузере
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element_by_id("book")
    text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()
    input_value = browser.find_element_by_id("input_value")
    # посчитать функцию
    y = calc(int(input_value.text))
    # найти текстовое поле и проскроллить страницу вниз
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(y)
    # нажать на кнопку Submit    
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
