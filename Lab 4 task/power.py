base = float(input("Enter the base: "))
exp  = int(input("Enter the exponent: "))

# Method 1: built-in ** operator (from Operators table)
result = base ** exp

# Method 2 (commented): pow() function
# result = pow(base, exp)

print(base, "raised to", exp, "=", result)