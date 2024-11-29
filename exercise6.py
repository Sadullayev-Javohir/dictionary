"""Lug'atni tartiblash. Lug'atdagi elementlarni qiymatlari bo'yicha tartiblang.
"""

myDict = {
    "number1": 1,
    "number2": 21,
    "number3": 3,
    "number4": 4
}

SortDic = dict(sorted(myDict.items()))

print(SortDic)