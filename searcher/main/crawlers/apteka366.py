from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://366.ru/search/?text={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.js-product-item')
    res_list = []
    for elem in res:
        unit = {
            'name': elem.find_element(
                By.CSS_SELECTOR,
                '.listing_product__title'
            ).text,
            'prices': elem.find_element(
                By.CSS_SELECTOR,
                '.listing_product__price span'
            ).text,
            'link': elem.find_element(
                By.CSS_SELECTOR,
                '.listing_product__title'
            ).get_attribute('href'),
        }
        res_list.append(unit)
    return res_list
