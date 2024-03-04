from field import Field


class PhoneError(Exception):
    ...


class Phone(Field):

    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        
        if len(str(value)) == 10 and str(value).isdigit():
            self.__value = value
        else:
            raise PhoneError
     
