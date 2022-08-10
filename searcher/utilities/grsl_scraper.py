import os
import zipfile

import requests
import wget
from lxml import html

from main.definitions import GRLS_ADDRESS, USERAGENT, SOURCEPATH


def main():
    # скачиваем с сайта базу в формате xls, извлекаем из зипа, чистим за собой.
    url = GRLS_ADDRESS + 'GRLS.aspx'
    headers = {
        'User-agent': USERAGENT,
    }
    response = requests.get(url, headers=headers)
    root = html.fromstring(response.text)
    url = root.xpath('//div[@id="ctl00_plate_tdzip"]/button/@onclick')[0]
    url = GRLS_ADDRESS + url.split("'")[1]
    z = zipfile.ZipFile(wget.download(url, SOURCEPATH.__str__()), 'r')
    z.extractall(path=SOURCEPATH)
    z.close()
    path = SOURCEPATH.glob('*.zip')
    for file in path:
        os.remove(file)


if __name__ == "__main__":
    main()
