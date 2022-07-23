import requests
from lxml import html


class GRLS_drugs_finder:
    def __init__(self, drugname):
        self.name = drugname
        # здесь надо вставить связь с базой и запрос в базу.
        # если это drugname есть в базе и не просрочено, берем из базы
        # self.tnlist и self.mnnlist.
        # если его в базе нет или оно просрочено, получаем mnn, затем циклом из
        # self.mnnlist и self.name получаем список tn, кладем в self.tnlist.
        # в конце прокручиваем self.tnlist через сет.
        # результат записываем в базу.
        self.mnnlist = self.get_tnmnn(self.name, 3)
        self.tnlist = self.get_tnmnn(self.name, 2)
        for mnn in self.mnnlist:
            self.tnlist += self.get_tnmnn(mnn, 2)
        self.tnlist = list(set(self.tnlist))

    def find(self):
        # берем self.mnnlist и self.tnlist, складываем, прокручиваем через сет
        # и отдаем в виде списка
        ans = list(set(self.mnnlist + self.tnlist))
        # на будущее будем отдавать кортежем - сперва мнн, потом тн
        # ans = tuple(ans_mnn, ans_tn)
        return ans

    def get_tnmnn(self, name, mode):
        # mode может быть 2 или 3
        if mode == 2:
            post = 'mnn'
        else:
            post = 'tn'
        resp = requests.get(
            f'https://grls.rosminzdrav.ru/grls.aspx?s={name}&m={post}'
        )
        ans = []
        if resp.ok:
            root = html.fromstring(resp.content)
            if root.xpath(
                    "//span[@id='ctl00_plate_lerr']/text()"
            ) != ['Данные не найдены']:
                found_drugs = root.xpath(
                    "//span[@id='ctl00_plate_lrecn']/text()"
                )
                found_drugs = (str(found_drugs[-1])).split()
                ans += self.parse(root, mode)
                if int(found_drugs[-1]) > 10:
                    page = int(found_drugs[-1])
                    page = min((page // 10 + 2), 10)
                    root_other = root.xpath(
                        "//td[@class='btn_flat pad_lr'][1]/@onclick"
                    )
                    root_other = (str(root_other[-1]).strip("\"")).split(
                        'LockScreen("dvLock", "Ваш запрос обрабатывается...");'
                        ' window.location.href="'
                    )
                    root_other = root_other[-1][:-1]
                    for i in range(2, page):
                        resp_other = requests.get(
                            f'https://grls.rosminzdrav.ru/{root_other}{i}'
                        )
                        if resp_other.ok:
                            root_another = html.fromstring(resp_other.content)
                            ans += self.parse(root_another, mode)
        return ans

    def parse(self, item, mode):
        # mode может быть 2 или 3
        return item.xpath(
            "//table[contains(@class,'qa-result-table')]"
            "/tr[@class='hi_sys poi']"
            f"/td[{mode}]/text()"
        )
