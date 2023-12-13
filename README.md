# User Profile Page Web Application

## Overview

Welcome to the User Profile Page web application project! This project is built using Django on the backend and allows users to create and customize their profile pages. Users can write text posts, add a profile picture, and link their Facebook, Twitter, LinkedIn, and GitHub accounts. The application also includes user authentication features such as login, logout, and sign up. The project uses SQLite3 as the database management system.

## Features

1. **Text Posts**: Users can create and share text posts on their profile page.

2. **Profile Picture**: Users have the option to upload and display a profile picture.

3. **Social Media Links**: Users can connect their Facebook, Twitter, LinkedIn, and GitHub accounts to their profile.

4. **User Authentication**: The application provides secure user authentication with features such as login, logout, and sign up.

5. **Database**: SQLite3 is used as the backend database management system to store user data.

## Installation

Follow these steps to set up and run the User Profile Page web application:

1. Clone the repository:
   ```bash
   git clone https://github.com/MoHazem02/User-Profile-Page.git
   ```

2. Change into the project directory:
   ```bash
   cd user-profile-page
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to create the database tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your web browser and navigate to http://localhost:8000 to access the User Profile Page application.

## Configuration

Make sure to update the following configurations in the `settings.py` file:

```python
# settings.py

SECRET_KEY = 'your_secret_key'

# Add your database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Add your allowed hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Update your social media API keys and secrets
# ...

# Set your email configuration for password reset, if needed
# ...
```

## Usage

1. Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```

2. Follow the prompts to create a superuser account.

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Open your web browser and go to http://localhost:8000/admin to log in with the superuser credentials and manage user data.

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Please follow the [contribution guidelines](CONTRIBUTING.md) when contributing.

---

Thank you for using the User Profile Page web application! If you have any questions or issues. Happy coding!
