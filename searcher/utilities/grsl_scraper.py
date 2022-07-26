import requests
import wget
import zipfile
from lxml import html

from main.defs import GRLS_ADDRESS, USERAGENT


def main():
    url = GRLS_ADDRESS + 'GRLS.aspx'
    headers = {
        'User-agent': USERAGENT,
    }
    response = requests.get(url, headers=headers)
    root = html.fromstring(response.text)
    url = root.xpath('//div[@id="ctl00_plate_tdzip"]/button/@onclick')[0]
    url = GRLS_ADDRESS + url.split("'")[1]
    z = zipfile.ZipFile(wget.download(url, "./../sources"), 'r')
    z.extractall(path='./../sources')
    z.close()


if __name__ == "__main__":
    main()
