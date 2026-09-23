# /   → Exact division (decimal allowed)
# //  → Integer division (remove decimal)
# %   → Remainder
# **  → Power
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Exact division:", num1 /num2)
print("Integer division:", num1 //num2)
print("Remainder:", num1%num2)
print("Power:",num1** num2)