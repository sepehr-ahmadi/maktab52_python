from abc import ABC, abstractmethod


class Person(ABC):
    name: str
    gender: str
    email: str

    def __init__(self, name, gender, email):
        self.name = name
        self.email = email
        self.gender = gender


class relic(ABC):
    _owner: list
    _Title: str
    _year_of_production: int

    def set_owner(self, owner):
        self._owner = owner

    def set_Title(self, Title):
        self._Title = Title

    def set_year_of_production(self, year_of_production):
        self._year_of_production = year_of_production

    @abstractmethod
    def owner_numbering(self):
        pass


class books(relic):

    def __init__(self, Title, owner, publisher, ISBN, year_of_production=0) -> None:
        self.set_owner(owner)
        self.set_Title(Title)
        self.year_of_production = year_of_production
        self.publisher = publisher
        self.ISBN = ISBN

    def owner_numbering(self):
        return len(self._owner)


class poem(relic):
    def __init__(self, Title, owner, format):
        self.Title = Title
        self.owner = owner
        self.format = format


class article(relic):
    def __init__(self, Title, owner):
        pass


class Author(Person):
    def __init__(self, name, gender, email, code, genre):
        super().__init__(name, gender, email)
        self.code = code
        self.genre = genre
