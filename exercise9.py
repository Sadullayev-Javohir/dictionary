"""Lug'atni tekshirish va qo'shish. Lug'atga yangi element qo'shishdan oldin,
mavjudligini tekshiring."""

inputKey = input("Kalit kiriting: ")
inputValue = input("Qiymat kiriting: ")


myDict = {
    "number1": 10022,
    "number2": 19202,
    "number3": 10922,
    "number4": 29232
}

myDict[inputKey] = inputValue

print(myDict)

    
