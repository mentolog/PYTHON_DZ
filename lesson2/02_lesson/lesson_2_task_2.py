def is_year_leap(year):
    return year % 4 == 0

year = int(input("Введите год от 1900 до 2099: "))

if 1900 <= year <= 2099:
    result = is_year_leap(year)
    if result:
        print(f"{year} — високосный год: {result}")
    else:
        print(f"{year} — не високосный год: {result}")
else:
    print("Год должен быть в диапазоне от 1900 до 2099.")
