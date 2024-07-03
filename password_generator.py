# password_generator.py

import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True):
    """
    Generate a random password with specified length and character types.

    Args:
        length (int): The length of the password. Default is 12.
        use_special_chars (bool): Whether to include special characters. Default is True.
        use_digits (bool): Whether to include digits. Default is True.

    Returns:
        str: The generated password.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters")

    chars = string.ascii_letters
    if use_special_chars:
        chars += string.punctuation
    if use_digits:
        chars += string.digits

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    """Main function to run the Password Generator CLI tool."""
    print("Welcome to PasswordGenerator CLI Tool")
    
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 8): "))
            if length < 8:
                raise ValueError("Password length must be at least 8 characters")

            special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
            digits = input("Include digits? (y/n): ").strip().lower() == 'y'

            password = generate_password(length, special_chars, digits)
            print(f"\nGenerated Password: {password}\n")

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            cont = input("Do you want to generate another password? (y/n): ").strip().lower()
            if cont != 'y':
                print("Thank you for using PasswordGenerator!")
                break

if __name__ == "__main__":
    main()
