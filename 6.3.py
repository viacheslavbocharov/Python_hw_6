import copy
user_number = input("Enter any integer: ")
str_list = list(user_number)

int_list = [int(digit) for digit in str_list]

mult = 1
for i in int_list:
    mult *= i

if mult != 0:

    while mult > 9:
        number = mult
        int_number_list = [int(digit) for digit in str(number)]
        result = 1
        for i in int_number_list:
            result *= i
            mult = result

print(f"{user_number} -> {mult}")