#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '@']
total_char_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^', '@','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to the PyPassword Generator!")
#nr_letters= int(input("How many letters would you like in your password?\n")) 
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))
char_total = int(input("How many characters would you like your password?\n"))

password = ""
#passwordTest = ""

for character in range(0, char_total):
    password += random.choice(total_char_list)

print("This is the test password: " + password)
'''
for pass_letters in range(0, nr_letters):
    #new_letter = letters[random.randrange(0, len(letters))]
    random_char = random.choice(letters)
    password += random_char
for pass_nums in range(0, nr_numbers):
    #new_num = numbers[random.randrange(0, len(numbers))]
    random_num = random.choice(numbers)
    password += random_num
for pass_symbs in range(0, nr_symbols):
    #new_symb = symbols[random.randrange(0, len(symbols))]
    random_symb = random.choice(symbols)
    password += random_symb

print(password)

password_shuffled = ''.join(random.sample(password, len(password)))
print(password_shuffled)


#Additional option
password_list = []
for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))
for number in range (0, nr_numbers):
    password_list.append(random.choice(numbers))
for symbol in range (0, nr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password2 = ""
for char in password_list:
    password2 += char
print(password2)'''