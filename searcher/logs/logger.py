import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from main.definitions import LOG_STRING_FORMAT, LOG_DATE_FORMAT, \
    LOGGING_LEVEL, LOGPATH


# допилить вторым аргументом путь
def get_logger(level, LOGPATH=LOGPATH):
    # прикручиваем это к нашему handlery
    SERVER_FORMATTER = logging.Formatter(fmt=LOG_STRING_FORMAT,
                                         datefmt=LOG_DATE_FORMAT)
    LOG_HANDLER = TimedRotatingFileHandler(LOGPATH, encoding='utf8',
                                           interval=1, when='D')
    LOG_HANDLER.setFormatter(SERVER_FORMATTER)

    # создаем еще один handler для вывода сообщений об ошибках в консоль
    # STREAM_HANDLER = logging.StreamHandler(sys.stderr)
    # STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
    # STREAM_HANDLER.setLevel(logging.ERROR)

    # запускаем логгер ds_logger
    LOGGER = logging.getLogger('ds_logger')
    # подключаем параметр
    LOGGER.addHandler(LOG_HANDLER)
    # LOGGER.addHandler(STREAM_HANDLER)
    LOGGER.setLevel(level)
    return LOGGER


# отладка
if __name__ == '__main__':
    LOGPATH = Path.cwd() / 'testlog.log'
    LOGGER = get_logger(LOGGING_LEVEL, LOGPATH)
    LOGGER.warning('Предупреждение')
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
