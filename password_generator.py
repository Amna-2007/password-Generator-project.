import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    
    # Step 1: Character pool banao options ke hisaab se
    chars = string.ascii_lowercase          # a-z hamesha rehga
    
    if use_upper:
        chars += string.ascii_uppercase     # A-Z
    if use_digits:
        chars += string.digits              # 0-9
    if use_symbols:
        chars += string.punctuation         # !@#$%^&* etc.

    # Step 2: Check karo kuch toh select hua ho
    if not chars:
        print("Error: Koi bhi option select nahi kiya!")
        return None

    # Step 3: Password generate karo
    password = ''.join(random.choices(chars, k=length))
    return password


def get_strength(length, upper, digits, symbols):
    score = 0
    if length >= 8:  score += 1
    if length >= 12: score += 1
    if length >= 16: score += 1
    if upper:        score += 1
    if digits:       score += 1
    if symbols:      score += 2
    
    if score <= 2:   return "Kamzor"
    elif score <= 4: return "Theek Hai"
    elif score <= 5: return "Acha"
    else:            return "Bohot Strong"


def main():
    print("=== Password Generator ===\n")

    # User se options lo
    try:
        length = int(input("Password ki length kitni ho? (default 12): ") or 12)
    except ValueError:
        length = 12

    upper   = input("Capital letters include karo? (y/n, default y): ").lower() != 'n'
    digits  = input("Numbers include karo? (y/n, default y): ").lower() != 'n'
    symbols = input("Symbols (!@#$) include karo? (y/n, default y): ").lower() != 'n'

    try:
        count = int(input("Kitne passwords generate karo? (default 1): ") or 1)
    except ValueError:
        count = 1

    print(f"\n--- Tumhare {count} Password(s) ---")
    for i in range(count):
        pwd = generate_password(length, upper, digits, symbols)
        strength = get_strength(length, upper, digits, symbols)
        print(f"{i+1}. {pwd}  [{strength}]")


if __name__ == "__main__":
    main()



   


