import re


def result_cleaner(func):
    '''декоратором чистим выдачу'''
    def cleaner(*args):
        ans = func(*args)
        result = []
        for item in ans:
            name, price, link = item.values()
            if name and price and link:
                price = re.search(
                    r'\d+', re.sub(r'(\d+) (\d+)', r'\1\2', price)).group()
                if int(price) == 0:
                    continue
                price += ' ₽'
                name = re.sub(r'\s+', ' ', name).strip()
                result.append({'name': name, 'price': price, 'link': link})
        return result
    return cleaner