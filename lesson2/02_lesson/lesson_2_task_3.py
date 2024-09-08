import math

def square(side):
    return math.ceil(side) * math.ceil(side)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        side = float(input("Введите сторону квадрата от 1 до 100 (в сантиметрах): "))
        
        # Проверка на допустимый диапазон
        if 1 <= side <= 100:
            area = square(side)
            print(f"Площадь квадрата равна {area} сантиметров.")
            break
        else:
            print("Введенное число должно быть от 1 до 100.")

    except ValueError:
        print("Вы можете ввести только число в диапазоне от 1 до 100 с точностью до четырех знаков после точки.")
    
    attempts += 1

if attempts == max_attempts:
    print("Неправильный ввод!!!")
