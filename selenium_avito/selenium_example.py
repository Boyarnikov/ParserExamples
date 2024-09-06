from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_item_prices(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        print('loading')
        print('moving to parsing')
        item_prices = driver.find_elements(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ')

        for price in item_prices:
            print(price.text.strip())
    finally:
        driver.quit()


url = 'https://www.avito.ru/all/avtomobili'
scrape_item_prices(url)