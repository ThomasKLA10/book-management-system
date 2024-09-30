# Book Management System

## Overview
The Book Management System is a web application that allows users to manage their book collections effectively. Users can perform CRUD (Create, Read, Update, Delete) operations on book entries, making it easy to maintain and organize their libraries. The application is built using Flask and utilizes a PostgreSQL database for data storage.

## Project Setup Instructions

### Prerequisites
- **Docker:** Ensure you have Docker installed on your machine.
- **Docker Compose:** This project uses Docker Compose to manage services.

### Running the Application Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/book-management-system.git
   cd book-management-system
2. **Build and run the application using Docker Compose:**

    ```bash
     docker-compose up --build
3. **Access the application: Open your web browser and navigate to http://localhost:5000.**

### Docker Commands

- To start the application:
    ```bash
    docker-compose up
   
- To stop the application:
    ```bash
    docker-compose down
  
- To view logs:
    ```bash
    docker-compose logs
  
### Features
- Add new books to the collection.
- View a list of all books.
- Edit existing book details.
- Delete books from the collection.
- Input validation for all forms.

### Known Issues
- The application may not handle concurrent database access properly under heavy load.

