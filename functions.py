import random

characters = "abcdefghijklmnopqrstuv"
numbers = "0123456789"
symbols = "+-*/,.\\?\"';[]{}()_~^!@#$%&*|<>:`="

def generate_password(length, options):
    try:
        length = int(length)
        password = ""
        choices = []

        c = 0
        while c < len(options):
            if(options[c] == 1):
                choices.append(c)
            c += 1

        if len(choices) > 0:
            for i in range(length):
                type = random.randint(choices[0], choices[len(choices)-1])
                if type == 0:
                    password += random_char()
                elif type == 1:
                    password += random_number()
                elif type == 2:
                    password += random_symbol()
        return password
    except ValueError:
        return "Provide a valid length"

def random_char():
    char = characters[random.randint(0, len(characters) - 1)]
    if random.randint(0, 1) == 0:
        char = char.upper()
    return char

def random_number():
    number = numbers[random.randint(0, len(numbers) - 1)]
    return number

def random_symbol():
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    return symbol