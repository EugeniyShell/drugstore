from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://aptekamos.ru/tovary/poisk?q={search}&&inr=0')
    res = driver.find_elements(By.CSS_SELECTOR, '.product.flex-df')
    res_list = []
    for elem in res:
        unit = {
            'name': elem.find_element(
                By.CSS_SELECTOR,
                '.product-name'
            ).text,
            'prices': elem.find_element(
                By.CSS_SELECTOR,
                '.product-price'
            ).text,
            'link': elem.find_element(
                By.CSS_SELECTOR,
                '.product-price'
            ).get_attribute('data-go-to-link'),
        }
        res_list.append(unit)
    return res_list
