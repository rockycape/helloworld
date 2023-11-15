# You can use the int() function in Python, which allows you to specify the base of the input number, and then use the hex(), bin(), or oct() functions to convert the resulting decimal number to hexadecimal, binary, or octal, respectively. 
print('This program converts a number from any base to decimal')
print('What is the base of the number?')
b = int(input())  # Convert to integer
print('What is the number?')
ni = input()
decimal_number = int(ni, b)
print(f"The decimal representation of {ni} in base {b} is: {decimal_number}")


