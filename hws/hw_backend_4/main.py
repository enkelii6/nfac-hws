from fastapi import FastAPI, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from repository import BooksRepository, Book

app = FastAPI()
repo = BooksRepository()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def main_page(request: Request):

    return RedirectResponse("/books")

@app.get("/books")
def get_books(request: Request):
    books = repo.get_all()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "books": books}
    )

@app.get("/books/new")
def books_new(request: Request):

    return templates.TemplateResponse("new.html", {"request": request})

@app.post("/books/new")
def create_book(
        request: Request,
        title: str = Form(),
        author: str = Form(),
        year: int = Form(),
        price: int = Form(),
        poster: str = Form()
):

    new_book = Book(
        title=title,
        author=author,
        year=year,
        price=price,
        poster=poster
    )

    repo.save(new_book)
    return RedirectResponse(url="/books", status_code=303)

@app.get("/books/{book_id}")
def get_one(request: Request, book_id: int):
    book = repo.get_one(book_id)

    return  templates.TemplateResponse(
        "full_page.html",
        {"request": request, "book": book}
    )

@app.get("/search")
def search_books(
        request: Request,
        q: str = Query(..., min_length=2, max_length=50, title="Search query")
):
    books = repo.search_books(q)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "books": books, "search_query": q}
    )

@app.get("/books/{book_id}/edit")
def edit_book_page(request: Request, book_id: int):
    book = repo.get_one(book_id)
    if not book:
        return RedirectResponse("/books", status_code=303)
    return templtates.TemplateResponse("edit.html", {"request": request, "book": book})

@app.post("/books/{book_id}/edit")
def edit_book(
    request: Request,
    book_id: int,
    title: str = Form(),
    author: str = Form(),
    year: int = Form(),
    price: int = Form(),
    poster: str = Form()
):
    updated = repo.update(book_id, {
        "title": title,
        "author": author,
        "year": year,
        "price": price,
        "poster": poster
    })
    return RedirectResponse(url="/books", status_code=303)

@app.post("/books/{book_id}/delete")
def delete_book(book_id: int):
    repo.delete(book_id)
    return RedirectResponse(url="/books", status_code=303)