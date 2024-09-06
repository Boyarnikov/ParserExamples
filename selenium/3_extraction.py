from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized") 


driver = webdriver.Chrome(options=options)
driver.get("https://www.twitch.tv/directory/category/world-of-tanks")

element = WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-target=directory-first-item]'))
)

print(driver.page_source)
