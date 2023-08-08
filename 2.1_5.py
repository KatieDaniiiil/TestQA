from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element(By.ID, "peopleRule")

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked == "True", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "roboteRule")
robots_radio = robots_radio.get_attribute("checked")

assert people_checked is not None

# закрываем браузер после всех манипуляций
browser.quit()