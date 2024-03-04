import re

from field import Field


class Email(Field):
    
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):

        match = re.search(r"[A-Za-z]+[\w\.]+@\w+\.[a-zA-Z]{1,}[^\.-]", value)
        email_address = match.group() if match else "" 
        
        if len(value) != len(email_address):
            raise ValueError("The address must contain exactly one @ symbol."\
                            "The address must include the characters A-Za-z0-9 before and after the @ symbol."\
                            "The local name can contain the characters a-zA-z0-9 and the characters: ! #$%&'r; + - . = ? ^^ _ ` { } ½ ~."\
                            "The following characters cannot be used: < > ( ) [ ] @ , ; : \ /  * or space."\
                            "The domain name must contain two text lines separated by a dot."\
                            "The last character cannot be a minus sign, a hyphen, or a dot.")
        self.__value = value
