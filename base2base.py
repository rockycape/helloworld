# If you specify the base of the input number, you can use 
# the function int(number_input, base) which ouputs the number in decimal. 
print('This program converts a number from any base to decimal')
print('What is the base of the number?')
b = int(input())  # Convert to integer
print('What is the number?')
ni = input()
decimal_number = int(ni, b)
print(f"The decimal representation of {ni} in base {b} is: {decimal_number}")