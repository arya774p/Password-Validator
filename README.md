# Password Validator

## Description
Create a password validator that:
- Prompt a password from the user
- Do the validation checks defined below
- Keep prompting the user until a valid password is entered
- Print a message to the user indicating the password is valid

### Approach
- Take a password from the user
- Do the validation checks, without loops, for a single run
- If the password is valid, print a message to the user
- After the first run, make it dynamic


### Validation checks:
- Password should be at least 8 characters long
- Password should be at most 20 characters long
- Password should contain at least one uppercase letter
- Password should contain at least one lowercase letter
- Password should contain at least one digit
- Password should contain at least one special character (e.g. !, @, #, etc.)
- Password should not contain any whitespace
- Password should not contain the word 'password' (case-insensitive)

### Example 1:
#### Input:
```
Enter a password: password
Enter a password: Password123
Enter a password: Pass123
Enter a password: Pass12!
Enter a password: Pass@123!
```
#### Output:
```
Your password is valid
```

### Example 2:
#### Input:
```
Enter a password: password
Enter a password: Password123
Enter a password: Pass123
Enter a password: Pass 123
Enter a password: Pass 123!
Enter a password: Pass@12
Enter a password: Passwo^^^2
```

#### Output:
```
Your password is valid
```

## Requirements
- Python 3.7+
- Use of loops
- Use of conditional statements
- Use of string methods
