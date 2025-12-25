#format specifiers = {:flags} format a value based on what flags are inserted


price1 = 5000.2325
price2 = 7620.43
price3 = 9535.22

print(f"price 1 is ${price1:,.2f}")
print(f"price 2 is ${price2:,.2f}")
print(f"price 3 is ${price3:,.2f}")