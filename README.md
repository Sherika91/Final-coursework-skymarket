# coursework_5
# Clone the repository
git clone <repository_url>

# Navigate to the project directory
cd <project_directory>

# Install Python dependencies
pip install -r requirements.txt

# Set up env file
touch .env

# Set up the database
python manage.py makemigrations
python manage.py migrate

# Start the Django server
python manage.py runserver
