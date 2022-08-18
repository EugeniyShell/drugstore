from selenium.webdriver.common.by import By


def main(driver, search):
    driver.get(f'https://vseapteki.ru/search/?query={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.aGlg97eTgG')
    res_list = []
    for elem in res:
        unit = {
            'name': elem.find_element(
                By.CSS_SELECTOR,
                '.Wm58DKcoJf'
            ).text,
            'prices': elem.find_element(
                By.CSS_SELECTOR,
                '._2wvA2Xrvtz'
            ).text,
            'link': elem.find_element(
                By.CSS_SELECTOR,
                '.XkfRn1KeHj'
            ).get_attribute('href'),
        }
        res_list.append(unit)
    return res_list
