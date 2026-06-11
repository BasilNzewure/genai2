var1 = 467467.8484
var2 = 467467 


print(var1)
print(var2)

print(type(var1))
print(type(var2))

var2 = float(var2)
print("The new data type of var2 is: ", type(var2))

mult_var2 = var2 * var2
print(mult_var2)

var2 = str(var2)
print("The new data type of var2 is: ", type(var2))

print("The value of var1 is: ", var1)
var1 = int(var1) # Type casting from float to int
print("The value of var1 is: ", var1)
print(type(var1))