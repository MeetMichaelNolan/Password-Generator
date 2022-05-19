import random

# Asks user if they want letters in password

while True:
    letter = input("Do you want your password to have letters? (y/n) ")
    if letter == 'y':
        break
    elif letter == 'n':
        break
    else:
        print("Unsupported input, please try again.")

# Asks user if they want capital letters in password

while True:
    capLetter = input("Do you want your password to have capital letters? (y/n) ")
    if capLetter == 'y':
        break
    elif capLetter == 'n':
        break
    else:
        print("Unsupported input, please try again.")

# Asks user if they want numbers in password

while True:
    num = input("Do you want your password to have numbers? (y/n) ")
    if num == 'y':
        break
    elif num == 'n':
        break
    else:
        print("Unsupported input, please try again.")

# Asks user if they want symbols in their password

while True:
    symbol = input("Do you want your password to have symbols? (y/n) ")
    if symbol == 'y':
        break
    elif symbol == 'n':
        break
    else:
        print("Unsupported input, please try again.")

# Asks user how long they want their password to be

while True:
    length = int(input(f"Enter desired length of password: "))
    if type(length) != int:
        print("Unsupported input, please try again.")
    else:
        break

# the data we're taking from

letters = ['abcdefghijklmnopqrstuvwxyz']
capLetters = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
numbers = ['0123456789']

# Our password variable
password = ''

# Random generation to pick which data set to take from

while len(password) < length:
    rand = random.randint(1, 4)

    # Random generation to pick from each category

    let = random.randint(0, 25)
    cap = random.randint(0, 25)
    sym = random.randint(0, 7)
    numb = random.randint(0, 9)

    # Creating the password

    if rand == 1 and letter == 'y':
        password = password + letters[0][let]
    elif rand == 1 and letter == 'n':
        pass
    elif rand == 2 and capLetter == 'y':
        password = password + capLetters[0][cap]
    elif rand == 2 and capLetter == 'n':
        pass
    elif rand == 3 and num == 'y':
        password = password + numbers[0][numb]
    elif rand == 3 and num == 'n':
        pass
    elif rand == 4 and symbol == 'y':
        password = password + symbols[sym]
    elif rand == 4 and symbol == 'n':
        pass
    else:
        pass

print(f'Generated Password: {password}')
