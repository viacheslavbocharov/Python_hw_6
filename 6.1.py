import string

ascii_str = string.ascii_letters

user_letters = input("Enter a range of letters in the format 'a-z': ")

first_letter_index = ascii_str.index(user_letters[0])
second_letter_index = ascii_str.index(user_letters[-1])
print(f"ASCII: {ascii_str}")
print(ascii_str[first_letter_index:(second_letter_index + 1)])

