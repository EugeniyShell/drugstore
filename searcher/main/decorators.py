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


def result_logger(func):
    '''декоратором логируем результаты'''
    def logger_(*args):
        from wsgi import app
        ans = func(*args)
        app.logger.info(f'Decorated {func.__module__}.{func.__name__}')
        counting = 0
        for item in ans:
            try:
                app.logger.debug(f'{item["name"]} {item["price"]} '
                                 f'{item["link"]}')
            except Exception:
                app.logger.error({item})
            counting += 1
        app.logger.info(f'{counting} items resulted.')
        return ans
    return logger_
