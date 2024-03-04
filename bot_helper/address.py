from field import Field


class Address(Field):

    def __init__(self, address: list):
        self.__value = None
        self.value = address
        self.country, self.city, self.street, self.house, self.apartment = address
        
    @property
    def value(self) -> list:
        
        return self.__value

    @value.setter
    def value(self, address: list) -> None:
        self.__value = address
        if len(address) < 5:
            self.__value = self.__value.extend([None] * (5 - len(address)))

    def __str__(self) -> str:
        return (f'country: {self.country}, city: {self.city}, street: {self.street}, '
                f'house: {self.house}, apartment: {self.apartment}')
