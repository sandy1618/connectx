# ConnectX
## Steps to connect django project . 

Create a django project . 

Create a django App. 

- Whenever you make an app, register in settings.py , INSTALLED_APPS  LIST. 

Create urls to map urls in the project, urls.py files. this is the mail file. 

In the app folder, use the views and create function to receive request and give response. 

Use template engine , DTL for creating HTMl template. Make a template folder and register its path in the settings, tempalte list. This will register tempalate path. 
This tempalte can then be used in the return statement of the views.py functions. ( we use render object to give httpResonse object of the html file.)

Then in the models, create model class. 

then use 
python manage.py migrate 
python manage.py makemigrations first_app
    this will look for models.py in first app and then apply the models to the db. 
python manage.py migrate 

To show in the django admin, 
you need to register the models in first_app in the first_app.admin.py file.

```python
        # Register your models here.
        from .models import Topic,Webpage,AccessRecord
        # Register your models here.
        admin.site.register(Topic)
        admin.site.register(Webpage)
        admin.site.register(AccessRecord)
```


### MTV : MODEL TEMPLATE VIEW WORKFLOW
- django-admin startproject basicforms

- django-admin startapp basicapp

- create templates folder in root directory 
    - register path of template in TEMPLATE_DIR in settings.py
- create static folder in root directory 
    - register path of static in STATIC_DIR  in settings.py

### Create a form in forms.py in app folder. 
- render the view of the form in views.py file in app folder. 
    - view here will take form object and pass it to html to render the htmlResponse object. Here the HTML is in template folder. 

- Do proper URL Mapping to connect this view . Can use include or its okay, can directly use the urls.py file. 

- Saving the forms into the view



### Setting username and password for django admin. 

- python manage.py createsuperuser



