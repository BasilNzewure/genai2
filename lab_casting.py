item_cost = int(input("Enter Item Cost: "))
sales_price = int(input("Enter Sales Price:"))

profit = sales_price - item_cost

print('Item Cost in (USD): ', item_cost)
print("Sales Price in (USD): ", sales_price)
print("Profit in (USD): ", profit)


print("Data Type of item_cost", type(item_cost))
print("Data Type of sales_price", type(item_cost))
print("Data Type of profit", type(profit))



print()
print("Item cost after str conversion")
item_cost = str(item_cost)
sales_price = str(sales_price)

profit = sales_price + item_cost

print('Item Cost in (USD): ', item_cost)
print("Data Type of item_cost", type(item_cost))
print("Profit in (USD): ", profit)
print("Data Type of profit", type(profit))