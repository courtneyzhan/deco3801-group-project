# Console
python manage.py shell

User.objects.filter(username='courtney')
User.objects.get(id=1)
Posts.objects.all()
post = Posts.objects.first()
post.content

Get all posts from one user
user.post_set
<!--itemname.modelname_set -->

Ways to save objects created 
post_1 = Post(title="Diary 1", content="My first diary", author=user)
post_1.save
post_2 = Post(title="Diary 2", content="Second diary entry", author_id=user.id)
post_2.save
user.post_set.create(title='Diary 3', content='Diary content 3')

## Installation
Make sure Django is installed
`pip3 install django`
`django-admin --version`
>> 3.2.5

## Running Locally
cd django/together/
python3 manage.py runserver 8080
>> localhost:8080 in browser (default port 8000)


## Create app
python3 manage.py startapp diary

## Routing the app
Within app folder, import HttpResponse from django.http and create a function in views
`def function(request):
    return HttpResponse(CONTENT)`

create a urls.py and add following information
`from django.urls import path
from . import views

urlpatterns = [
    path('', views.FUNCTION, name='appname-identifier'),
]`

Then in the project urls.py, insert
`path('appname/', include('appname.urls')),`
to include is as localhost:8080/appname/

## Setting the app up
in appname > apps.py, should have a Config name (e.g. AppConfig). Copy into project > settings.py under INSTALLED_APPS as "appname.apps.AppConfig"

## Returning HTTP Content (Nicely)
Use templating.
appname > template > appname

## Returning HTML Pages (Nicely)
Use a main CSS
appname > static > appname

## Database Migration
  python3 manage.py makemigrations
    Prepares to update hte database
  python3 manage.py migrate
    Apply chnages to database

## Creating an Admin User
Database Migration must happen first!!
  python3 manage.py createsuperuser
courtney
test01 (testing purposes)