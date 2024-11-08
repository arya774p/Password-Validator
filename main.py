while True:
    password=input("Enter a password : ")

    atleast_8 = len(password) >= 8
    if not atleast_8:
        print("Password should be atleast 8 characters long")
    
    atmost_20 = len(password) <= 20
    if not atmost_20: 
        print("Password should be atmost 20 characters long")

    # Password should not contain any whitespace
    no_whitespace = ' ' not in password    # gives True if no whitespace else False
    if not no_whitespace:   # gives True if there is whitespace else False
        print("Password should not contain any whitespace")
    
    # Password should not contain the word ‘password’ (case-insensitive)
    not_have_password = 'password' not in password.lower()
    if not not_have_password:
        print("password should not contain word password")


    # Password should contain at least one uppercase letter
    contains_upper = False
    contains_lower = False
    has_digit = False
    has_special = False
    special_chars = """!@#$%^&*()_+=}{][|\:;"'<>,.?/"""
    for char in password:
        if char.isupper():
            contains_upper = True

        if ord(char) in range(97,123):  # 97 <= ord(char) <= 122
            contains_lower = True
            
        if char.isdigit():
            has_digit = True
                
        if char in special_chars:
            has_special = True       
    

        if contains_upper and contains_lower and has_digit and special_chars:
            break
    
    if contains_upper==False:   # if not contains_upper
        print("Password should contain aleast one uppercase letter")

    if not contains_lower:
        print("Pass should contain atleast one lowercase char")
        
    if has_digit == False:
        print("Pass should contaon atleast one digit")
        
    if not has_special:
        print("Password should contain atleast one special character")


    if atleast_8 and atmost_20 and no_whitespace and not_have_password and contains_upper and contains_lower and has_digit and has_special:
        print("Password is valid")
        break

