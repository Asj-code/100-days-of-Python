#Password Generator Project
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for letter in range (0, len(letters)):
  random_letters = random.sample(letters, nr_letters)

for number in range (0, len(numbers)):
  random_numbers = random.sample(numbers, nr_numbers)

for symbol in range (0, len(symbols)):
  random_symbols = random.sample(symbols, nr_symbols)

random_password_generated = random_letters + random_symbols + random_numbers

join_password = ''.join(random_password_generated)

print("Your password is: " + join_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# convert the string into a list of characters
# shuffle the list of characters randomly
# convert the list of characters back into a string

charlst = list(join_password)        
random.shuffle(charlst)     
new_random_password = ''.join(charlst)
print(new_random_password)