from forex_python.converter import CurrencyRates

cur = CurrencyRates()


fromcur = input("Please enter the currency code that has to be converted (USD,TRY,EUR): ").upper() #automatic capitalization


newcur = input("Please enter the currency code to convert: ").upper()

#amount of money statement
money = float(input("Please enter your money: "))

print("You are converting",money,fromcur,"to",newcur)

res = round(cur.convert(fromcur,newcur,money),3)#round shows 3 decimal part after comma

print("The converted rate is",res,newcur )