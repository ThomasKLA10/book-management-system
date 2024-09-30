from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Genre, Author  # Import all models

DATABASE_URL = "postgresql://postgres:password@db:5432/book_management"  # Ensure the URL is correct

# Create an engine and a session
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # This will create all tables: books, genres, authors

Session = sessionmaker(bind=engine)
session = Session()

