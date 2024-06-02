import subprocess
import pyfiglet

cipherhub=pyfiglet.figlet_format("CipherHub")
print(cipherhub)
print("By Harigovind")

def main():
    print("Choose an option:")
    print("1. Check Password Strength")
    print("2. Generate Password")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        passchecker_path = "C:\\Users\\hgpsm\\OneDrive\\Desktop\\Password\\passchecker.py"
        subprocess.run(["python", passchecker_path])
    elif choice == '2':
        passgenerator_path = "C:\\Users\\hgpsm\\OneDrive\\Desktop\\Password\\password_generator.py"
        subprocess.run(["python", passgenerator_path])
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
