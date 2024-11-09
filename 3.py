from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

mail_address = 'phuripattaraphan8@gmail.com'
password = 'theyok56798'
UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run headless mode if needed
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1920x1080')
chrome_options.add_argument(f"user-agent={UA}")

# Path to ChromeDriver
service = Service('path/to/chromedriver')  # Replace with the path to your ChromeDriver

driver = webdriver.Chrome(service=service, options=chrome_options)

# Your login automation script
url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp/'
driver.get(url)

driver.find_element(By.ID, "Email").send_keys(mail_address)
driver.find_element(By.ID, "next").click()
time.sleep(1)  # Wait for the transition to load

driver.find_element(By.ID, "Passwd").send_keys(password)
driver.find_element(By.ID, "signIn").click()

# Close the browser
driver.quit()
