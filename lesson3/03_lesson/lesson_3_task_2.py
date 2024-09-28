from smartphone import Smartphone

# Создаем переменную catalog
catalog = []

# Добавляем пять экземпляров класса Smartphone в список catalog
catalog.append(Smartphone("Apple", "iPhone 13", "+79161112233"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79223334455"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79334445566"))
catalog.append(Smartphone("Google", "Pixel 6", "+79445556677"))
catalog.append(Smartphone("Huawei", "P50", "+79556667788"))

# Цикл для вывода информации о каждом телефоне
for phone in catalog:
    print(phone.get_info())
