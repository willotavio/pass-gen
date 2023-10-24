import random

characters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "+-*/,.\\?\"';[]{}()_~^!@#$%&*|<>:`="

def generate_password(length, options):
    try:
        length = int(length)
        password = ""
        choices = []

        # choices array store the chosen options numbers like: choices = {1, 2} -> choices = (numbers and symbols)
        if options[0] != 'none':
            choices.append(options[0])
        c = 1
        while c < len(options):
            if options[c] == 1:
                choices.append(c)
            c += 1

        if len(choices) > 0:
            letter_case = ""
            if choices[0] == 'lowercase' or choices[0] == 'uppercase' or choices[0] == 'lowercase/uppercase':
                letter_case = choices[0]
                choices[0] = 0
            for i in range(length):
                char_type = random.choice(choices)
                if char_type == 0:
                    password += random_char(letter_case)
                elif char_type == 1:
                    password += random_number()
                elif char_type == 2:
                    password += random_symbol()
        return password
    except ValueError:
        return "Provide a valid length"

def random_char(letter_case):
    char = characters[random.randint(0, len(characters) - 1)]
    if letter_case == 'lowercase':
        char = char.lower()
    elif letter_case == 'uppercase':
        char = char.upper()
    else:
        if random.randint(0, 1) == 1:
            char = char.upper()
    return char

def random_number():
    number = numbers[random.randint(0, len(numbers) - 1)]
    return number

def random_symbol():
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    return symbol