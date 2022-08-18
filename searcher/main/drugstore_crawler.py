from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from main.crawlers import aptekamos, asna, planetazdorovo, gorzdrav, rigla, \
    apteka, eapteka, vseapteki, apteka366, megapteka
from main.definitions import CHROMEDRIVER


def crawl_it(search):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-notifications')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)
    driver.implicitly_wait(10)
    result = []
    # здесь поочередно парсим все аптеки
    result += aptekamos.main(driver, search)
    result += gorzdrav.main(driver, search)
    result += rigla.main(driver, search)
    result += apteka366.main(driver, search)
    result += eapteka.main(driver, search)
    result += vseapteki.main(driver, search)
    result += megapteka.main(driver, search)
    #
    # result += asna.main(driver, search)  # отдает 403
    # result += planetazdorovo.main(driver, search)  # отдает 403
    # result += apteka.main(driver, search)  # джаваскриптовый сайт

    driver.quit()
    return result
