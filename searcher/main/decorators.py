import re


def result_cleaner(func):
    def cleaner(*args):
        ans = func(*args)
        result = []
        for item in ans:
            name, price, link = item.values()
            print(name, price, link)
            name = name.replace('\xa0', ' ').replace(r'\s', ' ')\
                .replace('  ', ' ').strip()
            # price = price.replace(',', '.').replace(r'[^0-9\.]', ' ')\
            #     .replace('  ', ' ').split(' ')[0]
            # price = f'от {price} рублей'
            # price = price.split('.')[0].replace('₽', '').strip() + ' ₽'
            price = re.search(
                r'\d+',
                re.sub(r'(\d+) (\d+)', r'\1\2', price)
            ).group() + ' ₽'
            if name and price and link:
                result.append({'name': name, 'price': price, 'link': link})
        return result
    return cleaner