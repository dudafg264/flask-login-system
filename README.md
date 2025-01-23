# Flask Login Project

This project is a simple Flask-based web application demonstrating a basic login system using Flask-WTF, WTForms, and Flask-Bootstrap. It provides a basic authentication mechanism where users can log in with an email and password. The project is designed to be a starting point for building more advanced authentication systems.

## Features
- **Login Form**: Users can log in with an email and password.
- **Form Validation**: Includes validation for required fields, email format, and password length.
- **Dynamic Pages**: Displays success or error pages based on login credentials.
- **Responsive Design**: Styled with Bootstrap for a clean and responsive interface.

## Tech Stack
- Python
- Flask
- Flask-WTF
- WTForms
- Flask-Bootstrap

## How to Use
1. Navigate to the home page (`http://127.0.0.1:5000`).
2. Click on the "Login" link to access the login page.
3. Enter the following test credentials:
   - **Email**: `admin@email.com`
   - **Password**: `12345678`
4. Upon successful login, you will be redirected to the success page. If the credentials are incorrect, you will see an error message.
5. Modify the code in `main.py` to customize the behavior or add new features.

## File Structure
```
├── main.py                # Main application script
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── login.html         # Login page
│   └── success.html       # Success page