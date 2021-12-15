class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def getStr(self):
        return f"{self.title} ({str(self.year)})"
