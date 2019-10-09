number=input("Enter phone Number : ")

digit={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero",
}
out=""
for ch in number:
    out+=digit.get(ch,"!")+" "

print(out)