import json
import re
import osmnx as ox
from strsimpy.longest_common_subsequence import LongestCommonSubsequence
from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, NewsNERTagger, \
    NamesExtractor, Doc

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
morph_vocab = MorphVocab()
lcs = LongestCommonSubsequence()
data_set_expenses = json.load(open("../data_set/expenses.json", encoding='utf-8'))

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


def getTypeRoom(type_room):
    if isinstance(type_room, int) or type_room == "Удовлетворительное":
        return 2
    if type_room == "Ветхое":
        return 1
    if type_room == "Хорошее":
        return 3
    if type_room == "Аварийное":
        return 3
    print('getTypeRoom', type_room)
    exit(1)


def getAddress(name):
    match = re.match(r'([\s\S]*?),\s(\d{6}[\S\s]*),\s([\d-]*)', name)
    if match and match.groups():
        return match.groups()[0], match.groups()[1], match.groups()[2]
    else:
        match = re.match(r'([\s\S]*?),\s([\S\s]*),\s([\d-]*)', name)
        if match and match.groups():
            return match.groups()[0], match.groups()[1], match.groups()[2]
        else:
            print('getAddress', name)
            exit(1)


def normalize(text):
    text = re.sub(r'(?:^|\s)Св. Иннокентия[.]*\s', " Святителя Иннокентия ", text)
    text = re.sub(r'[\(\),.\-\/№;:]', " ", text)
    text = re.sub(r'(?:^|\s)[гспдткм][.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)зд[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)пр[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)пгт[.]*\s', " ", text)
    text = re.sub(r'(?:^|\s)мкр[.]*\s', " ", text)
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


def comparisonArray(a, b):
    count = len(b)
    for bel in b:
        if bel in a:
            count -= 1
        if count == 0:
            return True
    return False

data_set_lemmatize = dict()
def getExpenses(year, month, department, address, print_test=False):
    if print_test:
        print(year, month, department, address)
    # department_tokens = lemmatize(department)
    address_tokens = lemmatize(address)
    array = list()
    if year not in data_set_lemmatize:
        data_set_lemmatize[year] = dict()
        data_set_lemmatize[year][month] = list()
        for element in data_set_expenses:
            if year == element[0]:
                if int(element[7].split(".")[1]) == month:
                    element.append(True)
                    # element_expenses_tokens = lemmatize(f"{element[1]} {element[5]}")
                    # if comparisonArray(element_expenses_tokens, department_tokens):
                    element_address_tokens = lemmatize(element[5])
                    data_set_lemmatize[year][month].append({"tokens": element_address_tokens, "element": element})
                    if print_test:
                        print(address_tokens, element_address_tokens)
                    if comparisonArray(address_tokens, element_address_tokens):
                        element[8] = False
                        array.append(element)
    else:
        if month not in data_set_lemmatize[year]:
            data_set_lemmatize[year][month] = list()
            for element in data_set_expenses:
                if year == element[0]:
                    if int(element[7].split(".")[1]) == month:
                        element.append(True)
                        # element_expenses_tokens = lemmatize(f"{element[1]} {element[5]}")
                        # if comparisonArray(element_expenses_tokens, department_tokens):
                        element_address_tokens = lemmatize(element[5])
                        data_set_lemmatize[year][month].append({"tokens": element_address_tokens, "element": element})
                        if print_test:
                            print(address_tokens, element_address_tokens)
                        if comparisonArray(address_tokens, element_address_tokens):
                            element[8] = False
                            array.append(element)
        else:
            for element_address in data_set_lemmatize[year][month]:
                if element_address["element"][8] and comparisonArray(address_tokens, element_address["tokens"]):
                    flag = True
                    for el in array:
                        if el[3] == element_address["element"][3]:
                            flag = False
                            break
                    if flag:
                        element_address["element"][8] = False
                        array.append(element_address["element"])

    return array


class Premises:
    def __init__(self):
        self.data = dict()
        self.data_set = json.load(open("../data_set/lists_on.json", encoding='utf-8'))
        area_house_cod = dict()
        for element in self.data_set:
            if element[3] != element[3] or element[3] == 0:
                continue
            name, address, house_cod = getAddress(element[2])
            if element[1] not in self.data:
                self.data[element[1]] = dict()
            if house_cod not in self.data[element[1]]:
                self.data[element[1]][house_cod] = dict()
            if house_cod not in area_house_cod:
                area_house_cod[house_cod] = dict()
                area_house_cod[house_cod]["address"] = element[2]
            else:
                area_house_cod[house_cod]["address"] = element[2]
            months, year = getMonth(element[0])
            if year not in self.data[element[1]][house_cod]:
                self.data[element[1]][house_cod][year] = dict()
            for month in months:
                if month not in self.data[element[1]][house_cod][year]:
                    if "room_all_house" not in area_house_cod[house_cod]:
                        area_house_cod[house_cod]["room_all_house"] = element[5]
                    if element[5] == 0:
                        element[5] = area_house_cod[house_cod]["room_all_house"]
                    self.data[element[1]][house_cod][year][month] = {
                        "address": area_house_cod[house_cod]["address"],
                        "year_foundation": int(element[3]),
                        "room_area": element[4],
                        "room_all_house": element[5],
                        "room_occupied": element[6],
                        "type": getTypeRoom(element[7])
                    }
                    # TODO сделать тип помещения


premises = Premises()
count = 0
for department in premises.data:
    for index, house_cod in enumerate(premises.data[department]):
        print(index, len(premises.data[department]), house_cod)
        for year in premises.data[department][house_cod]:
            if year < 2022:
                for month in premises.data[department][house_cod][year]:
                    if premises.data[department][house_cod][year][month]["room_occupied"] > 0:
                        address = premises.data[department][house_cod][year][month]["address"]
                        array = getExpenses(year, month, department, address)
                        if len(array) > 0:
                            for element in array:
                                if "expenses" not in premises.data[department][house_cod][year][month]:
                                    premises.data[department][house_cod][year][month]["expenses"] = list()
                                premises.data[department][house_cod][year][month]["expenses"].append({
                                    "type": element[3],
                                    "price": element[6]})
with open('../data_set/full.json', 'w', encoding='utf-8') as f:
    json.dump(premises.data, f, ensure_ascii=False)



