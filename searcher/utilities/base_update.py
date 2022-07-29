from pprint import pprint

import json
import pandas

from main.defs import SOURCEPATH


def main():
    # получаем набор файлов нужного формата по нужному пути
    path = SOURCEPATH.glob('*.xls')
    for file in path:
        excel = pandas.ExcelFile(file)
        #pprint(excel.sheet_names)
        excel_data_df = pandas.read_excel(excel, sheet_name='Действующий',
                                          header=6)
        json_file = json.loads(excel_data_df.to_json(orient='records'))
        print(type(json_file))
        #print('Excel Sheet to JSON:', json.loads(json_file))
        with open(SOURCEPATH / 'json_file.txt', 'w', encoding='UTF-8') as f:
            f.writelines(str(json_file[:100]))


if __name__ == "__main__":
    main()
