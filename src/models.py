class Article:
    def __init__(self, title, link, date):
        self.title = title
        self.link = link
        self.date = date

    def __str__(self):
        return f"Tytuł: {self.title}\nLink: {self.link}\nData: {self.date}\n"
    
    def __repr__(self):
        return f"Article(title={self.title!r}, link={self.link!r}, date={self.date!r})"