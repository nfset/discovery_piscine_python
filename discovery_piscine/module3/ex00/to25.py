number = int(input())

if (number > 25):
    print("Error!")
else:
    while (number <= 25):
        print(f'Inside the loop, your number is: {number}')
        number += 1
