# Arken AI - Medical Report Generation Platform
###

<div align="center">
<img style="width:70%" src="https://github.com/mahmoud0alabsi/mahmoud0alabsi/blob/main/assets/logo/arkenai.png?raw=true"/>
</div>

###
An AI-powered web platform that automates the generation of medical reports from doctor-patient interactions. The system begins by transcribing audio conversations using speech-to-text processing, then preprocesses the transcript. The refined text is passed to the OpenAI API, which generates structured, human-readable medical reports. Built with Django for backend logic and API integration, JavaScript for dynamic frontend interaction, and deployed on Google Cloud for scalability and performance.

## Features

- AI-Powered Medical Report Generation
- Speech-to-Text Processing
- Automated Clinic Letter Generation
- User Authentication System
- Voice Recording and Processing
- Booking Demo System
- User Profile Management
- Admin Dashboard
- Contact Form with Email Integration

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)
- OpenAI API Key (from your Azure instance)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mahmoud0alabsi/ArkenAI-Medical-Report-Generation-Platform.git
cd ArkenAI-Medical-Report-Generation-Platform
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up the database (if needed):
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Configure environment variables:
Create a `.env` file inside the `app/` directory and add:
```
OPENAI_API_KEY=your_openai_api_key_from_azure
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
```

> **Note:** The medical report generation tool will not work unless you provide a valid OpenAI API token (from your Azure instance) in `app/.env`.

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application:
- Main site: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/secure/panel/auth/

## Default User Account

A default user account is already provided for login and admin access:
- Email: admin@example.com
- Password: admin123

You do not need to create a new user.

## Project Structure

```
website_code/
├── app/
│   ├── __pycache__/
│   ├── forms/
│   ├── migrations/
│   ├── models/
│   ├── static/
│   ├── templates/
│   ├── views/
│   ├── __init__.py
│   ├── .env
│   ├── admin.py
│   ├── ai_code.py
│   ├── apps.py
│   ├── const.py
│   ├── decorators.py
│   └── urls.py
├── base_templates/
├── django_logs/
├── media/
├── sourceCode/
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## Key Features

1. **AI-Powered Medical Report Generation**
   - Speech-to-text processing of doctor-patient conversations
   - OpenAI API integration for intelligent report generation
   - Structured, human-readable medical reports
   - Automated clinic letter generation

2. **User Authentication**
   - Custom user model with email-based authentication
   - Password reset functionality

3. **Voice Recording**
   - Record and save voice messages
   - Process voice recordings
   - View recording history

4. **Booking Demo System**
   - Contact form for demo requests
   - Email notifications for new requests
   - Admin interface for managing requests

5. **User Profile**
   - Edit personal information
   - View recording history
   - Manage account settings

## Security Notes

- The application uses Django's built-in security features
- CSRF protection is enabled
- Password hashing is implemented
- Admin panel is secured with custom URL
- Secure handling of medical data

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request


## Contact

For issues or questions, open a GitHub issue or contact:
- 📧 Email: [malabsi034@gmail.com](mailto:malabsi034@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/mahmoud-alabsi](https://www.linkedin.com/in/mahmoud-alabsi)
- 💻 GitHub: [github.com/mahmoud0alabsi](https://github.com/mahmoud0alabsi)