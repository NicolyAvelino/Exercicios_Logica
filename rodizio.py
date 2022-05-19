placa = input("Placa")
ult = placa[len(placa)-1:len(placa)]
rodizio = {
    "1":"Seg",
    "2":"Ter",
    "3":"Quar",
    "4":"Quin",
    "5":"Sex",
    "0":"Sex"
}
print(rodizio[ult])