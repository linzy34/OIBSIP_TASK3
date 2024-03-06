import string
import random

def create_password(psd_length, use_letters=True, use_numbers=True, use_special_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_symbols:
        characters += string.punctuation

    if not(use_letters or use_numbers or use_special_symbols):
        print("Error...Please select at least one character type.")
        return None

    password = "".join(random.choice(characters) for _ in range(psd_length))
    return password

def main():
    print("PASSWORD GENERATOR")
    print("....................")

    psd_length = int(input("Enter the length of your password: "))
    use_letters = input("Include letters in your password? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers in your password? (yes/no): ").lower() == "yes"
    use_special_symbols = input("Include symbols in your password? (yes/no): ").lower() == "yes"

    password = create_password(psd_length, use_letters, use_numbers, use_special_symbols)
    if password:
        print("Your password is:", password)

if __name__ == "__main__":
    main()

