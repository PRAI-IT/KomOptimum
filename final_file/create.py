import os
import csv
import re
import json
import pandas as pd
import tensorflow as tf
from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, NewsNERTagger, \
    NamesExtractor, Doc

normalizer = tf.keras.layers.Normalization(axis=None)
segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
morph_vocab = MorphVocab()

type_consumptions = [
    'Расходы прошлого года. Оплата потребления электроэнергии',
    'Расходы прошлого года.Оплата потребления тепловой энергии',
    'Расходы прошлого года.Оплата потребления электроэнергии', 'Другие расходы.Горячее водоснабжение',
    'Другие расходы.Оплата  канализации',
    'Расходы прошлого года, признанные после отчетной даты.Оплата потребления эл.энергии',
    'Другие расходы.Оплата потребления тепловой энергии', 'Другие расходы.Холодное водоснабжение',
    'Расходы прошлого года, признанные после отчетной даты.Оплата потребления тепловой энергии',
    'Оплата потребления тепловой энергии.', 'Другие расходы.Оплата потребления электроэнергии',
    'Расходы прошлого года, признанные после отчетной даты.Оплата потребления электроэнергии',
    'Другие расходы.Горячее водоснабжения', 'Другие расходы.Канализация',
    'Другие расходы.Оплата холодного водоснабжения', 'Другие расходы.Оплата водоснабжения',
    'Другие расходы.Оплата горячего водоснабжения',
    'Другие расходы.Оплата водоотведения',
    'Другие расходы. Расходы прошлого года, признанные после отчетной даты. Оплата потребления газа',
    'Другие расходы.Водоотведение', 'Другие расходы.Оплата потребления газа',
    'Расходы прошлого года.Оплата водоснабжения, канализации',
    'Плата за технологическое присоед. к электрическим сетям (в случаях,не связанных со строительством и кап. ремонтом зданий и сооружений)',
    'Расходы прошлого года, признанные после отчетной даты.Оплата водоснабжения, канализации',
    'Расходы прошлого года..Оплата потребления тепловой энергии',
    'Другие расходы.Холодная вода', 'Другие расходы.Затраты на канализацию',
    'Расходы прошлого года.Оплатата потребления электроэнергии',
    'Другие расходы. Расходы прошлого года. Оплата потребления газа',
    'Затраты на канализацию', 'Оплата за потребление тепловой энергии',
    'Расходы прошлого года. Оплата водоснабжения, канализации', 'Другие расходы.Затраты на горячее водоснабжение',
    'Затраты на холодное водоснабжение',
    'Другие расходы.Оплата водоотведение', 'Оплата за горячее водоснабжение по тарифам',
    'Оплата за горячее водоснабжение  по тарифам',
    'Оплата за горячее водоснабжение', 'Водоснабжение холодная вода',
    'Водоснабжение горячая вода', 'Другие расходы.Оплата канализации', 'Оплата канализации',
    'Оплата водоотведения по тарифам', 'Оплата водоотведения', 'Оплата потребления электроэнергии',
    'Оплата потребления тепловой энергии', 'Оплата холодного водоснабжения', 'Оплата горячего водоснабжения',
    'Оплата холодное водоснабжение', 'Оплата водоснабжения',
    'Оплата потребления электроэнерги', 'Оплата водоотведение', 'Оплата горячее водоснабжение',
    'Оплата горячее водоснабжения', 'Оплата холодное водоснабжения',
    'Оплата горячево водоснабжения', 'Горячее водоснабжение', 'Оплата  канализации',
    'Холодное водоснабжение', 'Другие расходы. Канализация', 'Канализация',
    'Оплата за канализацию', 'Водоотведение', 'Оплата за электроэнергию по тарифам',
    'Оплата за водоотведение по тарифам', 'Оплата за тепловую энергию по тарифам',
    'Оплата за холодное водоснабжение по тарифам',
    'Оплата за холодное водоснабжение  по тарифам', 'Оплата потребления газа по тарифам',
    'Оплата за холодное водоснабжение', 'Оплата за горячее  водоснабжение по тарифам',
    'Оплата за  водоотведение по тарифам', 'Оплата за дизельное топливо', 'Оплата за электроэнергию  по тарифам',
    'Оплата за водоотведение  по тарифам', 'Оплата за  водоотведение  по тарифам', 'Расходы по оплате отопления',
    'Расходы по оплате потребления электроэнергии', 'Расходы по оплате водоотведения',
    'Расходы по оплате холодного водоснабжения', 'Оплата за  горячее водоснабжение по тарифам',
    'Оплата за  тепловую энергию по тарифам', 'Оплата за  электроэнергию по тарифам',
    'Плата за технологическое присоединение к электрическим сетям',
    'Расходы по оплате услуг за холодное водоснабжение по тарифам'
]


def normalize(text):
    text = re.sub(r'(?:^|\s)Св. Иннокентия[.]*\s', " Святителя Иннокентия ", text)
    text = re.sub(r'[\(\),.\-\/№;:]', " ", text)
    text = re.sub(r'(?:^|\s)[гспдткм][.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)зд[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)пр[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)пгт[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)мкр[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)ДГУ[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)[Рр]асчётно кассовый центр[.]*\s', " Расчётно кассовый центр РКЦ ", text)
    text = re.sub(r'(?:^|\s)[Рр]асчетно кассового центра[.]*\s', " Расчётно кассовый центр РКЦ ", text)
    text = re.sub(r'(?:^|\s)Верхнепортовая[.]*\s', " верхнепортовый ", text)
    text = re.sub(r'(?:^|\s)Верхне Портовая[.]*\s', " верхнепортовый ", text)
    text = re.sub(r'(?:^|\s)Вольно[.]*\s', " вольный ", text)
    text = re.sub(r'(?:^|\s)[Зз]дание[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)[Нн]овая[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)ул[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)пер[.]*\s', " ", text)
    return text


def lemmatize(text):
    doc = Doc(normalize(text))
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    return [_.lemma for _ in doc.tokens if _.lemma not in ['"', '.']]


def getMonth(quarter):
    months = [10, 11, 12]
    elements = quarter.split(" ")
    if elements[0] == '1':
        months = [1, 2, 3]
    elif elements[0] == '2':
        months = [4, 5, 6]
    elif elements[0] == '3':
        months = [7, 8, 9]
    return months, int(elements[2])


def comparisonArray(a, b):
    count = len(b)
    for bel in b:
        if bel in a:
            count -= 1
        if count == 0:
            return True
    return False


def getTypeRoom(type_room):
    if isinstance(type_room, int) or type_room == "Удовлетворительное":
        return 2
    if type_room == "Ветхое":
        return 1
    if type_room == "Хорошее":
        return 3
    if type_room == "Аварийное":
        return 3


def getDataMl(department, type, data):
    if not os.path.isdir(f'../models/{department}'):
        model_loaded = tf.keras.models.load_model(f'../models/all/{type}.keras')
    else:
        model_loaded = tf.keras.saving.load_model(f'../models/{department}/{type}.keras')
    df = pd.DataFrame([data])
    return model_loaded.predict(df)[0][0]


arrayResult = list()
# data_set = json.load(open("../data_set/lists_on.json", encoding='utf-8'))
# data_rooms = dict()
# for element in data_set:
#     element.append(lemmatize(element[2]))
#     if element[1] not in data_rooms:
#         data_rooms[element[1]] = dict()
#     months, year = getMonth(element[0])
#     if year not in data_rooms[element[1]]:
#         data_rooms[element[1]][year] = dict()
#     for month in months:
#         if month not in data_rooms[element[1]][year]:
#             data_rooms[element[1]][year][month] = list()
#         data_rooms[element[1]][year][month].append(element)
# with open('../data_set/list_element.json', 'w', encoding='utf-8') as f:
#     json.dump(data_rooms, f, ensure_ascii=False)


data_rooms = json.load(open("../data_set/list_element.json", encoding='utf-8'))
with open('test_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(spamreader):
        print(index)
        if len(arrayResult) == 0:
            arrayResult.append(row)
        else:
            typeData = 3
            if row[0] == "Электроэнергия":
                typeData = 2
            elif row[0] == "Отопление":
                typeData = 4
            elif row[0] == "Водоснабжение":
                typeData = 1
            elif row[0] == "Коммунальные услуги (расходы прошлых лет)":
                typeData = 0
            month, year = row[2].split(" ")
            direction_of_expenses = row[1]
            for type_consumption in type_consumptions:
                if direction_of_expenses.find(type_consumption) > -1:
                    type_direction_of_expenses = type_consumption
                    direction_of_expenses = re.sub(type_consumption + '\s*', '', direction_of_expenses)
                    break
            match = re.search(r'[\d.]*([\s\S]*?)(?:(\s*ст\.[\s\S]*)|$)', direction_of_expenses)
            if match:
                tokens = lemmatize(match.groups()[0])
            find = False
            for department in data_rooms:
                if str(int(month)) in data_rooms[department][year]:
                    for element in data_rooms[department][year][str(int(month))]:
                        if match and comparisonArray(element[8], tokens):
                            find = True
                            if element[3] != element[3]:
                                element[3] = 0
                            element[7] = getTypeRoom(element[7])
                            row[-1] = getDataMl(department, typeData,
                                                (element[3], element[4], element[5], element[6], element[7], int(month)))
                            arrayResult.append(row)
                            break
                if find:
                    break
pd.DataFrame(arrayResult).to_csv('sample.csv')
