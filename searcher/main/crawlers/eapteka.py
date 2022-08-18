from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://www.eapteka.ru/search/?q={search}')
    res = driver.find_elements(By.CSS_SELECTOR, 'section.cc-item')
    res_list = []
    for elem in res:
        unit = {
            'name': elem.get_attribute(
                "data-amplitude-item-serp-name"
            ),
            'prices': elem.get_attribute(
                "data-amplitude-item-serp-price"
            ),
            'link': elem.find_element(
                By.CSS_SELECTOR,
                '.cc-item--title'
            ).get_attribute('href'),
        }
        res_list.append(unit)
    return res_list
