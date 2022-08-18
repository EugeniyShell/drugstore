from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from main.crawlers import aptekamos, asna, planetazdorovo, gorzdrav
from main.definitions import CHROMEDRIVER


def crawl_it(search):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-notifications')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)
    driver.implicitly_wait(5)
    result = []
    # здесь поочередно парсим все аптеки
    result += aptekamos.main(driver, search)
    result += asna.main(driver, search)  # отдает 403
    result += planetazdorovo.main(driver, search)  # отдает 403
    result += gorzdrav.main(driver, search)
    driver.quit()
    return result
