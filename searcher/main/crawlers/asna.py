from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://www.asna.ru/search/?query={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.product_product__ZvoP0')
    res_list = []
    for elem in res:
        unit = {
            'name': elem.find_element(
                By.CSS_SELECTOR,
                '.product_name__VzTPG'
            ).text,
            'prices': elem.find_element(
                By.CSS_SELECTOR,
                '.catalogPrice_price__TRAFl'
            ).text,
            'link': elem.find_element(
                By.CSS_SELECTOR,
                '.product_name__VzTPG'
            ).get_attribute('href'),
        }
        res_list.append(unit)
    return res_list
