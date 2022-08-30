import importlib
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# никаких импортов из main.crawlers! этим занимается importlib внутри функции
# from main.crawlers import aptekamos, asna, planetazdorovo, gorzdrav, rigla, \
#     apteka, eapteka, vseapteki, apteka366, megapteka
from main.decorators import result_cleaner
from main.definitions import CHROMEDRIVER


def crawl_it(search_list):
    result = []
    for item in search_list:
        result += use_crawl(item)
    # здесь обработка результатов - сортировка и устранение дубликатов
    temp_dict = {}
    for item in result:
        temp_dict[item['link']] = item
    result = list(temp_dict.values())
    result.sort(key=lambda x: int(x['price'].split(' ')[0]))
    return result


@result_cleaner
def use_crawl(search):
    options = Options()
    # options.add_argument('start-maximized')
    options.add_argument('--headless')
    # options.add_argument('--disable-notifications')
    # options.add_argument('--disable-extensions')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)
    driver.implicitly_wait(5)
    result = []
    path = Path.cwd() / 'main' / 'crawlers'
    crwl = sorted(os.listdir(path=path))[2:]
    for item in crwl:
        func = importlib.import_module(f'.{item[:-3]}',
                                       package='main.crawlers')
        try:
            res = func.main(driver, search)
            if len(res):
                print(f'{func.__name__} --> OK!')
                result += res
            else:
                print(f'{func.__name__} --> ERROR!')
        except Exception:
            res = func.another(search)
            if len(res):
                print(f'{func.__name__} --> OK!')
                result += res
            else:
                print(f'{func.__name__} --> ERROR!')
    # result += aptekamos.main(driver, search)
    # result += gorzdrav.main(driver, search)
    # result += rigla.main(driver, search)
    # result += apteka366.main(driver, search)
    # result += eapteka.main(driver, search)
    # result += vseapteki.main(driver, search)
    # result += megapteka.main(driver, search)
    # result += apteka.main(driver, search)
    driver.quit()
    return result
