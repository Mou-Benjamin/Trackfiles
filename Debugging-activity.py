# Debugging with breakpoints
# Program with logical error
def calculate_total(price, quantity):
    total = price * quantity
    return total

# variables
price = 10
quantity = 5

# Breakpoint can be set here to inspect variables and flow
total_amount = calculate_total(price, quantity)

# Output
print("Total Amount:", total_amount)