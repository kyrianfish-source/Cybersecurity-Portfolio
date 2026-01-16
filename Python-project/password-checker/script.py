# Password Strength Checker
# This script checks if a password meets basic security requirements.

def check_password(password):
    if len(password) < 8:
        return "Weak: Password too short"
    if password.isalpha():
        return "Weak: Add numbers or symbols"
    return "Strong password"

print(check_password("hello"))
print(check_password("hello123"))
