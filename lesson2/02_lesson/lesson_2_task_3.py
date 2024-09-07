import math

def square(side):
    return math.ceil(side) * math.ceil(side)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        side = float(input("Введите сторону квадрата от 0 до 100 (в сантиметрах): "))
        if 0 <= side <= 100:
            area = square(side)
            print(f"Площадь квадрата равна {area} сантиметров.")
            break
        else:
            print("Введенное число должно быть от 0 до 100.")
    except ValueError:
        print("Введите корректное число.")
    
    attempts += 1

if attempts == max_attempts:
    print("Неправильный ввод!!!")
