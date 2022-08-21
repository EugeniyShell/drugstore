import requests
from lxml import html

from main.definitions import USERAGENT

HEADERS = {
    'User-agent': USERAGENT,
    'Pragma': 'no-cache',
    'Cookie': 'qrator_jsr=1661080576.693.XPLbs5Rndef948F4'
              '-iih0kf5tofsch9konr7b44c5rm6n5sv7-00; '
              '_ga_MPGG3927SG=GS1.1.1661077306.4.1.1661080576.60.0.0; '
              'qrator_ssid=1661080577.008.KfUGaZoSF89YgDFY'
              '-up1vml40l01v188jpdt9jdbdkv7l03tb; '
              'qrator_jsid=1661080576.693.XPLbs5Rndef948F4'
              '-62ids9nr3cdk06vj8g3g0u32kmg5crd7',
}


def main(search):
    resp = requests.get(f'https://www.asna.ru/search/?query={search}',
                        headers=HEADERS)
    root = html.fromstring(resp.content)
    res = root.xpath('//div[@itemprop="offers"]')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.xpath(
                    './/a[@class="product_name__VzTPG"]/text()'
                )[0],
                'prices': elem.xpath(
                    './/meta[@itemprop="price"]/@content'
                )[0],
                'link': 'https://www.asna.ru' + elem.xpath(
                    './/a[@class="product_name__VzTPG"]/@href'
                )[0],
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list


# if __name__ == '__main__':
#     print(main('Лираглутид'))
