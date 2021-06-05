class books:
    books_counter = 0
    id_book = 0

    def __init__(self, name, price, number_of_book):
        self.name = name
        self.price = price
        self.number_of_book = number_of_book
        books.books_counter = books.books_counter + number_of_book
        books.id_book = books.id_book + 1

    def __str__(self):
        return f' name of book: {self.name} \n book_id: {books.id_book}\n price: {self.price} \n ' \
               f'number of this book:{self.number_of_book} \n total books: {books.books_counter}'


b = books('pashas', 1994, 4)
a = books('pasha', 1990, 2)

print(a)
