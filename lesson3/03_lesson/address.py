class Address:
    def __init__(self, postal_code, city, street, house, apartment):
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def get_full_address(self):
        return f"{self.postal_code}, {self.city}, {self.street}, {self.house} - {self.apartment}"
