from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from main.crawlers import aptekamos, asna, planetazdorovo, gorzdrav, rigla, \
    apteka, eapteka, vseapteki, apteka366, megapteka
from main.decorators import result_cleaner
from main.definitions import CHROMEDRIVER


def crawl_it(search_list):
    result = []
    for item in search_list:
        # здесь вызываем селениумный парсинг тех, кто парсится им
        result += selenium_crawl(item)
        # здесь вызываем парсинг тех, кто не пускает селениум
        result += lxml_crawl(item)
    # здесь будет обработка результатов - сортировка и устранение дубликатов
    temp_dict = {}
    for item in result:
        temp_dict[item['link']] = item
    result = list(temp_dict.values())
    result.sort(key=lambda x: int(x['price'].split(' ')[0]))
    return result


@result_cleaner
def selenium_crawl(search):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-notifications')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)
    driver.implicitly_wait(10)
    result = []
    result += aptekamos.main(driver, search)
    result += gorzdrav.main(driver, search)
    result += rigla.main(driver, search)
    result += apteka366.main(driver, search)
    result += eapteka.main(driver, search)
    result += vseapteki.main(driver, search)
    result += megapteka.main(driver, search)
    result += apteka.main(driver, search)
    driver.quit()
    return result


@result_cleaner
def lxml_crawl(search):
    result = []
    result += asna.main(search)
    result += planetazdorovo.main(search)
    return result
