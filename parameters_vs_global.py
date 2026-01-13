#Activity 4 – Parameter vs Global

def calculate_tax(amount, rate):
   tax=(amount * rate)
   return tax

amount= float(input("enter amount:"))
rate= float(input("enter rate:"))

tax=calculate_tax(amount, rate)
print("tax is: ",tax)

