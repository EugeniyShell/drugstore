from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://megapteka.ru/search?q={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.app-grid-card-item')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.find_element(
                    By.CSS_SELECTOR,
                    '.header a'
                ).get_attribute('title'),
                'prices': elem.find_element(
                    By.CSS_SELECTOR,
                    '.desktop .price'
                ).text,
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    '.header a'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
