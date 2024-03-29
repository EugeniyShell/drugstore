from selenium.webdriver.common.by import By
from main.decorators import result_logger


@result_logger
def main(driver, search):
    driver.get(f'https://gorzdrav.org/search/?text={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.js-product-item')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.find_element(
                    By.CSS_SELECTOR,
                    '.js-product-details-link .c-prod-item__title'
                ).text,
                'price': elem.find_element(
                    By.CSS_SELECTOR,
                    '.c-prod-item__action .b-price'
                ).text,
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    '.js-product-details-link'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
