# OTP Generation and Verification with Python Flask

This project demonstrates how to implement OTP (One-Time Password) generation and verification via email using Python Flask and HTML. It includes user authentication and secure transaction verification.

## Features

- Generate OTP and send it via email
- Validate OTP for user authentication
- Secure user transactions with OTP verification

## Requirements

- Python 3.x
- Flask
- Flask-Mail
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Lavz-8/otp-flask-app.git
    cd otp-flask-app
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root with the following contents:

    ```bash
    FLASK_APP=app.py
    FLASK_ENV=development
    MAIL_SERVER=smtp.your-email-provider.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=your-email@example.com
    MAIL_PASSWORD=your-email-password
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    flask run
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000/`.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Credits
This otp verfication was created by **Lavanya Varadharajan**.

