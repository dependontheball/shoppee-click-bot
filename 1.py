from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# เปิดเบราว์เซอร์
driver = webdriver.Chrome()
driver.get('https://shopee.co.th')
driver.implicitly_wait(2)

button = driver.find_element(By.XPATH, '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')  # ระบุตาม id, class, หรืออื่นๆ
ActionChains(driver).move_to_element(button).click().perform()


input("Press Enter to close the browser...")