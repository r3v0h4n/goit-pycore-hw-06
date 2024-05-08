from collections import UserDict
from record import Record

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        key = str(record.get_name())
        self.data[key] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        del self.data[name]