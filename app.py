from flask import Flask, render_template, request, redirect, url_for
from database import session
from models import Book

app = Flask(__name__)

# Home Page: Lists all books
@app.route('/')
def home():
    books = session.query(Book).all()  # Get all books
    return render_template('home.html', books=books)  # Show home page with book list

# Add a Book: Show form and handle book creation
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Create a new book with form data and save to DB
        new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            genre=request.form.get('genre'),
            publication_date=request.form.get('publication_date'),
            description=request.form.get('description')
        )
        session.add(new_book)
        session.commit()
        return redirect(url_for('home'))
    return render_template('add_book.html')  # Show the add book form

# Edit a Book: Show edit form and update book info
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = session.query(Book).get(id)  # Find the book by ID
    if request.method == 'POST':
        # Update book with form data and save changes
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form.get('genre')
        book.publication_date = request.form.get('publication_date')
        book.description = request.form.get('description')
        session.commit()
        return redirect(url_for('home'))
    return render_template('edit_book.html', book=book)  # Show edit form pre-filled with current book data

# Delete a Book: Remove book by ID
@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = session.query(Book).get(id)  # Find book by ID
    session.delete(book)
    session.commit()
    return redirect(url_for('home'))

# Search Books: Search by title or author
@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        search_query = request.form['search_query']
        books = session.query(Book).filter(
            (Book.title.ilike(f'%{search_query}%')) | (Book.author.ilike(f'%{search_query}%'))
        ).all()  # Find books that match the search query
        return render_template('search_results.html', books=books)
    return render_template('search_form.html')  # Show search form

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)








