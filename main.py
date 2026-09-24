# Password Strength Analyzer - Task 1 | Thiranex Internship
# Author: Shamna

def check_password_strength(password):
    # Conditions
    has_length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password)

    score = sum([has_length, has_upper, has_lower, has_digit, has_special])

    print("\n--- Analysis Report ---")
    print(f"Length >= 8      : {'PASS' if has_length else 'FAIL'}")
    print(f"Uppercase (A-Z)  : {'PASS' if has_upper else 'FAIL'}")
    print(f"Lowercase (a-z)  : {'PASS' if has_lower else 'FAIL'}")
    print(f"Number (0-9)     : {'PASS' if has_digit else 'FAIL'}")
    print(f"Special Char     : {'PASS' if has_special else 'FAIL'}")

    if score == 5:
        return "STRONG - Excellent! Your password is strong."
    elif score >= 3:
        return "MEDIUM - Good, but you can make it stronger."
    else:
        return "WEAK - Please make it stronger."

# Main Program
print("=== Password Strength Analyzer ===")
user_pass = input("Enter your password: ")
result = check_password_strength(user_pass)
print(f"\nFinal Strength: {result}")
