import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login)
print('input login')

test_1.py
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click login, button')
warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"
print('Good test')
#text_products = driver.find_elem
#
#vaiue_text_products = text_products.text
#@print(vaiue_text_products)

#assert vaiue_text_products == "Products"
#print("GOOD")
driver.refresh()
time.sleep(10)
driver.quit()