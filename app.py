from flask import Flask, render_template, request, redirect, url_for
from database import session
from models import Book

app = Flask(__name__)

# Route 1: Home Page ("/")
@app.route('/')
def home():
    books = session.query(Book).all()  # Query all books from the database
    return render_template('home.html', books=books)  # Render the home page with books list



# Route 2: Add Book ("/add")
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get form data and create a new book object
        title = request.form['title']
        author = request.form['author']
        genre = request.form.get('genre')
        publication_date = request.form.get('publication_date')
        description = request.form.get('description')

        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            publication_date=publication_date,
            description=description
        )
        session.add(new_book)  # Add the new book to the session
        session.commit()  # Commit the changes to the database

        return redirect(url_for('home'))  # Redirect to the home page after adding
    return render_template('add_book.html')  # Show the add book form

# Route 3: Edit Book ("/edit/<int:id>")
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = session.query(Book).get(id)  # Get the book by id
    if request.method == 'POST':
        # Update the book's attributes based on form data
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form.get('genre')
        book.publication_date = request.form.get('publication_date')
        book.description = request.form.get('description')

        session.commit()  # Commit the changes to the database
        return redirect(url_for('home'))  # Redirect to the home page after editing
    return render_template('edit_book.html', book=book)  # Show the edit book form with current data

# Route 4: Delete Book ("/delete/<int:id>")
@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = session.query(Book).get(id)  # Get the book by id
    session.delete(book)  # Delete the book from the database
    session.commit()  # Commit the changes to the database
    return redirect(url_for('home'))  # Redirect to the home page after deletion

# Route 5: Search Books ("/search")
@app.route('/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        search_query = request.form['search_query']  # Get the search query from the form
        # Search for books by title or author
        books = session.query(Book).filter(
            (Book.title.ilike(f'%{search_query}%')) | (Book.author.ilike(f'%{search_query}%'))
        ).all()
        return render_template('search_results.html', books=books)  # Render search results page
    return render_template('search_form.html')  # Render search form if GET request

if __name__ == '__main__':
    app.run(debug=True)







