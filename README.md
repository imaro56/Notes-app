# Notes app 
## Running guide

This document provides step-by-step instructions to set up and run the Django project Notes app using a virtual environment.

## Prerequisites

- Python 3.8 or higher installed
- Git installed
- pip (Python package manager) installed

## Setup Instructions

1. **Clone the Repository**

   Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/imaro56/Notes-app.git
   cd Notes-app
   ```

2. **Create a Virtual Environment**

   Create a Python virtual environment to isolate project dependencies:

   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   Activate the virtual environment:

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

   After activation, you should see `(.venv)` in your terminal prompt.

4. **Install Dependencies**

   Install the required packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```
   
5. **Move to project folder**

   ```bash
   cd myproject
   ```

6. **Apply Database Migrations**

   Set up the database by running migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a Superuser (Optional)**

   If your project requires an admin user, create one:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set up the superuser credentials.

8. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000/`.

9. **Access the Admin Interface**

   If you created a superuser, access the admin interface at:

   ```
   http://127.0.0.1:8000/admin/
   ```

## Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment:

```bash
deactivate
```

## Additional Notes

- Always activate the virtual environment (`.venv`) before running any Django commands.

 Keep `requirements.txt` updated when adding new dependencies using 
```bash 
 pip freeze > requirements.txt
 ```