# Daily Haven Coffee Shop Website

A 3-page Flask website for a local coffee shop called "Daily Haven".

## Features

- Home page with hero section and conversation strip
- Menu page displaying items grouped by category
- Contact form with validation and email sending
- Responsive design based on provided mockup
- Template inheritance for consistent layout
- Environment-based configuration for email credentials

## Setup

1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux)
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your own values
5. Run the application: `python app.py`
6. Visit http://localhost:5000 in your browser

## Environment Variables

Copy `.env.example` to `.env` (never commit `.env` — it's gitignored):

- `SMTP_HOST`: SMTP server host (e.g., smtp.gmail.com)
- `SMTP_PORT`: SMTP server port (e.g., 587)
- `SMTP_USER`: SMTP username/email
- `SMTP_PASS`: SMTP password or app-specific password
- `CONTACT_RECIPIENT`: Email address to receive form submissions
- `SECRET_KEY`: Flask secret key for sessions and security

## Project Structure

- `app.py`: Main Flask application with routes
- `menu_data.py`: Menu items data as list of dictionaries
- `templates/base.html`: Base template with shared layout
- `templates/home.html`: Homepage template
- `templates/menu.html`: Menu page template
- `templates/contact.html`: Contact page with form
- `static/style.css`: CSS styling extracted from mockup
- `requirements.txt`: Python dependencies

## Design Notes

- Colors, fonts, and layout match the provided mockup
- Uses Google Fonts: Fraunces, Work Sans, IBM Plex Mono
- Implements responsive design from the mockup
- Menu items are grouped by category for easy maintenance
- Contact form includes validation and success/error feedback

## Testing Notes

To test the contact form email functionality:
1. Set up a test email account (like Gmail)
2. Enable 2-factor authentication and generate an app password
3. Set the environment variables accordingly in `.env`
4. Submit the contact form and verify email receipt

For development without email sending, the form will still validate and show success/error messages.
