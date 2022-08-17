from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from main.definitions import CHROMEDRIVER


def main(search):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-notifications')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER, options=options)
    driver.implicitly_wait(10)
    driver.get(f'https://aptekamos.ru/tovary/poisk?q={search}&&inr=0')
    return driver.find_element(
        By.XPATH, '//div[@class="product flex-df"]//div[@class="product-name"]'
    ).text
