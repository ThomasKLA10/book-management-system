from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    author = Column(String(100), nullable=False)
    genre = Column(String(50))
    publication_date = Column(Date)
    description = Column(Text)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}')>"
