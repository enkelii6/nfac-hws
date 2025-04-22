from dataclasses import dataclass

@dataclass()
class Book:
    title: str
    author: str
    year: int
    price: int
    poster: str
    id: int = 0

class BooksRepository:
    def __init__(self):
        self.books = [
            Book(
                id=1,
                title="Гарри Поттер и философский камень",
                author="Дж. К. Роулинг",
                year=1997,
                price=4990,
                poster="https://m.media-amazon.com/images/I/81iqZ2HHD-L._AC_UF1000,1000_QL80_.jpg"
            ),
            Book(
                id=2,
                title="Властелин Колец: Братство Кольца",
                author="Дж. Р. Р. Толкин",
                year=1954,
                price=3990,
                poster="https://simg.marwin.kz/media/catalog/product/cache/41deb699a7fea062a8915debbbb0442c/c/o/cover1_27_48.jpg"
            ),
            Book(
                id=3,
                title="Убить пересмешника",
                author="Харпер Ли",
                year=1960,
                price=4490,
                poster="https://m.media-amazon.com/images/I/71FxgtFKcQL._AC_UF1000,1000_QL80_.jpg"
            ),
            Book(
                id=4,
                title="Великий Гэтсби",
                author="Ф. Скотт Фицджеральд",
                year=1925,
                price=2990,
                poster="https://m.media-amazon.com/images/I/71FTb9X6wsL._AC_UF1000,1000_QL80_.jpg"
            ),
            Book(
                id=5,
                title="Код да Винчи",
                author="Дэн Браун",
                year=2003,
                price=5490,
                poster="https://s.f.kz/prod/350/349828_1000.jpg"
            )
        ]

    def get_all(self):
        return self.books

    def get_one(self, book_id: int) -> Book | None:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def get_next_id(self) -> int:
        return max(book.id for book in self.books) + 1 if self.books else 1

    def save(self, book: Book):
        book = Book(
            id=self.get_next_id(),
            title=book.title,
            author=book.author,
            year=book.year,
            price=book.price,
            poster=book.poster
        )
        self.books.append(book)

    def search_books(self, query: str) -> list[Book]:
        query = query.lower()
        return [
            book for book in self.books
            if (query in book.title.lower() or
                query in book.author.lower())
        ]

    def update(self, book_id: int, updated_data: dict) -> bool:
        for book in self.books:
            if book.id == book_id:
                book.title = updated_data.get('title', book.title)
                book.author = updated_data.get('author', book.author)
                book.year = updated_data.get('year', book.year)
                book.price = updated_data.get('price', book.price)
                book.poster = updated_data.get('poster', book.poster)
                return True
        return False

    def delete(self, book_id: int) -> bool:
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

