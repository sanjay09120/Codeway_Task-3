import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a valid length (greater than 0).")
            return
        
        password = generate_password(length)
        
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
