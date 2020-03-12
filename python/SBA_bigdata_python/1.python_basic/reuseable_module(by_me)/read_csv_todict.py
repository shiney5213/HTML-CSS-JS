# ﻿파일 불러와서 colname는 key로, 값은 value로 하는 dict 만들기

def read_csv(filepath):
    fp = open(filepath, 'r', encoding='utf-8')
    data = fp.read()
    fp.close()

    # 컬럼명 갖고 오기
    colnames = data.split('\n')[0]
    colnames = colnames.split(',')
    # return data
    elements = []

    rows = data.split("\n")

    for row in rows[1:]:
        element = {}
        fields = row.split(",")

        for i in range(len(colnames)):
            element[colnames[i]] = fields[i].replace(' ', '')

        elements.append(element)
    return elements


filepath = './data/company.csv'
read_csv(filepath)
