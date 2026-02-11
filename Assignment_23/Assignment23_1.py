class BookStore:
    NoOfBooks = 0

    def __init__(self):
        self.Book = ""
        self.Author = ""
        BookStore.NoOfBooks = 1

    def Display(self):
        print("The name of the book : ")
        self.Book = input()

        print("The name of the author : ")
        self.Author = input()

        print("No of books are : ")
        BookStore.NoOfBooks = int(input())

        print(f"{self.Book} by {self.Author}. No of Books : {BookStore.NoOfBooks}")

obj1 = BookStore()
obj1.Display()

obj2 = BookStore()
obj2.Display()