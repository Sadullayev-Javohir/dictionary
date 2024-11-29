"""Lug'atda kalit mavjudligini tekshirish. Lug'atda ma'lum bir kalit bor yoki
yo'qligini tekshiring."""

inputKey = input("Kalit kiriting: ")
text = ""

myDict = {
    "number1": 10022,
    "number2": 19202,
    "number3": 10922,
    "number4": 29232
}

if inputKey in myDict:
    text = f"Kalit bor: {inputKey}"
else:
    text = f"Kalit yo'q: {inputKey}"

print(text)
