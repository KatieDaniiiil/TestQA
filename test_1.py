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

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('input Pasword')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click login, button')
text_products = driver.find_element(By.XPATH, "//span[@class='title']")
vaiue_text_products = text_products.text
print(vaiue_text_products)

assert vaiue_text_products == "Products"
print("GOOD")
time.sleep(10)
driver.quit()