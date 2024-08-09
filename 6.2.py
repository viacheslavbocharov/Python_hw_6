user_seconds = int(input("Enter digit in a range from 0 to 8640000: "))
days = user_seconds // 86400
hours = (user_seconds - days * 86400) // 3600
minutes = (user_seconds - days * 86400 - hours * 3600) // 60
seconds = user_seconds - days * 86400 - hours * 3600 - minutes * 60

if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)


day_in_correct_form = None
if days in {1, 21, 31, 41, 51, 61, 71, 81, 91}:
    day_in_correct_form = 'день'
elif days % 10 in {2, 3, 4} and not 11 <= days % 100 <= 14:
    day_in_correct_form = 'дня'
else:
    day_in_correct_form = 'дней'

print(f"{days} {day_in_correct_form}, {hours}:{minutes}:{seconds}")
