import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://borispotapov.github.io/index.html"
browser = webdriver.Chrome()
browser.get(link)
button1 = browser.find_element(By.XPATH, '//*[@id="menu-button"]/a')
button1.click()
time.sleep(2)

button2 = browser.find_element(By.XPATH, '//*[@id="menu-button"]/a')
button2 = button2.text
assert 'Психологическая консультация' == button2, 'Произошла ошибка!'
time.sleep(2)
print('Проверка завершена!')


# закрываем браузер после всех манипуляций
time.sleep(5)

browser.quit()