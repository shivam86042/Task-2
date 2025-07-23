import random
import string

def generate_password(length):
    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the combined list
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Please enter a positive number.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a number.")
