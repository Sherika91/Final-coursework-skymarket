# Final Course WorkBackend-Part
## Installation
Before you start, make sure you have Python 3.7^ and pip installed on your system.
```
python --version
pip --version
```
If you don't have them, you can download them from [here](https://www.python.org/downloads/).

## Setup
### Clone the repository and navigate to the project directory.

```sh
git clone <project_url>
cd <skymakret>
```

### Create a virtual environment and activate it.
```sh
python -m venv venv
source venv/bin/activate
```

### Install requirements
```sh
pip install -r requirements.txt
```
### Set up your .env variables using .env.example file
```sh
cp .env.example .env
```
### Set up your database
Make sure you have postgres installed on your system and running.   
If you don't have it, you can download it from [here](https://www.postgresql.org/download/).
```sh
psql -U postgres
CREATE DATABASE <your_database_name>;
CREATE USER <your_user_name> WITH PASSWORD '<your_password>';
GRANT ALL PRIVILEGES ON DATABASE <your_database_name> TO <your_user_name>;
```
### Apply migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
### Run the server
```sh
python manage.py runserver
```
