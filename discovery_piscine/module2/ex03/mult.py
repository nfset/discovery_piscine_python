first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
result = first_number * second_number

print(f'{first_number} x {second_number} = {result}')
if (result > 0):
    print("The result is postive")
elif (result < 0):
    print("The result is negative")
else:
    print("The result is postive and negative")