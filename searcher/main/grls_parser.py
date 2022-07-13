import requests
from lxml import html


def grls_finder(search):
    res1 = grls_parse(search, 'mnn')
    res2 = grls_parse(search, 'tn')
    # print(res1, res2)
    ans = list(set(res1 + res2))
    # возможно стоит добавить сортировку в алфавитном порядке
    return ans


def grls_parse(name, mode):
    # стоит переписать на рекурсивный вызов
    # вместо аргументов name, mode передавать сразу готовые url
    # функция ищет список названий и его собирает
    # функция ищет ссылку на следующую страницу погенации и дергает её рекурсивно
    # результат рекурсии плюсуется к собранному результату и возвращает все вместе
    # если ничего нет - возвращается пустой список
    resp = requests.get(
        f'https://grls.rosminzdrav.ru/grls.aspx?s={name}&m={mode}'
    )
    # print(resp.status_code)
    # if resp.status_code != 200:
    if resp.ok:
        root = html.fromstring(resp.content)
        found_drugs = root.xpath(
            "//span[@id='ctl00_plate_lrecn']/text()"
        )
        found_drugs = (str(found_drugs[-1])).split()
        if int(found_drugs[-1]) < 11:
            return pars(root)
        else:
            page = int(found_drugs[-1])
            page = min((page//10 + 2), 10)
            ans = list()
            ans += pars(root)
            root_other = root.xpath(
                "//td[@class='btn_flat pad_lr'][1]/@onclick"
            )

            root_other = (str(root_other[-1]).strip("\"")).split(
                'LockScreen("dvLock", "Ваш запрос обрабатывается..."); window.location.href="')
            root_other = root_other[-1][:-1]
            print(root_other)
            for i in range(2, page):
                print(f'https://grls.rosminzdrav.ru/{root_other}{i})')
                resp_other = requests.get(
                    f'https://grls.rosminzdrav.ru/{root_other}{i}'
                )
                if resp_other.ok:
                    root_another = html.fromstring(resp_other.content)
                    ans += pars(root_another)
            return ans
    else:
        return []


def pars(root):
    names = root.xpath(
        "//table[contains(@class,'qa-result-table')]"
        "/tr[@class='hi_sys poi']"
        "/td[2]/text()"
    )
    print(names)
    return names
