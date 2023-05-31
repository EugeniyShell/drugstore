import pandas

from main.definitions import SOURCEPATH

path = SOURCEPATH.glob('*.xls')
for file in path:
    print(file)
    df = pandas.read_excel(file, sheet_name=None)
    print(df)