import pyperclip  # Module for copying text to the clipboard

# Define the alphabet for encryption/decryption
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Get the user's choice to encrypt or decrypt
while True:
    response = input('Do you want to (e)ncrypt or (d)ecrypt? ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Get the key from the user (number of positions to shift)
while True:
    maxKey = len(SYMBOLS) - 1
    response = input(f'Please enter the key (0 to {maxKey}) to use: ').upper()
    if response.isdecimal() and 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Get the message from the user
message = input(f'Enter the message to {mode}: ').upper()

# Initialize the result variable
translated = ''

# Process each character in the message
for symbol in message:
    if symbol in SYMBOLS:
        # Find the position of the symbol in SYMBOLS
        num = SYMBOLS.find(symbol)

        # Shift the position based on the mode
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # Handle wrapping around the end of SYMBOLS
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add the encrypted/decrypted symbol to the result
        translated += SYMBOLS[num]
    else:
        # Add the symbol unchanged if it's not in SYMBOLS
        translated += symbol

# Displays the result
print(translated)

# Try to copy the result to the clipboard
try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard.')
except:
    pass
