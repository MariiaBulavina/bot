from collections import UserDict
import pickle

import tabulate


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        try:
            self.data.pop(name)
        except KeyError:
            return 'You have no contacts with this name'
        
        return f'Сontact with the name {name} has been deleted'
        
    def iterator(self, page):

        start_of_iteration = 0
        while True:
            if len(self.data) <= start_of_iteration:
                break
            result = list(self.data.items())[start_of_iteration:start_of_iteration+page]
            yield result
            start_of_iteration += page

    def save(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    def load(self, file_name):
            try:
                with open(file_name, 'rb') as file:
                    file.seek(0)
                    self.data = pickle.load(file)
            except FileNotFoundError:
                pass    
    
    def create_table(self):

        data = [
        ['name', 'phones', 'birthday', 'emails', 'address']
    ]

        for contact in self.data.values():
            line = [contact.name, contact.phones, contact.birthday, contact.emails, contact.address]
            data.append(line)
        
        result = tabulate.tabulate(data)
        return result
