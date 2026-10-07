class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        if self.is_borrowed:
            status = "borrowed"
        else:
            status = "available"
        return f"{self.title} by {self.author} ({status})"
