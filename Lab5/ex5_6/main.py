class LibraryItem:
    def __init__(self, title, author, item_id, is_checked_out=False):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.is_checked_out = is_checked_out

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nItem ID: {self.item_id}\nChecked Out: {'Yes' if self.is_checked_out else 'No'}"


class Book(LibraryItem):
    def __init__(self, title, author, item_id, is_checked_out=False, genre=""):
        super().__init__(title, author, item_id, is_checked_out)
        self.genre = genre

    def display_info(self):
        return super().display_info() + f"\nGenre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, is_checked_out=False, duration=0):
        super().__init__(title, director, item_id, is_checked_out)
        self.duration = duration

    def display_info(self):
        return super().display_info() + f"\nDirector: {self.author}\nDuration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, is_checked_out=False, issue_number=0):
        super().__init__(title, publisher, item_id, is_checked_out)
        self.issue_number = issue_number

    def display_info(self):
        return super().display_info() + f"\nPublisher: {self.author}\nIssue Number: {self.issue_number}"


book = Book("Norwegian Wood", "Haruki Murakami", "B001", False, "Bildungsroman")
dvd = DVD("Inception", "Christopher Nolan", "D001", True, 148)
magazine = Magazine("Vogue", "Vogue", "M001", False, 235)

print(book.display_info())
print(book.check_out())
print(book.return_item())

print(dvd.display_info())
print(dvd.check_out())

print(magazine.display_info())
