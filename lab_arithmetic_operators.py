# Additon Operator
# Subtraction Operator
# Multiplication Operator
# Power Operator 
# Division Operator
# Floor Division Operator 

# Additon Operator - used to carry out addition operation
bio = 70
phy = 67
chm = 89

sum_score = bio + phy + chm
print("Student Total Score: ", sum_score)

print()

# Subtraction Operator - used to carry subtraction operation
item_cost = int(input("Enter Item Cost: "))
sales_price = int(input("Enter Sales Price:"))

profit = sales_price - item_cost

if profit > 0:
    profit = "Profit"
else:
    profit = "Loss"

print("Profit Status: ", profit)

# Multiplication Operator - used for carrying out multiplications
monthly_google_subscription = 9000
months_in_yr = 12
total_subscription = monthly_google_subscription * months_in_yr
print("The total amount of Google sucbscription per year in (USD): ", total_subscription)

