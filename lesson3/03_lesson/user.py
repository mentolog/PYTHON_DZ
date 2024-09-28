class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        print(f"Имя: {self.first_name}")

    def print_last_name(self):
        print(f"Фамилия: {self.last_name}")

    def print_full_name(self):
        print(f"Полное имя: {self.first_name} {self.last_name}")

# Пример использования:
user = User("Иван", "Петров")
user.print_first_name()   # Выведет: Имя: Иван
user.print_last_name()    # Выведет: Фамилия: Петров
user.print_full_name()    # Выведет: Полное имя: Иван Петров
