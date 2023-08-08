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
password.send_keys('password_all')
print('Input Password')
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click login, button')

#driver.execute_script("window.scrollTo(0, 500)")
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
action.move_to_element(red_t_shirt).perform()
#warring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
##print('Good test')
#text_products = driver.find_elem
#vaiue_text_products = text_products.text
#@print(vaiue_text_products)
#assert vaiue_text_products == "Products"
#print("GOOD"
#driver.save_screenshot('screenshot.png')
#driver.refresh()
#driver.execute_script("window.scrollTo(0, 200)")
#time.sleep(5)
#river.save_screenshot('screenshot_2.png')
time.sleep(55)


now_date = datetime.utcnow().strtime('%Y.%M.%D.%H.%M.%S')
name_screenshot = 'screenshot' + now_date +'.png'
driver.save_screenshot('screenshot_3.png')
time.sleep(55)
driver.quit()