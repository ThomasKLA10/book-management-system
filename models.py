from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Genre model
class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    book_count = Column(Integer, default=0)  # Add this line for book count
    books = relationship('Book', back_populates='genre')  # Relationship to Book

    def __repr__(self):
        return f"<Genre(name='{self.name}', book_count='{self.book_count}')>"

# Author model
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    book_count = Column(Integer, default=0)  # Add this line for book count
    books = relationship('Book', back_populates='author')  # Relationship to Book

    def __repr__(self):
        return f"<Author(name='{self.name}', book_count='{self.book_count}')>"

# Book model
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))  # Foreign key to Author
    genre_id = Column(Integer, ForeignKey('genres.id'))    # Foreign key to Genre
    publication_date = Column(Date)
    description = Column(Text)

    # Relationships
    author = relationship('Author', back_populates='books')  # Relationship with Author
    genre = relationship('Genre', back_populates='books')    # Relationship with Genre

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author.name}', genre='{self.genre.name}')>"

