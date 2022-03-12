# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(0, nr_numbers):
    password_list += random.choice(numbers)

for char in range(0, nr_letters):
    password_list += random.choice(letters)

for char in range(0, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f'Your password is: {password}')


# With append and without random.shuffle

# password_list = []

# for letter in range(0, nr_letters):
#     letter_get = random.choice(letters)
#     password_list.append(letter_get)

# for number in range(0, nr_numbers):
#     number_get = random.choice(numbers)
#     password_list.append(number_get)

# for symbol in range(0, nr_symbols):
#     symbol_get = random.choice(symbols)
#     password_list.append(symbol_get)

# total_len = nr_letters + nr_numbers + nr_symbols
# password = ""

# for character in range(0, total_len):
#     password += password_list.pop(random.randrange(len(password_list)))

# print(password)
