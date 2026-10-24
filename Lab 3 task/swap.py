a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap: a =", a, ", b =", b)

# Method 1: Pythonic swap (uses a temporary tuple internally)
a, b = b, a

print("After swap:  a =", a, ", b =", b)