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
        print("page loaded")

        item_prices = []
        while not item_prices:
            try:
                item_prices = driver.find_elements(By.CLASS_NAME, 'iva-item-priceStep-uq2CQ')
            except Exception:
                print("Oops, need to solve capcha")
                input("Input when done")
        for price in item_prices:
            print(price.text.strip())

    finally:
        driver.quit()


url = 'https://www.avito.ru/all/avtomobili'
for i in range(10):
    scrape_item_prices(url+f"?p={i}")