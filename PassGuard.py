import re

def password_strength_percentage(password):
    percentage = 0

    # Condition 1: Length
    if len(password) >= 8:
        percentage += 20

    # Condition 2: Uppercase letter
    if re.search(r"[A-Z]", password):
        percentage += 20

    # Condition 3: Lowercase letter
    if re.search(r"[a-z]", password):
        percentage += 20

    # Condition 4: Digit
    if re.search(r"[0-9]", password):
        percentage += 20

    # Condition 5: Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        percentage += 20

    return percentage


# ---------- MAIN PROGRAM ----------
password = input("Enter your password: ")
strength = password_strength_percentage(password)

print(f"\nPassword Strength: {strength}%")

if strength <= 40:
    print("Strength Level: Weak")
    print("Please consider adding:")
    print("- More characters")
    print("- Uppercase letters")
    print("- Digits and special characters")

elif strength <= 80:
    print("Strength Level: Medium")
    print("Good, but you can make it stronger!")

else:
    print("Strength Level: Strong")
    print("Great job! Your password is strong.")