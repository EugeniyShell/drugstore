import re


def result_cleaner(func):
    '''декоратором чистим выдачу'''
    def cleaner(*args):
        ans = func(*args)
        result = []
        for item in ans:
            name, price, link = item.values()
            print(name, price, link)
            if name and price and link:
                # name = name.replace('\xa0', ' ').replace('\n', ' ')\
                # .replace('  ', ' ').strip()
                name = re.sub(r'\s+', ' ', name).strip()
                # price = price.replace(',', '.').replace(r'[^0-9\.]', ' ')\
                #     .replace('  ', ' ').split(' ')[0]
                # price = f'от {price} рублей'
                # price = price.split('.')[0].replace('₽', '').strip() + ' ₽'
                price = re.search(
                    r'\d+',
                    re.sub(r'(\d+) (\d+)', r'\1\2', price)
                ).group() + ' ₽'
                result.append({'name': name, 'price': price, 'link': link})
        return result
    return cleaner