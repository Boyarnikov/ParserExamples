from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

driver.get("https://www.scrapingcourse.com/ecommerce/page/1")

product_data = {
    "Url": driver.find_element(
        By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
    ).get_attribute("href"),
    "Image": driver.find_element(By.CSS_SELECTOR, ".product-image").get_attribute(
        "src"
    ),
    "Name": driver.find_element(By.CSS_SELECTOR, ".product-name").text,
    "Price": driver.find_element(By.CSS_SELECTOR, ".price").text,
}

print(product_data)
driver.quit()
