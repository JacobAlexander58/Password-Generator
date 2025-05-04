import random
import string

print("Welcome to the Password Generator")

length=int(input("Enter the length of the password: "))

characters=string.ascii_letters+string.digits+string.punctuation

password="".join(random.choice(characters) for _ in range(length))

print(f"Your password is: \n{password}")