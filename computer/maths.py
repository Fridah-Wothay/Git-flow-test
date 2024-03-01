# prompt for user input

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division

op = int(input("Enter the choice number:"))

# perform operation based on input
if op == 1:
print("Sum: {} + {} = {}".format(a,b,a+b))
