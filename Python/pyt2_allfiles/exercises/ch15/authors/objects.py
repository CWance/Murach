from dataclasses import dataclass


# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)

    def __str__(self):
        string = ""
        for i in self.__list:
            string += (str(i) + ", ")
        return string[:len(string) - 2]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__list):
            result = self.__list[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration


@dataclass
class Book:
    title: str = ""
    authors: Authors = None

    def getDescription(self):
        return f"{self.title} by {self.authors.__str__()}"

    def __str__(self):
        return self.title + " by " + str(self.authors)


@dataclass
class Author:
    firstName: str = ""
    lastName: str = ""

    def __str__(self):
        return self.firstName + " " + self.lastName
