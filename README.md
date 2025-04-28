# FastAPI Blog Application 🚀

A FastAPI-based blogging application that enables users to manage blogs, authenticate via JWT, and interact with a PostgreSQL database. This project demonstrates how to use FastAPI for building secure, fast, and scalable APIs, SQLAlchemy for database operations, and JWT for secure user authentication. 🔐

## Features 🌟:
- **User Authentication**: Secure login system using JWT tokens for access control. 🛡️
- **CRUD Operations for Blogs**: Users can create, read, update, and delete their blogs. ✍️📝
- **Password Hashing**: Passwords are securely hashed using `bcrypt` to ensure data privacy. 🔑
- **JWT Authentication**: JSON Web Tokens (JWT) are used to authenticate and authorize users. 🏷️
- **Database Integration**: Uses PostgreSQL with SQLAlchemy ORM for database handling. 🗃️
- **Pydantic Models**: Input validation and serialization with Pydantic. 📊

## Technologies Used 💻:
- **FastAPI**: A modern web framework for building APIs. 🌐
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database. 📚
- **PostgreSQL**: Relational database for storing blog and user data. 🏫
- **Pydantic**: For data validation and serialization. 🔄
- **JWT**: JSON Web Tokens for secure authentication. 🔐
- **Bcrypt**: Password hashing. 🔒

### Usage 💡:
- **Login**: Users can log in using their username and password, receiving a JWT token for authentication. 👤
- **JWT Token**: Once authenticated, users can use the JWT token to access protected routes, such as creating, updating, and deleting blogs. 🔑
- **Blog Management**: Users can create blogs, edit them, and delete them. Blogs are associated with the user. 📑

### API Endpoints 📡:
- `POST /login`: User login with username and password to get JWT token. 📝
- `POST /blog/`: Create a new blog (requires authentication). ✍️
- `GET /blog/{id}`: Retrieve a single blog by ID. 🏷️
- `GET /blogs/`: Retrieve all blogs. 📃
- `PUT /blog/{id}`: Update a specific blog (requires authentication). 🔄
- `DELETE /blog/{id}`: Delete a specific blog (requires authentication). ❌

## Security 🔐:
- **JWT Authentication**: Every request to access or modify user data is protected by JWT, ensuring that only authenticated users can access their data. 🛡️
- **Password Hashing**: User passwords are hashed with `bcrypt` before being stored in the database, ensuring that passwords are never stored in plaintext. 🔑

## Environment Variables 📂:
- `DATABASE_URL`: URL for your PostgreSQL database. 🌐
- `SECRET_KEY`: A secret key used for signing JWT tokens. 🗝️
- `ALGORITHM`: The algorithm used for JWT token signing (default is `HS256`). ⚙️
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Time (in minutes) after which the access token expires. ⏳

## Author ✍️:
Manoj Kumar Pendem 🧑‍💻
