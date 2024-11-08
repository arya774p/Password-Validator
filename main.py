

password=input("Enter a password : ")

if len(password) >= 8:
    print("Atleast 8 digit validation checked")

if len(password) <= 20:
    print("Atmost 20 digit validation checked")

# Password should not contain any whitespace
if ' ' not in password:
    print("no whitespace validation checked")

# Password should not contain the word ‘password’ (case-insensitive)
if 'password' not in password.lower():
    print("password validation checked")

# Password should contain at least one uppercase letter
contains_upper = False
for char in password:
    if char.isupper():
        contains_upper = True
        break

if contains_upper:
    print("uppercase validation checked")

# Password should contain at least one lowercase letter - 97-122
contains_lower = False
for char in password:
    if ord(char) in range(97,123):  # 97 <= ord(char) <= 122
        contains_lower = True
        break

if contains_lower:
    print("lowercase validation checked")

# Password should contain at least one digit
has_digit = False
for char in password:
    if char.isdigit():
        if int(char) in range(0,10):
            has_digit = True
            break
if has_digit:
    print("atleast one digit validation checked")

# Password should contain at least one special character (!, @, #, $, %, ^, &, *, (, ), _, +, =, {, }, [, ], |, \, :, ;, ", ', <, >, ,, ., ?, /)

special_chars = """!@#$%^&*()_+=}{][|\:;"'<>,.?/"""
has_special = False
for char in password:
    if char in special_chars :
        has_special = True
        break
if has_special :
    print("contains special characters")