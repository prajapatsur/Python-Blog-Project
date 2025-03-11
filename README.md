# Python Blog Project

This is a simple blog application built using Flask, SQLAlchemy, and Flask-Login. The application allows users to sign up, log in, create posts, and view posts created by other users.

## Features

- User Authentication (Sign Up, Log In, Log Out)
- Create, View, and Delete Posts
- Flash Messages for User Feedback
- Bootstrap for Responsive Design

## Project Structure

```
Python Blog Project/
│
├── website/
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── create_post.html
│   │   └── posts.html
│   └── static/
│       └── style.css
│
└── README.md
```

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/python-blog-project.git
    cd python-blog-project
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `.\myenv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask shell
    >>> from website import create_app, db
    >>> app = create_app()
    >>> with app.app_context():
    ...     db.create_all()
    ```

5. Run the application on terminal:
    ```sh
    python app.py
    ```

## Usage

- Navigate to `http://127.0.0.1:5000/` in your web browser.
- Sign up for a new account or log in with an existing account.
- Create new posts, view posts, and delete your own posts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)

### It is a guided project
[YouTube- Tech With Tim](https://www.youtube.com/@TechWithTim)
