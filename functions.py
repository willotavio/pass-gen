import random

characters = "abcdefghijklmnopqrstuv"
numbers = "0123456789"
symbols = "+-*/,.\\?\"';[]{}()_~^!@#$%&*|<>:`="

def generate_password(length, options, characters_options):
    try:
        length = int(length)
        password = ""
        choices = []

        # choices array store the chosen options numbers like: choices = {1, 2} -> choices = (numbers and symbols)
        c = 0
        while c < len(options):
            if options[c] == 1:
                choices.append(c)
            c += 1

        if len(choices) > 0:
            for i in range(length):
                char_type = random.randint(choices[0], choices[len(choices)-1])
                if char_type == 0:
                    password += random_char(characters_options)
                elif char_type == 1:
                    password += random_number()
                elif char_type == 2:
                    password += random_symbol()
        return password
    except ValueError:
        return "Provide a valid length"

def random_char(characters_options):
    char = characters[random.randint(0, len(characters) - 1)]
    if characters_options[0] == 1 and characters_options[1] == 0:
        char = char.lower()
    elif characters_options[0] == 0 and characters_options[1] == 1:
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