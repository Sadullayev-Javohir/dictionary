"""Lug'atni birlashtirish. Ikki lug'atni birlashtiring va natijaviy lug'atni
qaytaring."""

myDict = {
    "number1": 10022,
    "number2": 19202,
    "number3": 10922,
    "number4": 29232
}

myDict1 = {
    "brand": "Gucci",
    "model": "110",
    "color": "Black",
    "price": 25000
}

myDict.update(myDict1)

print(myDict)
