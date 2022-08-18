from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://planetazdorovo.ru/search/?q={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.product-card.card')
    res_list = []
    for elem in res:
        unit = {
            'name': elem.find_element(
                By.CSS_SELECTOR,
                '.product-card__title span'
            ).text,
            'prices': elem.find_element(
                By.CSS_SELECTOR,
                '.product-card__price'
            ).text,
            'link': elem.find_element(
                By.CSS_SELECTOR,
                '.product-card__title a'
            ).get_attribute('href'),
        }
        res_list.append(unit)
    return res_list
