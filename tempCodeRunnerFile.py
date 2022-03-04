Active = input("Currency pair : ")
if Active == "" or Active == NULL:
    Active = "EURUSD"
    Active = Active.upper()
    print("Default currency pair =",Active)
else:
    Active = Active.upper()
    print("Your currency pair is",Active)