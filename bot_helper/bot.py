
import re

from addressbook import AddressBook
from birthday import BirthdayError
from notes import NoteBook, Note
from phone import PhoneError
from record import Record


book = AddressBook()
notes = NoteBook()


def input_error(func):

    def inner(*args):

        try:
            return func(*args)
        except IndexError:
            return 'Not enough params'
        except KeyError:
            return 'You have no contacts with this name'
        except ValueError:
            return 'You entered incorrect data'
        except BirthdayError:
            return 'You can\'t add a date in this format'
        except PhoneError:
            return 'Phone number must be 10 digits long'

    return inner


def hello(*args):
    return 'How can I help you?'


@input_error
def add_contact(*args):

    name = args[0]

    if name in book:
            return f'A contact with the name {name} already exists'
    else:
        book[name] = Record(name)
        try:
            phone = args[1]
            book[name].add_phone(phone)
            return f'A contact with the name {name} and number: {phone} has been added'
        except IndexError:
            return f'A contact with the name {name} has been added'


@input_error
def add_phone(*args):

    name = args[0]

    if name in book:
        phone = args[1]
        book[name].add_phone(phone)
        return f'Number {phone} has been added for contact {name}'
    else:
        return 'You have no contacts with this name'


@input_error
def change_phone(*args):
    
    name = args[0]
    old_phone = args[1]
    new_phone = args[2]
    record = book.get(name)

    if record:
        message = record.edit_phone(old_phone, new_phone)
        return message
    else:
        raise KeyError


@input_error
def phone(*args):

    name = args[0]
    record = book.get(name)

    if record:
        return record.phones
    else:
        return 'You have no contacts with this name'


@input_error
def show_all_contacts(*args):

    page = int(args[0])

    for record in book.iterator(page):
        print(record)
        print('\nNext page\n')
    return 'These are all your contacts'    


@input_error
def delete_contact(*args):

    name = args[0]
    message = book.delete(name)
    return message


@input_error
def remove_phone(*args):

    name = args[0]
    phone = args[1]
    record = book.get(name)

    if record:
        message = record.remove_phone(phone)
        return message
    else:
        return 'You have no contacts with this name'
    

@input_error
def add_birthday(*args):

    name = args[0]

    if name in book:
        birthday = args[1]
        book[name].add_birthday(birthday)
        return f'A birthday {birthday} has been added to the entry for the name {name}' 
    else:
        return 'Enter a contact name to add a birthday'


@input_error
def days_to_birthday(*args):

    name = args[0]
    record = book.get(name)

    try:
        return record.days_to_birthday() 
    except AttributeError:
        return f'There is no birthday entry in the contact with the name {name}'


@input_error
def find_contact(*args):

    data = args[0]
    search_matches = []

    for contact in book.data.items():
        changed_contact = str(contact).replace('Contact name:', '').replace('phones:', '').replace('birthday:', '').replace('address:', '').replace('emails:', '').replace('None', '')
        result = re.findall(data, str(changed_contact))

        if result:
            search_matches.append(contact)
    return search_matches


@input_error
def find_note(*args):

    data = args[0]
    search_matches = []

    for note in notes.data.items():
        result = re.findall(data, str(note))

        if result:
            search_matches.append(note)
    return search_matches


@input_error
def delete_note(*args):

    title = args[0]
    message = notes.delete_note(title)
    return message


@input_error
def add_email(*args):

    name = args[0]

    if name in book:
        email = args[1]
        book[name].add_email(email)
        return f'Email {email} has been added for contact {name}'
    else:
        return 'You have no contacts with this name'
    

@input_error
def change_email(*args):

    name = args[0]
    old_email = args[1]
    new_email = args[2]
    record = book.get(name)

    if record:
        message = record.edit_email(old_email, new_email)
        return message
    else:
        raise KeyError
    

@input_error
def remove_email(*args):

    name = args[0]
    email = args[1]
    record = book.get(name)

    if record:
        message = record.remove_email(email)
        return message
    else:
        return 'You have no contacts with this name'


@input_error
def add_address(*args):

    name = args[0]

    if name in book:
        address_str = ' '.join(list(args[1:]))
        address = address_str.split(', ')

        book[name].add_address(address)
        return f'Address {address} has been added for contact {name}'
    else:
        return 'You have no contacts with this name'
    

@input_error
def change_address_by_key(*args):
    
    name = args[0]
    key = args[1]
    new_information = args[2]

    record = book.get(name)

    if record:
        message = record.edit_address_by_key(key, new_information)
        return message
    else:
        return 'You have no contacts with this name'


@input_error
def delete_address(*args):

    name = args[0]

    if name in book:
        book[name].delete_address()


@input_error
def add_note(*args):

    title = input('Enter a title for your note: ')
    text = input('Enter the text of your note: ')

    if title in notes:
        exist_question = input(f'Note with title {title} already exist. Do you want to add this text to an existing note? y/n')

        if exist_question == 'y':
            notes[title].add_text(text)
            return f'A text {text} has been added to the note with the title {title}]'

        elif exist_question == 'n':
            return 'Then you need to create a note with a different title' 
    else:
        notes[title] = Note(title, text)
        tag_question = input('Do you want to add tags? y/n ')

        if tag_question == 'y':
            tags = input('Enter tags in the format: #tag #tag1: ')
            notes[title].add_tags(tags)

        return f'Note {title}: {text} was created'
    

@input_error
def change_note(*args):
    
    title = args[0]
    new_text = args[1]
    notes[title].change_note(new_text)
    return f'Note with title {title} has been changed'


@input_error
def change_tag(*args):
    ...


@input_error
def change_title(*args):
    ...    


@input_error
def show_all_notes(*args):
    table = notes.create_table()
    return table


@input_error
def show_contacts_table(*args):
    table = book.create_table()
    return table


def close(*args):
    return 'Good bye!'


def no_command(*args):
    return 'Unknown command'


def help(*args):
    return '''COMMANDS

    To add a contact: 
    add_contact name or add_contact name phone 
    (The phone number must consist of numbers only and be 10 characters long)

    To add a phone number: 
    add_phone name phone 
    (The phone number must consist of numbers only and be 10 characters long)
    
    To change a phone number:
    change name old_phone new_phone

    To view a phone number:
    phone name

    To view entries in a book:
    show_all/show number_of_records_for_one_page

    To end the bot's work:
    good_bye/close/exit/.

    To delete a contact:
    delete_contact/delete name

    To remove a phone number:
    remove_phone/remove name phone

    To add a birthday entry:
    add_birthday name birthday_date
    (Date must be in the format dd-mm-yyyy)

    To get the number of days until next birthday:
    days_to_birthday name

    To find a contact based on matches with several letters or numbers:
    find letter/number

    '''


COMMANDS = {
    help: ['help'],
    hello: ['hello'],
    close: ['good_bye', 'close', 'exit', '.'],

    add_contact: ['add_contact'],
    show_all_contacts: ['show_all_contacts'],
    show_contacts_table: ['show_contacts_table'],
    delete_contact: ['delete_contact'],
    find_contact: ['find_contact'],

    add_phone: ['add_phone'],
    change_phone: ['change_phone'],
    phone: ['phone'],
    remove_phone: ['remove_phone'],

    add_birthday: ['add_birthday'],
    days_to_birthday: ['days_to_birthday'],

    add_email: ['add_email'],
    change_email: ['change_email'],
    remove_email: ['remove_email'],

    add_address: ['add_address'],
    change_address_by_key: ['change_address_by_key'],
    delete_address: ['delete_address'],

    add_note: ['add_note'],
    show_all_notes: ['show_all_notes'],
    find_note: ['find_note'],
    delete_note: ['delete_note'],
    change_title: ['change_title'],
    change_note: ['change_note'],
    change_tag: ['change_tag']


}


@input_error
def get_handler(command):

    for func, k_words in COMMANDS.items():
        for word in k_words:
            if command.startswith(word):
                return func

    return no_command


def main():

    book.load('contacts.bin')
    notes.load('notes.bin')
  
    while True:
        user_input = input('>>> ')

        if not user_input:
            continue

        input_list = user_input.split()

        command = input_list[0].lower()
        data = input_list[1:]

        function = get_handler(command)
        print(function(*data))

        if function.__name__ == 'close':
            book.save('contacts.bin')
            notes.save('notes.bin')
            break


if __name__ == '__main__':
    main()