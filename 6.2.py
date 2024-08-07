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

# 0 5... дней
# 1 день
# 2 3 4 дня

day_in_correct_form = None
if days in range(2,5):
    day_in_correct_form = 'дня'
elif days == 1:
    day_in_correct_form = 'день'
else:
    day_in_correct_form = 'дней'

print(f"{days} {day_in_correct_form}, {hours}:{minutes}:{seconds}")
