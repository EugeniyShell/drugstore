import requests
from lxml import html

from main.definitions import USERAGENT

HEADERS = {
    'User-agent': USERAGENT,
    'Cookie': 'qrator_ssid=1661090619.219.WkaCPQ1XYOcNfaSO-14adpqhtltnvfnmoth'
              'js83e2phabpnvp; '
              'qrator_jsid=1661090610.638.JEzAlA3R16ivW4fg-csbhmlmffu9v9hf92h'
              'hcpq3pg9n54k2s;'
}


def main(search):
    resp = requests.get(f'https://planetazdorovo.ru/search/?q={search}',
                        headers=HEADERS)
    root = html.fromstring(resp.text)
    res = root.xpath('//div[contains(@class, "card-list__element")]')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.xpath(
                    './/div[@class="product-card__title"]//span/text()'
                )[0],
                'prices': elem.xpath('.//div[@itemprop="price"]/text()')[0],
                'link': 'https://planetazdorovo.ru' + elem.xpath(
                    './/div[@class="product-card__title"]/a/@href'
                )[0],
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list


# if __name__ == '__main__':
#     print(main('Лираглутид'))
