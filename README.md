# Book Management System

## Overview
This Book Management System allows users to manage a collection of books by adding, editing, and deleting books, authors,
and genres. It includes features for tracking the number of books in each genre and by each author. The application is built
using Flask, SQLAlchemy, and PostgreSQL, and can be easily deployed using Docker.


## Project Setup Instructions

### Prerequisites
- **Docker:** Ensure you have Docker installed on your machine.
- **Docker Compose:** This project uses Docker Compose to manage services.

### Running the Application Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/book-management-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd book-management-system
    ```

3. Start the application using Docker:
    ```bash
    docker-compose up --build
    ```

4. Run database migrations:
    ```bash
    docker exec -it your-container-name flask db upgrade
    ```

5. Access the application at `http://localhost:5000`.
  
### Features
- Manage books, authors, and genres.
- Automatically track and display the number of books for each genre and author.
- Easy-to-use interface for adding, editing, and deleting records.
- Search functionality to find books by title or author.

### Usage:
- To add a new book, click on "Add Book" and fill in the form with the book's title, author, genre, and other details.
- To edit or delete a book, click the corresponding buttons next to each book in the list.
- Authors and genres can be managed from their respective pages.




