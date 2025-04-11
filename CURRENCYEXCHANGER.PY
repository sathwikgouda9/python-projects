from forex_python.converter import CurrencyRates
#requirements.txt: pip install forex-python otherwise code doesnot work;
def convert_currency(amt, fromC, toC):
    c = CurrencyRates()
    try:
        convertedamt = c.convert(fromC.upper(), toC.upper(), amt)
        print(f"{amt} {fromC.upper()} = {convertedamt:.2f} {toC.upper()}")
    except Exception as e:
        print("Error:", e)

amt = float(input("Enter amount: "))
fromC = input("From currency (e.g. USD): ")
toC= input("To currency (e.g. INR): ")

convert_currency(amt, fromC, toC)
