import os
import requests
import wget
import zipfile
from pathlib import Path
from lxml import html

from main.defs import GRLS_ADDRESS, USERAGENT


def main():
    path = Path("./../sources")
    url = GRLS_ADDRESS + 'GRLS.aspx'
    headers = {
        'User-agent': USERAGENT,
    }
    response = requests.get(url, headers=headers)
    root = html.fromstring(response.text)
    url = root.xpath('//div[@id="ctl00_plate_tdzip"]/button/@onclick')[0]
    url = GRLS_ADDRESS + url.split("'")[1]
    z = zipfile.ZipFile(wget.download(url, path.__str__()), 'r')
    z.extractall(path=path)
    z.close()
    path = path.glob('*.zip')
    for p in path:
        os.remove(p)


if __name__ == "__main__":
    main()
