import re


def result_cleaner(func):
    '''декоратором чистим выдачу'''
    def cleaner(*args):
        from wsgi import app
        app.logger.info(f'Decorated {func.__name__}')
        ans = func(*args)
        result = []
        counting = 0
        for item in ans:
            name, price, link = item.values()
            app.logger.debug(f'{name=} {price=} {link=}')
            if name and price and link:
                price = re.search(
                    r'\d+', re.sub(r'(\d+) (\d+)', r'\1\2', price)).group()
                if int(price) == 0:
                    continue
                price += ' ₽'
                name = re.sub(r'\s+', ' ', name).strip()
                result.append({'name': name, 'price': price, 'link': link})
                app.logger.debug('Process OK')
                counting += 1
            else:
                app.logger.warning('Process broken')
        app.logger.info(f'{counting} items processed.')
        return result
    return cleaner