import random
import string
import pyfiglet

banner=pyfiglet.figlet_format("Password generator", justify='center')
print(banner, end="")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("How many characters do you want in your password? "))
        if length > 36:
            print("Error: Password length cannot exceed 36 characters.")
            return
        if length < 8:
            print("Warning: Passwords should be at least 8 characters long.")
        password = generate_password(length)
        print("Your generated password is:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
print("Thank you for using password generator")