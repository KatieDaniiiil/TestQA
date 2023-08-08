
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
base_url = "https://www.saucedemo.com/"
browser = webdriver.Chrome()
driver.get(base_url)
driver.maximize_window()


login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print('input login')

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print('input Password')

button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()
print('Click login, button')


'''INFO Product 1 (Информация о первом продукте)'''

product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//input[@id="inventory_container"]')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH,'//*[@id="ad-to-card-saucelabs-backpack"]')
select_product_1.click()
print(select_product_1)

cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cart.click()
print(cart)

'''INFO Cart Product 1 (Информация о первом товаре в корзине)'''

cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]')
value_cart_product_1 = product_1.text
print(value_cart_product_1)
assert  value_product_1 == value_cart_product_1    # сравниваем название товара в каталоге и корзине
print('INFO Cart Product 1 GOOD')

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
value_cart_product_1 = price_product_1.text
print(value_cart_product_1)
assert  value_cart_product_1 == value_price_product_1 # сравниваем цену товара в каталоге и корзине
print('INFO Cart Product 1 GOOD')

checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print(checkout)

first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name.send_keys('Alex')
print('Input First_name ')


last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name.send_keys('Ivanov')
print('Input Last_name ')

zip = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
zip.send_keys('1234')
print('Input Zip')

button_continue = driver.find_element(By.XPATH, '//*[@id="continue"]')
button_continue.click()
print('Click Continue')

''' ИНФО Завершение'''

time.sleep(10) 
browser.quit()