from datetime import datetime, timedelta

current_time = datetime.now()
old_time = datetime(2023, 9, 23, 13, 10, 0)
# Вычитаем 5 минут из текущего времени

# Вычисляем разницу в минутах между текущим временем и новым временем
difference_in_minutes = int((current_time - old_time).total_seconds() / 60)

# Выводим результат
print("Разница в минутах:", difference_in_minutes)

if (difference_in_minutes/80 >= 0.8):
    print("zaebis")
else: print(difference_in_minutes/80)