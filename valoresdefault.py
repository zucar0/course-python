def calculate_total(price, tax=0.05, discount=0):
    total = price + (price * tax) - discount
    return total
total = calculate_total(100, 0.08, 10)
print("Total: ", total)

total2 = calculate_total(220, 0.08)
print("Total2: ", total2)


total3 = calculate_total(220)
print("Total3: ", total3)