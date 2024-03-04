from datetime import datetime

from field import Field


class BirthdayError(Exception):
    pass


class Birthday(Field):
    
    def __init__(self, value):

        self.__value = None
        self.value = value
        super().__init__(value)
        
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        try:
            self.__value = datetime.strptime((str(value)), '%d-%m-%Y').date()
        except ValueError:
            raise BirthdayError

