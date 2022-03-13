# FreJun_task


## Getting Started 

If you are trying to use this project for the first time, you can get up and running by following these steps. 


## Install and Run

Make sure you have **Python 3.x** installed and **the latest version of pip** *installed* before running these steps.
.

Clone the repository using the following command

```bash
git clone https://github.com/Ajayvardhanreddy/FreJun_task.git
# After cloning, move into the directory having the project files using the change directory command
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
## Create Project

We can now start a Django project within our `FreJun_task` directory. This will create a child directory of the same name to hold the code itself, and will create a management script within the current directory. Make sure to add the dot at the end of the command so that this is set up correctly:
```bash
django-admin startproject FreJun_task .
```
> **NOTE:** Dot (.) at the end of the above command makes the current directory as Project directory.

##  Configure the Django Database Settings


## Migrate the Database
Now that the Django settings are configured, we can migrate our data structures to our database and test out the server.

# apply migrations

python manage.py makemigrations
python manage.py migrate
```

 Create a superuser with the following command:

```bash
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver
```


## Explore admin panel for model data or instances

Open http://127.0.0.1:8000/admin or http://localhost:8000/admin, enter the superuser credentials (only superuser can access /admin page)

## Success:
If everything is good and has been done successfully, your **Django Project** should be hosted on port 8000 i.e http://127.0.0.1:8000/ or http://localhost:8000/ to serve you.




