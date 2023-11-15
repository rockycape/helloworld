# This program converts a number with a given base between 2 - 36
# to a number with base as specified by the user

def convert_base(number, from_base, to_base):
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        raise ValueError("Base must be between 2 and 36")

    # Convert the number to decimal first
    decimal_number = int(str(number), from_base)

    # Convert the decimal number to the desired base
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % to_base
        result = str(remainder) + result
        decimal_number //= to_base

    return result if result else "0"

# Get input from the user
number = input("Enter the number: ")
from_base = int(input("Enter the base of the input number (2-36): "))
to_base = int(input("Enter the base to convert to (2-36): "))

# Convert to the specified base
converted_number = convert_base(number, from_base, to_base)

# Display the result
print(f"The {from_base}-based representation of {number} is: {converted_number} in base {to_base}")
