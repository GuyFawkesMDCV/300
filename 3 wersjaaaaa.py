# Function to check if z is a valid operator
def is_valid_operator(z):
    valid_operators = ['+', '-', '*', '/', '//', '%']
    return z in valid_operators

# Function to check if a string represents a valid number
def is_valid_number(s):
    return s.replace(".", "", 1).isdigit()

# Get the language choice
while True:
    language = input('Choose a language (pl for Polish, en for English): ')
    if language in ['pl', 'en']:
        break
    else:
        print('Invalid choice. Please enter "pl" for Polish or "en" for English.')


# Set language-specific prompts and error messages
if language == 'pl':
    prompt = 'Wprowadź'
    error_message_invalid_operator = 'Błąd: Niepoprawny operator. Wprowadź ponownie:'
    error_message_invalid_number = 'Błąd: Niepoprawna cyfra. Wprowadź ponownie:'
    result_message = 'Wynik:'
if language == 'en':
    prompt = 'Enter'
    error_message_invalid_operator = 'Error: Invalid operator. Enter again:'
    error_message_invalid_number = 'Error: Invalid number. Enter again:'
    result_message = 'Result:'


# Prompt for the operator and check its validity
if language == 'pl':
    z = input(f'{prompt} znak:')
else:
        z = input(f'{prompt} sign:')
while not is_valid_operator(z):
    print(error_message_invalid_operator)
    if language == 'pl':
        z = input(f'{prompt} znak:')
    else:
        z = input(f'{prompt} sign:')

# Prompt for numbers based on the language
while True:
    if language == 'en':
        x = input(f'{prompt} number:')
        y = input(f'{prompt} number:')
    else:
        x = input(f'{prompt} liczbę:')
        y = input(f'{prompt} liczbę:')

    # Check if x and y are valid numbers
    if is_valid_number(x) and is_valid_number(y):
        break
    else:
        print(error_message_invalid_number)

# Perform the calculation based on the valid operator
if z == '+':
    result = float(x) + float(y)
elif z == '-':
    result = float(x) - float(y)
elif z == '*':
    result = float(x) * float(y)
elif z == '/':
    # Handle division by zero
    if float(y) != 0:
        result = float(x) / float(y)
    else:
        if language== 'pl':
            print('Błąd: Dzielenie przez zero.')
        else:
            print('Error. Division by zero.')
        result = None
elif z == '//':
    result = int(x) // int(y)
elif z == '%':
    result = float(x) % float(y)
else:
    print('Błąd: Nieoczekiwany błąd.')
    result = None

# Print the result in both languages if it's not None
if result is not None:
    print(f'{result_message} {result}')
