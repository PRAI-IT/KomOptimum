import json
import tensorflow as tf
import pandas as pd
import numpy as np
import os

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
SHUFFLE_BUFFER = 500
BATCH_SIZE = 2

data_set = json.load(open("../data_set/full.json", encoding='utf-8'))
count = dict()
countDepartment = dict()
countAll = 0
type_payment = json.load(open("../data_set/payment.json", encoding='utf-8'))


def getResult(expenses):
    result = list()
    for index in type_payment:
        value = 0
        for element in expenses:
            if element['type'] in type_payment[index]:
                value += element['price']
        result.append(value)
    return result


def getArrayExpenses(departmentGlobal,type, all=False):
    arrayToDateFrame = {
        'year_foundation': list(),
        'room_area': list(),
        'room_all_house': list(),
        'room_occupied': list(),
        'type': list(),
        'month': list(),
        'target': list(),
    }
    for department in data_set:
        for house_cod in data_set[department]:
            for year in data_set[department][house_cod]:
                for month in data_set[department][house_cod][year]:
                    if "expenses" in data_set[department][house_cod][year][month]:
                        if department == departmentGlobal or all:
                            arrayToDateFrame['year_foundation'].append(
                                data_set[department][house_cod][year][month]['year_foundation'])
                            arrayToDateFrame['room_area'].append(data_set[department][house_cod][year][month]['room_area'])
                            arrayToDateFrame['room_all_house'].append(
                                data_set[department][house_cod][year][month]['room_all_house'])
                            arrayToDateFrame['room_occupied'].append(
                                data_set[department][house_cod][year][month]['room_occupied'])
                            arrayToDateFrame['type'].append(data_set[department][house_cod][year][month]['type'])
                            arrayToDateFrame['month'].append(int(month))
                            # arrayToDateFrame['year'].append(int(year))
                            for index, price in enumerate(getResult(data_set[department][house_cod][year][month]["expenses"])):
                                if index == type:
                                    arrayToDateFrame["target"].append(price)
                            for element in data_set[department][house_cod][year][month]["expenses"]:
                                if department not in countDepartment:
                                    countDepartment[department] = 1
                                else:
                                    countDepartment[department] += 1
                                if element["type"] not in count:
                                    count[element["type"]] = 1
                                else:
                                    count[element["type"]] += 1
    return arrayToDateFrame


# print('количество платежек по областям', countDepartment)
# print('количество платежек', count)
# for element in count:
#     countAll += count[element]
# print('Общее количество', countAll)
# Дальневосточное ГУ Банка России
for department in data_set:
    for index, typePayment in enumerate(type_payment):
        df = pd.DataFrame(getArrayExpenses(department, index))
        df = df[df['target'] != 0]
        if len(df):
            msk = np.random.rand(len(df)) < 0.8
            x_train = df[msk]
            x_test = df[~msk]
            print(x_test)
            if len(x_train):
                y_train = x_train.pop('target')
                y_test = x_test.pop('target')
                payment_model = tf.keras.Sequential([
                    tf.keras.layers.Dense(64, activation="relu"),
                    tf.keras.layers.Dense(32, activation="relu"),
                    tf.keras.layers.Dense(10, activation="relu"),
                    tf.keras.layers.Dense(1)
                ])
                payment_model.compile(loss=tf.keras.losses.MeanAbsoluteError(reduction=tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE),
                                      optimizer="adam")

                payment_model.fit(x_train, y_train, epochs=20, batch_size=BATCH_SIZE)

                if len(x_test):
                    results = payment_model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)

                if not os.path.isdir(f'../models/{department}'):
                    os.mkdir(f'../models/{department}')
                payment_model.save(f'../models/{department}/{index}.keras')
for index, typePayment in enumerate(type_payment):
    department = "all"
    df = pd.DataFrame(getArrayExpenses(department, index, True))
    df = df[df['target'] != 0]
    if len(df):
        msk = np.random.rand(len(df)) < 0.8
        x_train = df[msk]
        x_test = df[~msk]
        print(x_test)
        y_train = x_train.pop('target')
        y_test = x_test.pop('target')
        payment_model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(10, activation="relu"),
            tf.keras.layers.Dense(1)
        ])
        payment_model.compile(
            loss=tf.keras.losses.MeanAbsoluteError(reduction=tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE),
            optimizer="adam")
        payment_model.fit(x_train, y_train, epochs=20, batch_size=BATCH_SIZE)

        if len(x_test):
            results = payment_model.evaluate(x_test, y_test, batch_size=BATCH_SIZE)

        if not os.path.isdir(f'../models/{department}'):
            os.mkdir(f'../models/{department}')
        payment_model.save(f'../models/{department}/{index}.keras')
