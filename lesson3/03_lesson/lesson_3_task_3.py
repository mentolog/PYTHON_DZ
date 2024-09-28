from address import Address
from mailing import Mailing

# Создаем два экземпляра класса Address для отправителя и получателя
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Невский", "20", "10")

# Создаем экземпляр класса Mailing
mail = Mailing(to_address, from_address, 350, "TRACK123456789")

# Выводим информацию о почтовом отправлении
print(mail.get_mailing_info())
