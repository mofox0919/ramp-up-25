from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()
books = []

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: date

class BookInput(BaseModel):
    title: str
    author: str
    year: date

@app.get("/books/")
def getBooks():
    return books

@app.get("/books/{id}")
def getBook(id: int):
    return books[id]

@app.delete("/books/{id}")
def deleteBook(id: int):
    del books[id]

@app.post("/books/")
def addBook(item: BookInput):
    new_book = Book(
        id = len(books),
        title=item.title,
        author=item.author,
        year=item.year
    )
    books.append(new_book)
    return new_book 

@app.post("/books/{id}")
def addBook(item: BookInput, id: int):
    books[id].title = item.title
    books[id].author = item.author
    books[id].year = item.year