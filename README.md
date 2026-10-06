# Student Registration System — Django + PostgreSQL

A beginner-friendly CRUD web application built with **Django** and **PostgreSQL**.

এই project-এর মাধ্যমে একজন beginner end-to-end বুঝতে পারবে:

- Django কী
- Django project এবং Django app-এর পার্থক্য
- Request কীভাবে URL → View → Model → Database → Template পর্যন্ত যায়
- PostgreSQL database কীভাবে Django-এর সাথে connect হয়
- Django ORM কীভাবে SQL না লিখেও database-এর সাথে কাজ করে
- Form submit করলে backend কীভাবে data receive করে
- CRUD — Create, Read, Update, Delete কীভাবে implement করা হয়
- Template এবং Static file-এর responsibility কী
- Migration কী এবং কেন প্রয়োজন

---

## 1. Project Overview

এই project একটি simple **Student Registration System**। এখানে user পারে:

1. সব registered student-এর list দেখতে
2. নতুন student add করতে
3. existing student update করতে
4. student delete করতে

Current pages:

| URL | কাজ |
|---|---|
| `/` | Registered student list |
| `/students/create/` | নতুন student register |
| `/students/<id>/update/` | Student update |
| `/students/<id>/delete/` | Student delete confirmation |
| `/admin/` | Django admin panel |

---

# 2. Django কী?

**Django** হলো Python-এর একটি web framework।

Framework মানে web application বানানোর জন্য Django আমাদের অনেক ready-made structure এবং functionality দেয়। যেমন:

- URL routing
- Database access
- HTML template rendering
- Form validation
- Security
- Authentication
- Admin panel
- Session management
- CSRF protection

Django ছাড়া basic Python দিয়ে web application বানাতে গেলে request handling, routing, database connection, validation—অনেক কিছু manually করতে হতো। Django এই কাজগুলো organized structure-এর মধ্যে সহজ করে দেয়।

---

# 3. Django কীভাবে কাজ করে?

Django traditionally **MVT — Model, View, Template** pattern follow করে।

```text
Browser
   |
   | HTTP Request
   v
URL Configuration
   |
   v
View
   |
   +------> Form
   |
   +------> Model
               |
               v
           Database
   |
   v
Template
   |
   v
HTTP Response
   |
   v
Browser
```

## Model

Model database structure define করে।

এই project-এ:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
```

এখান থেকে Django PostgreSQL-এ table তৈরি করতে পারে।

---

## View

View request receive করে এবং application logic execute করে।

Example:

```python
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
```

এখানে View:

1. Database থেকে students নেয়
2. Template-এর কাছে data পাঠায়
3. HTML response return করে

---

## Template

Template হলো dynamic HTML।

Example:

```django
{% for student in students %}
    {{ student.name }}
{% endfor %}
```

Django View থেকে পাওয়া data template-এর মধ্যে render করে browser-এ পাঠায়।

---

# 4. Django Project vs Django App

এই concept beginner-এর জন্য খুব important।

## Project

`studentregistrationform` হলো পুরো Django project-এর configuration layer।

এখানে থাকে:

- main settings
- main URLs
- database configuration
- installed apps
- middleware
- template settings
- static settings

## App

`students` হলো application/module।

এটি student-related business functionality handle করে।

Example:

```text
Project: studentregistrationform

Apps:
    students
    payments        # future example
    courses         # future example
    accounts        # future example
```

একটি Django project-এর মধ্যে multiple app থাকতে পারে।

---

# 5. Current Project Structure

```text
Class-39/
|
├── manage.py
|
├── studentregistrationform/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
|
├── students/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
|
├── templates/
│   ├── student_list.html
│   ├── student_create.html
│   ├── student_update.html
│   └── student_delete.html
|
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── student.js
|
└── venv/
```

> **Note:** বর্তমান backend-based version-এ `static/js/student.js` কোনো template থেকে ব্যবহার হচ্ছে না। এটি earlier frontend-only version-এর leftover file। চাইলে delete করা যায়।

> **Important:** `venv/` সাধারণত Git repository বা shared ZIP-এর মধ্যে রাখা উচিত না। প্রত্যেক developer নিজের machine-এ virtual environment create করবে।

---

# 6. Prerequisites

Machine-এ নিচের tools থাকা প্রয়োজন:

- Python
- pip
- Docker Desktop
- Code editor / IDE
- Browser

Check Python:

```bash
python3 --version
```

Check pip:

```bash
python3 -m pip --version
```

Check Docker:

```bash
docker --version
```

---

# 7. Step 1 — Create Project Directory

```bash
mkdir Class-39
cd Class-39
```

---

# 8. Step 2 — Create Virtual Environment

Virtual environment project-এর Python dependency আলাদা করে রাখে।

এক project-এর Django version অন্য project-কে affect করবে না।

## macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows PowerShell

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Activate হলে terminal-এর শুরুতে সাধারণত দেখা যায়:

```text
(venv)
```

Check:

```bash
which python
```

Windows:

```powershell
where python
```

Path-এর মধ্যে `venv` থাকা উচিত।

---

# 9. Step 3 — Install Django and PostgreSQL Driver

```bash
python -m pip install --upgrade pip
python -m pip install django "psycopg[binary]"
```

Check Django:

```bash
django-admin --version
```

Current project was generated using Django `6.1.1`.

## Why psycopg?

Django Python application এবং PostgreSQL-এর মধ্যে communication করার জন্য PostgreSQL driver দরকার।

```text
Django
   |
   | psycopg
   v
PostgreSQL
```

---

# 10. Step 4 — Run PostgreSQL with Docker Compose

Current ZIP-এ `docker-compose.yml` নেই। Fresh setup-এর সময় project root-এ এটি create করা যায়:

```yaml
services:
  db:
    image: postgres:16
    container_name: django_postgres
    restart: unless-stopped

    environment:
      POSTGRES_DB: django_db
      POSTGRES_USER: django_user
      POSTGRES_PASSWORD: django_password

    ports:
      - "5432:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Start PostgreSQL:

```bash
docker compose up -d
```

Check:

```bash
docker compose ps
```

Expected conceptually:

```text
django_postgres    Up    0.0.0.0:5432->5432/tcp
```

Stop:

```bash
docker compose down
```

Stop and delete database volume:

```bash
docker compose down -v
```

> `down -v` করলে stored database data delete হয়ে যাবে।

---

# 11. Step 5 — Create Django Project

Project root-এর মধ্যে:

```bash
django-admin startproject studentregistrationform .
```

শেষের `.` important।

এটি না দিলে nested directory তৈরি হতে পারে।

Command-এর পরে:

```text
Class-39/
├── manage.py
└── studentregistrationform/
```

---

# 12. `manage.py` — Responsibility

`manage.py` Django-এর command-line entry point।

এই project-এ এটি:

```python
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'studentregistrationform.settings'
)
```

এর মাধ্যমে Django-কে বলে কোন settings file ব্যবহার করতে হবে।

Common commands:

```bash
python manage.py runserver
python manage.py startapp students
python manage.py makemigrations
python manage.py migrate
python manage.py shell
python manage.py createsuperuser
```

Simpleভাবে:

```text
manage.py = Django project control করার command-line tool
```

---

# 13. Step 6 — Configure PostgreSQL

File:

```text
studentregistrationform/settings.py
```

Current database configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "django_user",
        "PASSWORD": "django_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Meaning:

| Setting | Meaning |
|---|---|
| `ENGINE` | কোন database backend ব্যবহার হবে |
| `NAME` | Database name |
| `USER` | PostgreSQL username |
| `PASSWORD` | PostgreSQL password |
| `HOST` | Database host |
| `PORT` | PostgreSQL port |

Django local machine-এ এবং PostgreSQL Docker container-এ run করলে:

```text
HOST = localhost
PORT = 5432
```

Connection flow:

```text
Django Application
      |
      | localhost:5432
      v
Docker Port Mapping
      |
      v
PostgreSQL Container
```

---

# 14. Test Database Connection

```bash
python manage.py shell -c "from django.db import connection; connection.ensure_connection(); print('Database connection successful')"
```

Expected:

```text
Database connection successful
```

If psycopg error appears:

```bash
python -m pip install "psycopg[binary]"
```

---

# 15. Step 7 — Configure Templates

Current project root-এ `templates/` directory ব্যবহার করছে।

Therefore `settings.py` contains:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    },
]
```

Meaning:

```text
BASE_DIR/templates
```

folder থেকে Django HTML templates খুঁজবে।

---

# 16. Step 8 — Configure Static Files

CSS, JavaScript, images ইত্যাদি static files।

Current `settings.py`:

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

Therefore:

```text
static/
├── css/
└── js/
```

Template-এর মধ্যে static file load:

```django
{% load static %}
```

CSS:

```django
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

Django file locate করছে কিনা check:

```bash
python manage.py findstatic css/style.css
```

---

# 17. Step 9 — Create `students` App

```bash
python manage.py startapp students
```

এতে Django basic app structure create করবে।

তারপর `settings.py`-এর `INSTALLED_APPS`-এ add করতে হবে:

```python
INSTALLED_APPS = [
    ...
    'students',
]
```

## কেন add করতে হয়?

Django-কে জানাতে হয় যে `students` app এই project-এর অংশ।

এটি না করলে Django app-এর model, migration ইত্যাদি properly discover করবে না।

---

# 18. `students/apps.py` — Responsibility

Current file:

```python
from django.apps import AppConfig


class StudentsConfig(AppConfig):
    name = 'students'
```

এটি Django application configuration define করে।

Beginner stage-এ সাধারণত এই file modify করার প্রয়োজন হয় না।

---

# 19. Step 10 — Create Student Model

File:

```text
students/models.py
```

Current model:

```python
from django.db import models


class Student(models.Model):

    COURSE_CHOICES = [
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Java', 'Java'),
        ('Web Development', 'Web Development'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    course = models.CharField(
        max_length=50,
        choices=COURSE_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

## Model কী করছে?

এই class database table-এর schema define করছে।

Conceptually PostgreSQL table:

```text
students_student
-------------------------------------------------
id
name
email
phone
course
created_at
updated_at
-------------------------------------------------
```

Django automatically `id` primary key add করে।

---

# 20. Important Model Fields

## `CharField`

```python
name = models.CharField(max_length=100)
```

Short text রাখার জন্য।

## `EmailField`

```python
email = models.EmailField(unique=True)
```

Email validation করে এবং `unique=True` এর কারণে একই email দুইবার insert করা যাবে না।

## `choices`

```python
course = models.CharField(
    max_length=50,
    choices=COURSE_CHOICES
)
```

Form-এর মধ্যে dropdown generate করতে সাহায্য করে।

## `auto_now_add`

```python
created_at = models.DateTimeField(auto_now_add=True)
```

Record প্রথম create হওয়ার সময় automatically timestamp দেয়।

## `auto_now`

```python
updated_at = models.DateTimeField(auto_now=True)
```

প্রতিবার record update হলে timestamp change হয়।

---

# 21. Step 11 — Migration

Model change করলেই database automatically change হয় না।

Django migration system ব্যবহার করে database schema manage করে।

First:

```bash
python manage.py makemigrations
```

এটি migration file generate করে:

```text
students/migrations/0001_initial.py
```

Then:

```bash
python manage.py migrate
```

এটি PostgreSQL-এ actual table create/update করে।

Flow:

```text
models.py
    |
    | makemigrations
    v
Migration File
    |
    | migrate
    v
PostgreSQL Schema
```

---

# 22. `students/migrations/0001_initial.py`

এই file manually সাধারণত edit করা হয় না।

Django generate করেছে।

এখানে `Student` model create করার database instructions রয়েছে।

Current migration-এর মাধ্যমে fields create হয়:

```text
id
name
email
phone
course
created_at
updated_at
```

---

# 23. Django ORM কী?

ORM = **Object Relational Mapper**।

ORM-এর মাধ্যমে Python code দিয়ে database query করা যায়।

Raw SQL:

```sql
SELECT * FROM students_student;
```

Django ORM:

```python
Student.objects.all()
```

Raw SQL:

```sql
DELETE FROM students_student WHERE id = 1;
```

Django:

```python
student.delete()
```

এটাই Django-এর একটি major advantage।

---

# 24. Step 12 — Create ModelForm

File:

```text
students/forms.py
```

Current code:

```python
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'name',
            'email',
            'phone',
            'course',
        ]
```

## ModelForm কী?

ModelForm model-এর field-এর ভিত্তিতে form তৈরি করে।

```text
Student Model
      |
      v
StudentForm
      |
      v
HTML Form Fields
```

Without ModelForm, manually করতে হতো:

- request.POST থেকে value নেওয়া
- validation লেখা
- Student object create করা
- field errors manage করা

ModelForm এগুলো অনেক সহজ করে দেয়।

---

# 25. Widgets

Current form custom placeholder ব্যবহার করছে:

```python
'name': forms.TextInput(
    attrs={
        'placeholder': 'Enter full name'
    }
)
```

Widget মূলত HTML input element কীভাবে render হবে সেটা control করে।

---

# 26. Step 13 — Views

File:

```text
students/views.py
```

এই file CRUD-এর business/request handling logic রাখে।

Current project-এ চারটি view আছে:

```text
student_list()
student_create()
student_update()
student_delete()
```

---

# 27. READ — Student List

```python
def student_list(request):

    students = Student.objects.all().order_by('-id')

    return render(
        request,
        'student_list.html',
        {
            'students': students
        }
    )
```

Step-by-step:

1. Browser `/` request করে
2. Django `student_list` view call করে
3. `Student.objects.all()` database query করে
4. সব student পাওয়া যায়
5. `students` variable template-এ পাঠানো হয়
6. `student_list.html` HTML generate করে
7. Browser response পায়

```text
GET /
  |
  v
student_list()
  |
  v
Student.objects.all()
  |
  v
PostgreSQL
  |
  v
student_list.html
  |
  v
Browser
```

---

# 28. CREATE — Add Student

```python
def student_create(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student-list')

    else:
        form = StudentForm()

    return render(
        request,
        'student_create.html',
        {'form': form}
    )
```

এখানে দুই ধরনের request handle হচ্ছে।

## GET request

User page open করে:

```text
GET /students/create/
```

Django empty form তৈরি করে:

```python
form = StudentForm()
```

তারপর HTML render করে।

## POST request

User form submit করলে:

```text
POST /students/create/
```

Django submitted data নেয়:

```python
form = StudentForm(request.POST)
```

Validation:

```python
form.is_valid()
```

Save:

```python
form.save()
```

তারপর list page-এ redirect:

```python
return redirect('student-list')
```

---

# 29. UPDATE — Existing Student

```python
student = get_object_or_404(
    Student,
    id=student_id
)
```

এটি given ID-এর student খুঁজে।

না পেলে Django automatically HTTP `404` response দেয়।

GET request-এর সময়:

```python
form = StudentForm(instance=student)
```

`instance=student` থাকার কারণে existing student data form-এ pre-fill হয়।

POST request-এর সময়:

```python
form = StudentForm(
    request.POST,
    instance=student
)
```

এখানে `instance=student` খুব important।

এটি Django-কে বলে:

```text
নতুন row create করো না,
এই existing row update করো।
```

---

# 30. DELETE — Student Delete

View প্রথমে student খুঁজে:

```python
student = get_object_or_404(
    Student,
    id=student_id
)
```

GET request হলে confirmation page দেখায়।

POST হলে:

```python
student.delete()
```

তারপর list page:

```python
return redirect('student-list')
```

Delete-এর জন্য POST ব্যবহার করা safer কারণ GET request ideally data change করা উচিত না।

---

# 31. Step 14 — App URL Configuration

File:

```text
students/urls.py
```

Current routes:

```python
urlpatterns = [

    path(
        '',
        views.student_list,
        name='student-list'
    ),

    path(
        'students/create/',
        views.student_create,
        name='student-create'
    ),

    path(
        'students/<int:student_id>/update/',
        views.student_update,
        name='student-update'
    ),

    path(
        'students/<int:student_id>/delete/',
        views.student_delete,
        name='student-delete'
    ),
]
```

URL-এর কাজ হলো incoming request কোন view handle করবে সেটা decide করা।

Example:

```text
/students/5/update/
          |
          v
student_id = 5
          |
          v
student_update(request, student_id=5)
```

---

# 32. Main Project URLs

File:

```text
studentregistrationform/urls.py
```

Current code:

```python
urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('students.urls')
    ),
]
```

Main project URL অন্য app-এর URL include করে।

Flow:

```text
Browser Request
      |
      v
studentregistrationform/urls.py
      |
      v
students/urls.py
      |
      v
students/views.py
```

---

# 33. Step 15 — Templates

Current templates:

```text
templates/
├── student_list.html
├── student_create.html
├── student_update.html
└── student_delete.html
```

প্রতিটি CRUD operation আলাদা page-এ রাখা হয়েছে যাতে beginner সহজে flow বুঝতে পারে।

---

# 34. `student_list.html`

Responsibility:

- সব registered student দেখানো
- total student count দেখানো
- Add Student link
- Update link
- Delete link

Template loop:

```django
{% for student in students %}
```

Data output:

```django
{{ student.name }}
{{ student.email }}
{{ student.phone }}
{{ student.course }}
```

Update URL:

```django
{% url 'student-update' student.id %}
```

Delete URL:

```django
{% url 'student-delete' student.id %}
```

---

# 35. `student_create.html`

Responsibility:

- নতুন student input নেওয়া
- POST request submit করা
- validation errors show করা

Important:

```html
<form method="POST">
```

এবং:

```django
{% csrf_token %}
```

Fields:

```django
{{ form.name }}
{{ form.email }}
{{ form.phone }}
{{ form.course }}
```

---

# 36. CSRF Token কী?

CSRF = **Cross-Site Request Forgery**।

Django POST form protect করার জন্য CSRF token ব্যবহার করে।

Template:

```django
{% csrf_token %}
```

Django middleware submitted token verify করে।

CSRF token না দিলে POST request সাধারণত `403 Forbidden` হতে পারে।

---

# 37. `student_update.html`

Responsibility:

- existing student-এর data show করা
- user changes নেওয়া
- POST request-এর মাধ্যমে update করা

View form-এ student instance পাঠায়:

```python
StudentForm(instance=student)
```

তাই template-এর একই form field existing data নিয়ে render হয়।

---

# 38. `student_delete.html`

Responsibility:

- delete-এর আগে confirmation দেখানো
- student information দেখানো
- POST request দিয়ে actual delete করা

এটি accidental deletion-এর chance কমায়।

---

# 39. `static/css/style.css`

Responsibility:

- page layout
- forms
- buttons
- tables
- responsive styling
- delete confirmation UI

CSS business logic handle করে না।

Simple separation:

```text
HTML = Structure
CSS  = Presentation / Design
Django View = Request / Application Logic
Model = Database Structure and Data Access
```

---

# 40. `static/js/student.js`

Current project-এর HTML templates এই file load করছে না।

এটি previous frontend-only implementation-এর file যেখানে JavaScript array-এর মধ্যে students রাখা হতো।

বর্তমানে data PostgreSQL-এ save হচ্ছে, তাই এই file প্রয়োজন নেই।

Safe cleanup:

```bash
rm static/js/student.js
```

Windows-এ manually delete করা যায়।

---

# 41. `students/admin.py`

Current file empty:

```python
from django.contrib import admin
```

Future-এ Student model Django Admin-এ manage করতে চাইলে:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

Then create admin user:

```bash
python manage.py createsuperuser
```

Open:

```text
http://127.0.0.1:8000/admin/
```

---

# 42. `students/tests.py`

Automated tests এখানে লেখা যায়।

Example future test areas:

- student creation
- duplicate email validation
- update
- delete
- URL status codes
- view rendering

Current project-এ tests এখনও implement করা হয়নি।

---

# 43. `__init__.py`

Python-কে directory-টিকে package হিসেবে recognize করতে সাহায্য করে।

Beginner project-এ সাধারণত এই file empty থাকে।

---

# 44. `wsgi.py`

WSGI = **Web Server Gateway Interface**।

Traditional synchronous Python web server/deployment-এর জন্য Django entry point।

Production example:

```text
Nginx
  |
Gunicorn
  |
WSGI
  |
Django
```

Local beginner development-এ সাধারণত এই file edit করার প্রয়োজন নেই।

---

# 45. `asgi.py`

ASGI = **Asynchronous Server Gateway Interface**।

Async-capable application server-এর entry point।

Useful for scenarios such as:

- WebSocket
- asynchronous connections
- real-time features

এই project-এ এটিও manually modify করা হয়নি।

---

# 46. `settings.py` — Full Responsibility

`settings.py` পুরো Django project-এর configuration file।

Current project-এ important sections:

## Installed Apps

```python
INSTALLED_APPS = [
    ...
    'students'
]
```

## Middleware

Request/response processing-এর shared layers।

Examples:

```text
Security
Session
CSRF
Authentication
Messages
```

## Templates

```python
'DIRS': [BASE_DIR / 'templates']
```

## Database

PostgreSQL connection settings।

## Static Files

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

## DEBUG

Current development setting:

```python
DEBUG = True
```

Production-এ `DEBUG=True` রাখা উচিত না।

---

# 47. Complete CREATE Request Flow

ধরো user Add Student page-এ গেল।

```text
1. Browser
   GET /students/create/

2. Main URL
   studentregistrationform/urls.py

3. App URL
   students/urls.py

4. View
   student_create(request)

5. Form
   StudentForm()

6. Template
   student_create.html

7. Browser
   Empty form দেখায়
```

User form submit করল:

```text
1. Browser
   POST /students/create/

2. URL
   student_create view

3. StudentForm(request.POST)

4. form.is_valid()

5. form.save()

6. Student Model

7. Django ORM

8. PostgreSQL INSERT

9. redirect('student-list')

10. Browser GET /
```

---

# 48. Complete READ Request Flow

```text
Browser
   |
   | GET /
   v
Main URLs
   |
   v
students.urls
   |
   v
student_list()
   |
   v
Student.objects.all().order_by('-id')
   |
   v
PostgreSQL SELECT
   |
   v
students QuerySet
   |
   v
student_list.html
   |
   v
Browser Table
```

---

# 49. Complete UPDATE Request Flow

```text
Click Update
    |
    v
GET /students/1/update/
    |
    v
student_update()
    |
    v
get_object_or_404(Student, id=1)
    |
    v
StudentForm(instance=student)
    |
    v
student_update.html
```

After submit:

```text
POST /students/1/update/
    |
    v
StudentForm(request.POST, instance=student)
    |
    v
form.is_valid()
    |
    v
form.save()
    |
    v
PostgreSQL UPDATE
    |
    v
redirect to student list
```

---

# 50. Complete DELETE Request Flow

```text
Click Delete
    |
    v
GET /students/1/delete/
    |
    v
student_delete()
    |
    v
student_delete.html
    |
    v
Confirmation Page
```

Confirm:

```text
POST /students/1/delete/
    |
    v
student.delete()
    |
    v
PostgreSQL DELETE
    |
    v
redirect to student list
```

---

# 51. CRUD Mapping

| CRUD | HTTP / Page | Django Function | ORM Operation |
|---|---|---|---|
| Create | `POST /students/create/` | `student_create()` | `form.save()` |
| Read | `GET /` | `student_list()` | `Student.objects.all()` |
| Update | `POST /students/<id>/update/` | `student_update()` | `form.save()` |
| Delete | `POST /students/<id>/delete/` | `student_delete()` | `student.delete()` |

---

# 52. Django Template Syntax

## Variable

```django
{{ student.name }}
```

## For Loop

```django
{% for student in students %}
    {{ student.name }}
{% endfor %}
```

## Empty Case

```django
{% empty %}
    No students registered yet.
```

## URL by name

```django
{% url 'student-create' %}
```

## Static File

```django
{% static 'css/style.css' %}
```

---

# 53. Why URL Names Are Useful

Instead of hardcoding:

```html
<a href="/students/create/">Add</a>
```

Django ব্যবহার করছে:

```django
<a href="{% url 'student-create' %}">Add</a>
```

Benefit:

URL path change হলেও template-এর code manually change করার প্রয়োজন কমে যায়, যতক্ষণ URL name same থাকে।

---

# 54. Why Redirect After Successful POST?

Create বা update হওয়ার পরে:

```python
return redirect('student-list')
```

এটি browser-কে new GET request করতে বলে।

Pattern:

```text
POST
 |
 v
Save Data
 |
 v
Redirect
 |
 v
GET
```

এটি **Post/Redirect/Get** pattern নামে পরিচিত।

Benefit:

Browser refresh করলে same form accidentalভাবে আবার submit হওয়ার possibility কমে।

---

# 55. Run the Project

## 1. Activate environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```powershell
venv\Scripts\Activate.ps1
```

## 2. Start PostgreSQL

```bash
docker compose up -d
```

## 3. Run migrations

```bash
python manage.py migrate
```

## 4. Start Django

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 56. Recommended Fresh Setup Commands

একজন নতুন student project clone/download করার পরে idealভাবে:

```bash
cd Class-39
```

Create venv:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install django "psycopg[binary]"
```

Start PostgreSQL:

```bash
docker compose up -d
```

Migrate:

```bash
python manage.py migrate
```

Run:

```bash
python manage.py runserver
```

---

# 57. Recommended `requirements.txt`

Current ZIP-এ `requirements.txt` নেই। Project share করার জন্য এটি add করা ভালো।

Generate:

```bash
pip freeze > requirements.txt
```

Then অন্য machine-এ:

```bash
pip install -r requirements.txt
```

For a small teaching project, minimal dependency list conceptually:

```text
Django
psycopg[binary]
```

---

# 58. Recommended `.gitignore`

Project root-এ `.gitignore` রাখা ভালো:

```gitignore
venv/
__pycache__/
*.pyc
.idea/
.DS_Store
.env
```

Reason:

- virtual environment commit করা উচিত না
- Python cache files দরকার নেই
- IDE-specific files দরকার নেই
- secrets `.env`-এ থাকলে Git-এ যাওয়া উচিত না

---

# 59. Development Credentials Warning

Current `settings.py`-এ database credentials hardcoded:

```python
"NAME": "django_db"
"USER": "django_user"
"PASSWORD": "django_password"
```

Teaching/local development-এর জন্য acceptable।

Production application-এ password, secret key ইত্যাদি environment variables বা secret manager-এ রাখা উচিত।

Example idea:

```text
.env
DATABASE_NAME=...
DATABASE_USER=...
DATABASE_PASSWORD=...
```

---

# 60. Common Error — CSS 404

Error:

```text
GET /static/css/style.css 404
```

Check:

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

Then:

```bash
python manage.py findstatic css/style.css
```

---

# 61. Common Error — PostgreSQL Connection Refused

Check Docker:

```bash
docker compose ps
```

Check port:

```text
5432:5432
```

Django local machine-এ run করলে:

```python
"HOST": "localhost",
"PORT": "5432",
```

---

# 62. Common Error — psycopg Not Found

Example:

```text
Error loading psycopg2 or psycopg module
```

Install:

```bash
python -m pip install "psycopg[binary]"
```

Make sure virtual environment active।

---

# 63. Common Error — No Table Exists

If model তৈরি করা হয়েছে কিন্তু table নেই:

```bash
python manage.py makemigrations
python manage.py migrate
```

Check migration status:

```bash
python manage.py showmigrations
```

---

# 64. Common Error — CSRF Verification Failed

POST form-এর মধ্যে নিশ্চিত করো:

```django
{% csrf_token %}
```

Example:

```html
<form method="POST">
    {% csrf_token %}
    ...
</form>
```

---

# 65. Common Error — Duplicate Email

Model:

```python
email = models.EmailField(unique=True)
```

তাই একই email দ্বিতীয়বার create করতে গেলে form validation error পাওয়া স্বাভাবিক।

এটি bug না; এটি data integrity rule।

---

# 66. File Responsibility Summary

| File / Folder | Responsibility |
|---|---|
| `manage.py` | Django command-line entry point |
| `studentregistrationform/settings.py` | Project configuration |
| `studentregistrationform/urls.py` | Main/root URL routing |
| `studentregistrationform/wsgi.py` | WSGI deployment entry point |
| `studentregistrationform/asgi.py` | ASGI deployment entry point |
| `students/apps.py` | Students app configuration |
| `students/models.py` | Database model/schema |
| `students/forms.py` | Form generation and validation |
| `students/views.py` | Request handling and CRUD logic |
| `students/urls.py` | Student-related URL routing |
| `students/migrations/` | Database schema history |
| `students/admin.py` | Django admin registration |
| `students/tests.py` | Automated tests |
| `templates/student_list.html` | Student list UI |
| `templates/student_create.html` | Create student UI |
| `templates/student_update.html` | Update student UI |
| `templates/student_delete.html` | Delete confirmation UI |
| `static/css/style.css` | UI styling |
| `static/js/student.js` | Legacy frontend-only JS; currently unused |
| `venv/` | Local Python virtual environment |

---

# 67. Responsibility Separation

একটি beginner-এর জন্য এই mental model useful:

```text
urls.py
    = কোন URL কোন function-এ যাবে?

views.py
    = request এলে কী কাজ হবে?

forms.py
    = input কীভাবে collect + validate হবে?

models.py
    = database data-এর structure কী?

templates/
    = user কী দেখবে?

static/
    = page দেখতে কেমন হবে?

settings.py
    = পুরো project কীভাবে configure হবে?
```

---

# 68. End-to-End Architecture

```text
+----------------------+
|       Browser        |
| HTML Form / Table    |
+----------+-----------+
           |
           | HTTP GET / POST
           v
+----------------------+
|    Django urls.py    |
+----------+-----------+
           |
           v
+----------------------+
|    Django views.py   |
+-----+------------+---+
      |            |
      |            v
      |       StudentForm
      |       forms.py
      |
      v
+----------------------+
|   Student Model      |
|   models.py          |
+----------+-----------+
           |
           | Django ORM
           v
+----------------------+
|     PostgreSQL       |
+----------------------+

Response path:

PostgreSQL
    |
    v
View
    |
    v
Template
    |
    v
HTML Response
    |
    v
Browser
```

---

# 69. What a Beginner Should Learn From This Project

এই project complete করার পরে student-এর ideally clear থাকা উচিত:

- Python virtual environment কী
- pip কী
- Django framework কী
- Django project কী
- Django app কী
- URL routing কী
- HTTP GET এবং POST-এর difference
- View কী
- Model কী
- ORM কী
- Migration কী
- ModelForm কী
- Template কী
- Static file কী
- CSRF token কী
- CRUD কী
- PostgreSQL connection কীভাবে কাজ করে
- Data browser থেকে database পর্যন্ত কীভাবে যায়

---

# 70. Recommended Next Improvements

Current project বুঝে যাওয়ার পরে next steps হতে পারে:

1. Django Admin-এ Student register করা
2. Search functionality
3. Pagination
4. Student detail page
5. Success/error messages
6. Bootstrap/Tailwind styling
7. Authentication/login
8. `.env` configuration
9. Unit tests
10. REST API using Django REST Framework
11. Dockerize Django application itself
12. Django + PostgreSQL full Docker Compose setup

---

# 71. Final Mental Model

সবচেয়ে important flow:

```text
User clicks / submits something
            |
            v
          URL
            |
            v
          View
         /    \
        v      v
      Form    Model
               |
               v
            Database
        
          View
            |
            v
        Template
            |
            v
         Browser
```

যদি এই flow clear থাকে, Django-এর beginner-level foundation অনেকটাই clear হয়ে যাবে।

---

## Quick Start

```bash
# Activate virtual environment
source venv/bin/activate

# Start PostgreSQL
# (requires docker-compose.yml described above)
docker compose up -d

# Apply database migrations
python manage.py migrate

# Start Django
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Project Status

Implemented:

- [x] PostgreSQL connection
- [x] Student model
- [x] Create student
- [x] Student list
- [x] Update student
- [x] Delete student
- [x] ModelForm validation
- [x] Separate CRUD pages
- [x] CSS styling
- [x] CSRF protection

Possible next work:

- [ ] Django Admin registration
- [ ] Search
- [ ] Pagination
- [ ] Authentication
- [ ] Tests
- [ ] Environment variables
- [ ] Dockerize Django app

