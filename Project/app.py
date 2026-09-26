from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from menu_data import MENU_ITEMS
from content import OVERHEARD_LINES, CATEGORY_NOTES
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Flask-Mail configuration
app.config['MAIL_SERVER'] = os.getenv('SMTP_HOST', 'localhost')
app.config['MAIL_PORT'] = int(os.getenv('SMTP_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('SMTP_USER')
app.config['MAIL_PASSWORD'] = os.getenv('SMTP_PASS')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('SMTP_USER')

mail = Mail(app)


def format_ampm(value):
    """Format a time as a lowercase 12-hour clock: 7am, 6:30pm, 12pm.

    Single source of truth for time display, so "7am - 4pm" stays correct
    everywhere instead of each template inventing its own suffix.
    """
    hour = value.hour % 12 or 12
    suffix = 'am' if value.hour < 12 else 'pm'
    if value.minute:
        return f'{hour}:{value.minute:02d}{suffix}'
    return f'{hour}{suffix}'


app.add_template_filter(format_ampm, 'ampm')


@app.route('/')
def home():
    overheard = [
        {'time': format_ampm(line['time']), 'quote': line['quote']}
        for line in OVERHEARD_LINES
    ]
    return render_template('home.html', overheard=overheard)

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=MENU_ITEMS, category_notes=CATEGORY_NOTES)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Validation
        errors = {}
        if not name:
            errors['name'] = 'Name is required'
        if not email:
            errors['email'] = 'Email is required'
        elif '@' not in email or '.' not in email.split('@')[-1]:
            errors['email'] = 'Please enter a valid email address'
        if not message:
            errors['message'] = 'Message is required'
        elif len(message) < 10:
            errors['message'] = 'Message must be at least 10 characters long'

        if not errors:
            # Send email
            try:
                safe_name = name.replace('\r', '').replace('\n', '')
                body = (
                    f'New contact form submission:\n\n'
                    f'Name: {name}\n'
                    f'Email: {email}\n'
                    f'Message: {message}\n'
                )
                msg = Message(
                    subject=f'New contact form submission from {safe_name}',
                    recipients=[os.getenv('CONTACT_RECIPIENT', 'admin@dailyhaven.com')],
                    reply_to=email,
                    body=body
                )
                mail.send(msg)
                flash("Thank you for your message! We'll get back to you soon.", 'success')
                return redirect(url_for('contact'))
            except Exception as e:
                # In production, you'd want to log this error
                flash('Sorry, there was an error sending your message. Please try again.', 'error')
                return render_template('contact.html', errors=errors, name=name, email=email, message=message)
        else:
            # Validation failed
            return render_template('contact.html', errors=errors, name=name, email=email, message=message)

    # GET request
    return render_template('contact.html', errors={})

if __name__ == '__main__':
    app.run(debug=True)
