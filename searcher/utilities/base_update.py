import os
import json
from pprint import pprint

import pandas
from sqlalchemy import create_engine, MetaData, Column, String, Integer, Table
from sqlalchemy.orm import sessionmaker, mapper

from main.data_base import Substantion
from main.definitions import SOURCEPATH, SQLALCHEMY_DATABASE_URI


def main():
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    metadata = MetaData()
    grls_table = Table(
        'grls',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('drugname', String),
        Column('commonname', String),
    )
    metadata.create_all(engine)
    # mapper(Substantion, grls_table)
    Session = sessionmaker(bind=engine)
    base_update_session = Session()
    drug = Substantion('imodium', 'loperamid')
    base_update_session.add(drug)
    base_update_session.commit()


def oldmain():
    # получаем набор файлов нужного формата по нужному пути
    path = SOURCEPATH.glob('*.xls')
    for file in path:
        excel = pandas.ExcelFile(file)
        #pprint(excel.sheet_names)
        excel_data_df = pandas.read_excel(excel, sheet_name='Действующий',
                                          header=6)
        json_file = json.loads(excel_data_df.to_json(orient='records'))
        #print('Excel Sheet to JSON:', json.loads(json_file))

        with open(SOURCEPATH / 'json_file.txt', 'w', encoding='UTF-8') as f:
            f.writelines(str(json_file[:100]))
        # удаление xls. предварительно закрывает открытый эксель
        excel.close()
        os.remove(file)


def base_update():
    pass


if __name__ == "__main__":
    main()
