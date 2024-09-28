from StringUtils import StringUtils  # Импортируем класс из другого файла

# Тестирование класса StringUtils
class StringUtilsTester:
    def __init__(self):
        self.utils = StringUtils()

    def run_tests(self):
        # Позитивные тесты
        print("Позитивные тесты:")

        # 1. Тест capitalize
        assert self.utils.capitilize("skypro") == "Skypro", "Ошибка в capitilize()"
        print("1. capitilize() - Успешно")

        # 2. Тест trim
        assert self.utils.trim("   skypro") == "skypro", "Ошибка в trim()"
        print("2. trim() - Успешно")

        # 3. Тест to_list
        assert self.utils.to_list("a,b,c,d") == ["a", "b", "c", "d"], "Ошибка в to_list()"
        print("3. to_list() - Успешно")

        # 4. Тест contains
        assert self.utils.contains("SkyPro", "S"), "Ошибка в contains()"
        print("4. contains() - Успешно")

        # 5. Тест delete_symbol
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro", "Ошибка в delete_symbol()"
        print("5. delete_symbol() - Успешно")

        # Негативные тесты
        print("\nНегативные тесты:")

        # 1. Тест на пустую строку для метода capitilize
        assert self.utils.capitilize("") == "", "Ошибка: capitilize() не обработал пустую строку"
        print("1. capitilize() с пустой строкой - Успешно")

        # 2. Тест на trim с пустой строкой
        assert self.utils.trim("    ") == "", "Ошибка: trim() не обработал строку с пробелами"
        print("2. trim() с пустой строкой - Успешно")

        # 3. Тест to_list с пустой строкой
        assert self.utils.to_list("") == [], "Ошибка: to_list() не обработал пустую строку"
        print("3. to_list() с пустой строкой - Успешно")

        # 4. Тест contains с отсутствующим символом
        assert not self.utils.contains("SkyPro", "Z"), "Ошибка: contains() нашел несуществующий символ"
        print("4. contains() с несуществующим символом - Успешно")

        # 5. Тест delete_symbol с отсутствующим символом
        assert self.utils.delete_symbol("SkyPro", "Z") == "SkyPro", "Ошибка: delete_symbol() удалил несуществующий символ"
        print("5. delete_symbol() с несуществующим символом - Успешно")


# Запуск тестов
if __name__ == "__main__":
    tester = StringUtilsTester()
    tester.run_tests()
