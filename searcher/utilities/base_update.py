import os
from pathlib import Path

import pandas
from sqlalchemy import create_engine, MetaData, Column, String, Integer, Table
from sqlalchemy.orm import sessionmaker, mapper

from logs.logger import get_logger
from main.definitions import SOURCEPATH, SQLALCHEMY_DATABASE_URI, LOGGING_LEVEL


class TableItem:
    # создаем класс-модель для наших данных
    def __init__(self, commonname, drugname):
        self.id = None
        self.commonname_normalized = commonname.lower()
        self.commonname = commonname
        self.drugname_normalized = drugname.lower()
        self.drugname = drugname


def main():
    # создаем движок БД
    # метадата - описание движка базы
    # описываем таблицу, которую будем создавать (имя, мета, колонки)
    # маппером связываем нашу таблицу и класс-модель
    # уничтожаем все таблицы в текущей базе
    # создаем новвые (одну) таблицы
    # создаем сессию при помощи сессионмейкера из алхимии
    # запускаем апдейтер базы создавая экземпляр класса session
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    LOGGER.info('Создан движок базы. Это база!')
    metadata = MetaData()
    grls_table = Table(
        'grls',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('commonname_normalized', String),
        Column('commonname', String),
        Column('drugname_normalized', String),
        Column('drugname', String)
    )
    # маппер привязывает каждый экземпляр нашего класса к строке таблицы
    mapper(TableItem, grls_table)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    base_update_session = session()
    usepandas(base_update_session)
    base_update_session.commit()


def usepandas(base_update_session):
    # получаем набор файлов нужного формата по нужному пути
    path = SOURCEPATH.glob('*.xls')
    for file in path:
        # дергаем из экселя нужные данные через pandas
        excel = pandas.ExcelFile(file)
        try:
            excel_data_df = pandas.read_excel(excel, sheet_name='Действующий',
                                              header=4)
            mnn_tn = excel_data_df[['Торговое наименование\nлекарственного '
                                    'препарата',
                                    'Международное непатентованное или химическое '
                                    'наименование']][1:]
            # апдейтим базу парами значений
            for _tn, _mnn in mnn_tn.itertuples(index=False):
                if _mnn == '~':
                    _mnn = _tn
                base_update(_mnn, _tn, base_update_session)
        except Exception as err:
            LOGGER.error(err)
        excel.close()
        # удаляем файл
        os.remove(file)


def base_update(mnn, tn, base_update_session):
    # создаем экземпляр модели и закидываем его в сессию
    item = TableItem(mnn, tn)
    # LOGGER.info('HERE LOG!!!')
    base_update_session.add(item)


if __name__ == "__main__":
    # запускаем логгер с отдельным пасом
    LOGPATH = Path.cwd() / '..' / 'logs' / 'baselog.log'
    LOGGER = get_logger(LOGGING_LEVEL, LOGPATH)
    main()
