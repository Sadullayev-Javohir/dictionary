"""Lug'atdagi eng katta qiymatni topish. Lug'atdagi maksimal qiymatni toping."""

myDict = {
    "number1": 10022,
    "number2": 19202,
    "number3": 10922,
    "number4": 29232
}
max = 0


for i in myDict:
    if max < myDict[i]:
        max = myDict[i]

print(f"Katta qiymat: {max}")