from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://www.rigla.ru/search?q={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.product-list-mode-grid__item')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.find_element(
                    By.CSS_SELECTOR,
                    '.product__title span'
                ).text,
                'prices': elem.find_element(
                    By.CSS_SELECTOR,
                    '.product__active-price-number'
                ).text,
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    '.product__title'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
