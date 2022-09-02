from selenium.webdriver.common.by import By
from main.decorators import result_logger


@result_logger
def main(driver, search):
    driver.get(f'https://vseapteki.ru/search/?query={search}')
    res = driver.find_elements(By.CSS_SELECTOR, '.aGlg97eTgG')
    res_list = []
    for elem in res:
        try:
            unit = {
                'name': elem.find_element(
                    By.CSS_SELECTOR,
                    '.Wm58DKcoJf'
                ).text,
                'price': elem.find_element(
                    By.CSS_SELECTOR,
                    '._2wvA2Xrvtz'
                ).text,
                'link': elem.find_element(
                    By.CSS_SELECTOR,
                    '.XkfRn1KeHj'
                ).get_attribute('href'),
            }
            res_list.append(unit)
        except Exception:
            print(Exception)
    return res_list
