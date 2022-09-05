import requests
from lxml import html

headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.67 Safari/537.36',
}

# apteka
# resp = requests.get(f'https://apteka.ru/search/?q=лираглутид')  # selenuim!
# apteka366
resp = requests.get(f'https://366.ru/search/?text=лираглутид', headers=headers)
print(resp.status_code)
root = html.fromstring(resp.content)
found = root.xpath('//div[@class="listing_product js-product-item"]')
for elem in found:
    try:
        unit = {
            'name': elem.xpath(
                '//a[contains(@class, "listing_product__title")]/text()'),
            'price': elem.xpath(
                '//div[@class="listing_product__price"]/span/text()'),
            'link': elem.xpath(
                '//a[contains(@class, "listing_product__title")]/@href'),
        }
    except Exception:
        pass
    print(unit)