# WAP to calculate selling price of book based on cost price and discount.
cp = float(input("Enter cost price: "))

discount = float(input("Enter discount percentage: "))

discount_amount = (cp * discount) / 100
selling_price = cp - discount_amount

print("Selling Price =", selling_price)