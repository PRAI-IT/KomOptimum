import os
import json
import pandas as pd

data_set = list()
dir_expenses = "../train_data/KC_TR_KR/"
for file in os.listdir(dir_expenses):
    if os.path.splitext(file)[-1] in (".xlsx", ".xls") and file in ["KR on 01.01.2017.xlsx","KR on 01.01.2018.xlsx","KR on 01.01.2019.xlsx"]:
        dataframe = pd.read_excel(open(dir_expenses + file, 'rb'),
                                  skiprows=lambda x: x in [0, 1, 2, 3, 4, 5, 6, 7])
        for index, row in dataframe.iterrows():
            if not row[1] != row[1] and not row[2] != row[2]:
                data_set.append([row[2], row[3], "", str(row[10])])
    if os.path.splitext(file)[-1] in (".xlsx", ".xls") and file in ["KR on 01.01.2020.xlsx","KR on 01.01.2021.xlsx","KR on 01.01.2022.xlsx","KR on 01.01.2023.xlsx"]:
        dataframe = pd.read_excel(open(dir_expenses + file, 'rb'),
                                  skiprows=lambda x: x in [0, 1, 2, 3, 4, 5, 6, 7, 8])
        for index, row in dataframe.iterrows():
            if not row[1] != row[1] and not row[2] != row[2]:
                data_set.append([row[2], row[4], str(row[5]), str(row[6])])
    if os.path.splitext(file)[-1] in (".xlsx", ".xls") and file in ["KS on 01.01.2017.xls","KS on 01.01.2018.xls","KS on 01.01.2019.xls"]:
        dataframe = pd.read_excel(open(dir_expenses + file, 'rb'),
                                  skiprows=lambda x: x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        for index, row in dataframe.iterrows():
            if not row["Unnamed: 1"] != row["Unnamed: 1"] and not row[2] != row[2]:
                data_set.append([row[2], row[5], str(row[3]), str(row[4])])
    if os.path.splitext(file)[-1] in (".xlsx", ".xls") and file in ["KS on 01.01.2020.xlsx", "KS on 01.01.2021.xlsx", "KS on 01.01.2022.xlsx", "KS on 01.01.2023.xls"]:
        dataframe = pd.read_excel(open(dir_expenses + file, 'rb'),
                                  skiprows=lambda x: x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        for index, row in dataframe.iterrows():
            if not row[1] != row[1] and not row[2] != row[2]:
                data_set.append([row[2], row[4], str(row[5]), str(row[6])])


with open('../data_set/kc_tr_kr.json', 'w', encoding='utf-8') as f:
    json.dump(data_set, f, ensure_ascii=False)
