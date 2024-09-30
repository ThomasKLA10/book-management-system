from flask import Flask, render_template, request, redirect, url_for
from database import session
from models import Book, Author, Genre

app = Flask(__name__)


# Home Page: Lists all books
@app.route('/')
def home():
    books = session.query(Book).all()  # Get all books
    genres = session.query(Genre).all()  # Get all genres
    authors = session.query(Author).all()  # Get all authors

    # Display the count of books for each genre and author
    genre_counts = {genre.name: len(genre.books) for genre in genres}
    author_counts = {author.name: len(author.books) for author in authors}

    return render_template('home.html', books=books, genre_counts=genre_counts, author_counts=author_counts)






# Add a Book: Show form and handle book creation
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Find or create the genre and author
        author_name = request.form['author']
        genre_name = request.form.get('genre')

        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            session.add(author)

        genre = session.query(Genre).filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
            session.add(genre)





        # Create a new book with form data and save to DB
        new_book = Book(
            title=request.form['title'],
            author=author,
            genre=genre,
            publication_date=request.form.get('publication_date'),
            description=request.form.get('description')
        )
        session.add(new_book)

        # Increment the book count for genre and author
        genre.book_count += 1
        author.book_count += 1

        session.commit()
        return redirect(url_for('home'))

    genres = session.query(Genre).all()
    authors = session.query(Author).all()
    return render_template('add_book.html', genres=genres, authors=authors)






# Edit a Book: Show edit form and update book info
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = session.query(Book).get(id)
    if request.method == 'POST':
        # Find or create the genre and author
        author_name = request.form['author']
        genre_name = request.form.get('genre')

        author = session.query(Author).filter_by(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            session.add(author)

        genre = session.query(Genre).filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
            session.add(genre)

        # Update book with form data
        book.title = request.form['title']
        book.author = author
        book.genre = genre
        book.publication_date = request.form.get('publication_date')
        book.description = request.form.get('description')

        session.commit()

        # Update book counts
        # Decrease old author's and genre's counts
        old_author = book.author
        old_genre = book.genre
        if old_author != author:
            old_author.book_count -= 1
            author.book_count += 1

        if old_genre != genre:
            old_genre.book_count -= 1
            genre.book_count += 1

        session.commit()
        # return redirect(url_for('home'))
        return redirect('/')

    genres = session.query(Genre).all()
    authors = session.query(Author).all()
    return render_template('edit_book.html', book=book, genres=genres, authors=authors)





# Delete a Book: Remove book by ID
@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = session.query(Book).get(id)
    author = book.author
    genre = book.genre

    session.delete(book)

    # Decrement the book count for genre and author
    author.book_count -= 1
    genre.book_count -= 1

    session.commit()
    return redirect(url_for('home'))

# Search Books: Search by title or author
@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        search_query = request.form['search_query']
        books = session.query(Book).filter(
            (Book.title.ilike(f'%{search_query}%')) | (Book.author.name.ilike(f'%{search_query}%'))
        ).all()  # Find books that match the search query
        return render_template('search_results.html', books=books)
    return render_template('search_form.html')  # Show search form

# Add an Author: Show form and handle author creation
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        author_name = request.form['name']
        new_author = Author(name=author_name)
        session.add(new_author)
        session.commit()
        return redirect(url_for('home'))

    return render_template('add_author.html')  # Render the author form

# Add a Genre: Show form and handle genre creation
@app.route('/add_genre', methods=['GET', 'POST'])
def add_genre():
    if request.method == 'POST':
        genre_name = request.form['name']
        new_genre = Genre(name=genre_name)
        session.add(new_genre)
        session.commit()
        return redirect(url_for('home'))

    return render_template('add_genre.html')  # Render the genre form


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



