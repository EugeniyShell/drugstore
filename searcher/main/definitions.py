from pathlib import Path

USERAGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
            '(KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
GRLS_ADDRESS = 'https://grls.rosminzdrav.ru/'
SOURCEPATH = Path("./../sources")
SQLALCHEMY_DATABASE_URI = 'sqlite:///../sources/grls.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
CHROMEDRIVER = Path.cwd() / 'chromedriver.exe'
LOGGING_LEVEL = 'DEBUG'
LOGPATH = Path.cwd() / 'logs' / 'log.log'
LOG_STRING_FORMAT = '[%(levelname)s] [%(asctime)s] [%(module)s:%(funcName)s]' \
                    ' --> %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
