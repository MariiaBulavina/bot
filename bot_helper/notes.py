import tabulate

from collections import UserDict
import pickle

class NoteBook(UserDict):
    
    def add_note(self, note):
        self.data[self.title] = note


    def delete_note(self, title):
        
        try:
            self.data.pop(title)
        except KeyError:
            return 'You have no notes with this title'
        
        return f'Note with the title {title} has been deleted'

    def create_table(self):

        data = [
        ['title', 'text', 'tegs']
    ]

        for note in self.data.values():
            line = [note.title, note.text, note.tegs]
            data.append(line)
        
    
        result = tabulate.tabulate(data)
        return result


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
          
class Note:

    def __init__(self, title: str, text: str) -> None:

        self.title = title
        self.text = text
        self.tegs = []


    def add_text(self, text):
        self.text += text

    def add_tegs(self, tegs):
        tegs = tegs.split(' ')
        for teg in tegs:
            self.tegs.append(teg)

    def change_note(self, text):
        self.text = text
                
        

    def __str__(self) -> str:
        return f'{self.title}: {self.text} {self.tegs}'    
    
    def __repr__(self) -> str:
        return f'{self.title}: {self.text} {self.tegs}'  