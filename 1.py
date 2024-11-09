from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# เปิดเบราว์เซอร์
driver = webdriver.Chrome()
driver.get('https://shopee.co.th')
driver.implicitly_wait(2)


input("hold ")
btn1 = driver.find_element(By.ID, "btnSubmit")
btn1.click()


# ปิดเบราว์เซอร์
driver.quit()
