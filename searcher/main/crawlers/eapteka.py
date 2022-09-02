from selenium.webdriver.common.by import By
from main.decorators import result_logger


@result_logger
def main(driver, search):
    driver.get(f'https://www.eapteka.ru/search/?q={search}')
    res = driver.find_elements(By.CSS_SELECTOR, 'section.cc-item')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.get_attribute(
                    "data-amplitude-item-serp-name"
                ),
                'price': elem.get_attribute(
                    "data-amplitude-item-serp-price"
                ),
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    '.cc-item--title'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
