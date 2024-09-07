def month_to_season(month):
    if month == 12 or month in [1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Неверный номер месяца"

# Пример использования функции
try:
    month = int(input("Введите номер месяца (от 1 до 12): "))
    if 1 <= month <= 12:
        print(month_to_season(month))
    else:
        print("Номер месяца должен быть от 1 до 12.")
except ValueError:
    print("Введите корректное число.")
