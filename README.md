# Django
This repository contains Django projects aimed at showcasing various web development techniques.

## About Django
Django is a high-level Python web framework that enables rapid development and clean, pragmatic design.Django is a web framework designed for building secure, scalable web applications. It follows the model-template-views (MTV) architectural pattern and emphasizes reusability, less code, and quick development. With its built-in features like an ORM, authentication, and an admin interface, Django makes it easy to create robust applications quickly.

## Getting Started

## Prerequisites
Ensure you have python and pip installed

## Installation
To install django, open command prompt and run this command: <br>
```bash
python -m pip install django
```
Now django is successfully downloaded.

### Create Project
Run following commands in vs code terminal:
```bash
django-admin startproject projectname
```
This will create Project
### Create App
```bash
python manage.py startapp appname
```
This will create app and all its files.
### Register app
Register your app in settings.py file under 'installed app' secton
### Run project
```bash
python manage.py runserver
```
Follow the link and your admin site is ready

## Run Django Project in VS Code

Download project folder and run following commands to migrate changes and create your superuser.
```bash
python manage.py createsuperuser
```
```bash
python manage.py makemigrations
python manage.py migrate
```



