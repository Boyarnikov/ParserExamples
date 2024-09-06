from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_argument('lang=en')

driver = webdriver.Chrome(options)
driver.get("https://www.twitch.tv/")
search_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search Input"]')
search_box.send_keys('tanks')

print("sending keys")
sleep(10)
#search_box.send_keys(Keys.ENTER)
search_button = driver.find_element(By.CSS_SELECTOR, 'button[icon="NavSearch"]')
search_button.click()

sleep(10000)