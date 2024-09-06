import requests
from bs4 import BeautifulSoup


def scrape_item_prices(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        item_prices = soup.find_all('p', attrs={
            'class': 'iva-item-priceStep-uq2CQ'
        })

        for price in item_prices:
            print(price.get_text(strip=True))
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        print(response)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(response.content.decode('utf-8'))


# Example usage
url = 'https://www.avito.ru/all/avtomobili'
scrape_item_prices(url)