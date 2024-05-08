from name import Name
from phone import Phone

class Record:
    def __init__(self, name: str) -> None:
        self.__name = Name(name)
        self.__phones = []

    def add_phone(self, phone: str) -> None:
        self.__phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        self.__phones.remove(self.find_phone(phone))

    def find_phone(self, phone: str) -> Phone:
        return next(p for p in self.__phones if p.get_value() == phone)
    
    def edit_phone(self, phone_to_edit: str, phone: str) -> None:
        self.find_phone(phone_to_edit).set_value(phone)

    def __str__(self) -> str:
        return f"Contact name: {self.__name.get_value()}, phones: {'; '.join(phone.get_value() for phone in self.__phones)}"
    
    def get_name(self) -> Name:
        return self.__name
