with open("Currency Converter.txt","r") as f:
    lines = f.readlines()

currecyDict = {}
for line in lines:
    parsed = line.split("\t")
    currecyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:- "))
print("Enter the name on the currency you want to convert this amount to? Available options \n")
[print(item) for item in currecyDict.keys()]

currency = input("Please enter one of these value: \n")
print(f"{amount} INR is equal to {amount * float(currecyDict[currency])} {currency}")