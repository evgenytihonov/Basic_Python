all_seconds = int(input("Введите время в секундах: "))

days = all_seconds // 3600 // 24
hours = all_seconds // 3600 - days * 24
minutes = all_seconds // 60 % 60
seconds = all_seconds % 60

print(f"Дней: {days}, Часов: {hours}, Минут: {minutes}, Секунд: {seconds}")
