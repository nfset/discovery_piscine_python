my_age = int(input("Please tell me your age "))

i = 1
print(f'You are currently {my_age} years old!')
while(i <= 3):
    my_age += 10
    print(f'In {i * 10} years, you will be {my_age} years old')
    i += 1
