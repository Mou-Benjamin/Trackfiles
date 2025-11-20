# initialise attempt variable
attempt = 1

# while loop

while attempt <= 8:
    print(f"failed login attempt: {attempt}")
    #increment attempt variable
    attempt += 1
print("Alert: Too many failed login attempts. Account locked.")