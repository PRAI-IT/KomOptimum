import os
import json
import pandas as pd

data_set = list()

dir_expenses = "../train_data/Lists ON"


def getFiles(path):
    files = list()
    for file in os.listdir(path):
        if os.path.isfile(f'{path}/{file}'):
            if os.path.splitext(file)[-1] in (".xlsx", ".xls"):
                files.append(f'{path}/{file}')
        else:
            files += getFiles(f'{path}/{file}')
    return files


for file in getFiles(dir_expenses):
    if os.path.splitext(file)[-1] in (".xlsx", ".xls") and "2023" not in file and "4 quarter 2022" not in file:
        dataframe = pd.read_excel(open(file, 'rb'),
                                  skiprows=lambda x: x in [0, 1, 2, 3, 4, 5, 6, 7])
        for index, row in dataframe.iterrows():
            if not row[1] != row[1] and isinstance(row[1], str) and row[1] not in ("ВСЕГО:","Итого:"):
                department = row[1]
            if not row[2] != row[2]:
                if isinstance(row[3], str):
                    row[3] = 0
                if row[5] != row[5]:
                    row[5] = 0
                if row[6] != row[6]:
                    row[6] = 0
                if row[7] != row[7]:
                    row[7] = 0
                if not isinstance(row[25], str):
                    row[25] = 0
                data_set.append([file.split('/')[-1].split('.')[0], department, row[2], row[3], row[5], row[6], row[7], row[25]])
    if os.path.splitext(file)[-1] in (".xlsx", ".xls") and ("2023" in file or "4 quarter 2022" in file):
        dataframe = pd.read_excel(open(file, 'rb'),
                                  skiprows=lambda x: x in [0, 1, 2, 3, 4, 5, 6])
        for index, row in dataframe.iterrows():
            if not row[1] != row[1] and isinstance(row[1], str) and row[1] not in ("ВСЕГО:","Итого:"):
                department = row[1]
            if not row[3] != row[3]:
                if isinstance(row[4], str):
                    row[4] = 0
                if row[6] != row[6]:
                    row[6] = 0
                if row[8] != row[8]:
                    row[8] = 0
                if row[7] != row[7]:
                    row[7] = 0
                if not isinstance(row[21], str):
                    row[21] = 0
                data_set.append([file.split('/')[-1].split('.')[0], department, row[3], row[4], row[6], row[8], row[7], row[21]])

with open('../data_set/lists_on.json', 'w', encoding='utf-8') as f:
    json.dump(data_set, f, ensure_ascii=False)
