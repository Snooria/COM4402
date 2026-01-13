#Activity 5 – Bug Hunt: Discount Function


discount=0
def apply_discount(price):
    if price > 100:
        discount = 10
    final_price = price - discount
    return final_price

p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)
