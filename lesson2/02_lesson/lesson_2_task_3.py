import math

def square(side):
    return side * side

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        side = input("Введите сторону квадрата от 0 до 100 (в сантиметрах): ")
        
        # Проверка на целое число
        if not side.isdigit():
            raise ValueError("Вы можете ввести только целое положительное число - от 0 до 100!")
        
        side = int(side)

        if 0 <= side <= 100:
            area = square(side)
            print(f"Площадь квадрата равна {area} сантиметров.")
            break
        else:
            print("Введенное число должно быть от 0 до 100.")
            
    except ValueError as e:
        print(e)
    
    attempts += 1

if attempts == max_attempts:
    print("Неправильный ввод!!!")
