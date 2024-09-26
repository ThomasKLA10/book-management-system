# test.py
from database import session
from models import Book

# Add a sample book
new_book = Book(title="Sample Book",
                author="John Doe",
                genre="Fiction",
                publication_date="2023-01-01",
                description="A sample book for testing."
                )
session.add(new_book)
session.commit()

# Query the book
book = session.query(Book).filter_by(title="Sample Book").first()
print(book)
