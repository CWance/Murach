from dataclasses import dataclass


class Tasks:
    title: str = ""

    def __init__(self, title):
        self.title = title
        self.__list = []

    def get_title(self):
        return self.title

    def add(self, task):
        self.__list.append(Task(task))

    def complete(self, number):
        self.__list[number - 1].complete()

    def delete(self, number):
        self.__list.pop(number - 1)

    def list(self):
        for i in range(len(self.__list)):
            print(f"{i + 1}. {self.__list[i]}")

    @property
    def count(self):
        return len(self.__list)

@dataclass
class Task:
    title: str = ""
    completed: bool = False

    def complete(self):
        self.completed = True

    def __str__(self):
        task = self.title
        if self.completed:
            task += " (DONE!)"
        return task