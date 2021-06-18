# Courses Application

This project is created in order to understand simple REST API by using Django and Django Rest Framework. 

## Installation

Below instructions will get you a copy of the project up. (Commands are written for Mac.)

After downloading the repository, set up virtual environment and activate it in your directory:

```bash
python3 -m venv venv # set up virtual environment
source venv/bin/activate # activate virtual environment
```

Now when you're inside the virtual environment, install package requirements:

```bash
pip install -r requirements.txt
```

Requirements

```bash
django==3.2.3
djangorestframework==3.12.4
psycopg2-binary==2.8.6
python-decouple==3.4
dj-database-url==0.5.0
whitenoise==5.2.0
gunicorn
```

## Getting started

Now run server (localhost).

```bash
python manage.py runserver
```
Homepage (list of all courses): http://127.0.0.1:8000/courses/ 

Detail view of course: http://127.0.0.1:8000/courses/{course_id}

## Documentation

Courses Application's API: https://courses27.docs.apiary.io/#

APIs for:

Course List: https://courses27.docs.apiary.io/#reference/0/courses-collection/list-of-all-courses

Course Detail: https://courses27.docs.apiary.io/#reference/0/one-course-info/view-of-a-course-detail

## Deployment

Deployed to Heroku

List of all courses: courses/ https://neobiscoursesapp.herokuapp.com/courses/

Detail view of course: courses/{course_id} https://neobiscoursesapp.herokuapp.com/courses/1/
