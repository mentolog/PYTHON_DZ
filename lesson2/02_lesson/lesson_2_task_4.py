def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        n = int(input("Введите число n (положительное целое): "))
        if n > 0:
            fizz_buzz(n)
            break
        else:
            print("Введенное число должно быть положительным целым числом.")
    except ValueError:
        print("Введите корректное число.")
    
    attempts += 1

if attempts == max_attempts:
    print("Неправильный ввод!!!")
