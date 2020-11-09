# python (for IoT probably)




## django3

	>	to resolve django version conflict, i've installed virtualenvwrapper to work on some specific version of django on specific projects.





### virtualenvwrapper commands:

```shell script
$ mkvirtualenv env_name			(create new enviroment)
$ deactivate					(to deactivate current enviroment)
$ workon						(list of all virtual enviroment)
$ workon env_name				(activate the specific python virtual enviroment)
$ rmvirtualenv env_name			(remove specified enviroment)
```
	->  i've create virtualenv called 'django-iot'
	->  in there, i'm installing django for my upcoming project
	->  to check:	
```shell script
$ python3 -m django --version
```
	>	it means that django is installed inside python virtual enviroment named 'django-iot'. outside of that, there's no django named package


	so now after manny hours, i've resolved the error most probably
	feeling very happy.








### problem:
	->	as django use SQLite as database but i've haven't installed that.
	->	so i tried to install it usingn pip command.
	->	but it doesn't work!!!
	->	i first visit:	[a link](https://pypi.org/project/django-s3-sqlite/)
	->	then i went to github repo  'django-s3-sqlite' :  [a link](https://github.com/FlipperPA/django-s3-sqlite/tree/0.0.3)
	->	there i read this:
```
	Newer versions of Django (v2.1+) require a newer version of SQLite (3.8.3+) than is available on AWS Lambda instances (3.7.17).

	Because of this, you will need to download the file _sqlite3.so (available in the root of this repository) and put it at the root of your Django project.
```
	->	so i installed the file:	[a link](https://github.com/FlipperPA/django-s3-sqlite/blob/0.0.3/_sqlite3.so)
	->	and pasted it into root of django project
	->	and now it worked~! 













### starting first webapp:

	>	im following MDN for this first project.
	>	project will be 'LocalLibrary'
	>	full project:	[a link](https://github.com/mdn/django-locallibrary-tutorial)

	->	setting up basics:
```shell script
$	django-admin startproject <project-name>
```
		>	project skeleton will be like:

			<project-name>/				# root folder
			    manage.py 				# main script to start server
			    <project-name>/			# Website/project
			        __init__.py 		# empty file that treat this directory as Python package.
			        settings.py 		# website settings
			        urls.py 			# site URL-to-view mappings
			        wsgi.py 			# help application communicate with webserver
			        asgi.py 			# asynchronous successor to WSGI

		>	to createt specific application inside project.
```shell script
$	python3 manage.py startapp <app-name>
```
		>	updated project directory should now look like this:
			<project-name>/
			    manage.py
			    <project-name>/
			    <app-name>/			# newly created application
			        admin.py
			        apps.py
			        models.py
			        tests.py
			        views.py
			        __init__.py
			        migrations/		# automatically update database as  modify the models

		>	after creating application, time to register:
		>	go to 'django_projects/<project-name>/<project-name>/settings.py'
		>	add the <app-name> to INSTALLED_APPS list. 
		>	Then add a new line at the end of the list (comma)

		>	example:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app-name>', 
]
```
		>	next step will be setting up database. for that, first resolve issue by adding '_sqlite3.so' file in root of folder (read problem section for details)

		>	then, everything related to database remains same as we are using 'sqlite'. so let's move on!

		>	now setup TIME_ZONE, use this:

```python
			TIME_ZONE = 'Europe/London'
```
		>	setting up URL mapper (urls.py)

		>	so add url to our new app.

		>	in other words, open 'django_projects/<project-name>/<project-name>/urls.py'

		>	 Use include() to add paths from the application 

```python
from django.urls import include

urlpatterns += [
    path('<app-name>/', include('<app-name>.urls')),
]
```
		>	Add URL maps to redirect the base URL to our application

```python
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
```
		>	to use static files like css, js.

		>	Use static() to add url mapping to serve static files during development (only)

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

		>	now save and close this file.

		>	then, create urls.py inside <app-name> folder and add this,

```python
from django.urls import path
from . import views

urlpatterns = [

]
```
		>	finally done with URL mapping!

		>	At this point we have a complete skeleton project










#### Running database migrations
	
	>	Running database migrations
```shell script	
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
	>	'makemigrations' command creates (but does not apply) the migrations for all applications installed in project.

	>	'migrate' command is what applies the migrations to your database.

	>	running the website
```shell script
$ python3 manage.py runserver
```





```
[DAY 2]
```





### models:

```python

from django.db import models

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta: 
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

```



	>	Once you've chosen what database you want to use, you don't need to talk to it directly at all — you just write your model structure and other code, and Django handles all the dirty work of communicating with the database for you.

	>	models contains fields(variales), metadata(classes) and methods(functions.






#### 1. fields:

```python
my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
```

	>	FIELD represents a column of data that we want to store in one of our database tables.

	>	in this example, 'my_field_name' is FIELD and of TYPE 'models.CharField'.

	>	FIELD TYPE determine the type of record that is used to store the data in the database, along with validation criteria to be used when values are received from an HTML form.

	>	FIELD TYPE 'models.CharField' means that this field will contain strings of alphanumeric characters.

	>	FIELD TYPE can also take arguments that further specify how the field is stored or can be used.

		->	'max_length=20'	:	max length of value in the field

		->	'help_text="Enter field documentation"' : works as a place holder

	>	FIELD NAME is use to refer to it in queries and templates.

	>	NOTE:	

		->	when the label is used as a form label through Django frame, the first letter of the label is capitalized. 

			EXAMPLE:	'my_field_name' would be 'My field name'

		->	the order that fields are declared will affect their default order if a model is rendered in a form, thouth this may be overwritten.







##### common field types:

	>	CharField:	short-to-mid sized fixed-length strings.
					'max-length' argument is must!

	>	IntegerField:	integers

	>	DateField & DateTimeField:	date and date/time information.
									
		->	these fields can additional declare the parameters: 
			>	auto_now=True:	set field to the current date every time model is saved.
			>	auto_now_add:	only set the date when the model is first created.
			>	default:	set a default date that can be overridden by the user.

	>	 EmailField:	store and validate the email.

	>	FileField & ImageField:	use to upload files and images respectively.
					These have parameter to define how and where the uploaded files are stored.

	>	AutoField:	special type of 'IntegerField' that automatically increments.
				A primary key of this type is automatically added if not explicitly specify one.

	>	ForeignKey:	use to specify one-to-many relationships to another database model.

	>	ManyToManyField:	use to specify many-to-many relationship.

	>	more:	https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types










##### common field arguments:

	>	help_text:	placeholder for HTML forms

	>	verbose_name:  name for field used in field labels.
				if not specified, Django will be infer the default verbose name from field name.

	>	default:	default value for the field.

	>	null:	if True, store blank values as NULL. default False.
			CharField will instread store empty string.

	>	blank:	allow field to be blank in forms. default False.

	>	choices:	a group of choices for this field.
				if provided, default form element will be 'select box' with these choises instead of standard text field.

	>	primary_key:	if True, set the current field as primary key for model.

	>	for more:	https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-options





#### 2. Metadata:

	>	can declare model-level metadata for Model by declaring class Meta.

```python
class Meta:
	ordering = ['-my_field_name', 'another_field_name']
```

	>	ordering attribute control the default ordering of records returned when query the model type.

	>	ordering will depend on FIELD TYPES.

		->	character fields are sorted alphabetically.

		->	data fields are sorted in chronological order.

	>	prefix the FIELD NAME with minus symbol (-) to reverse the sorting order.

```python
verbose_name = 'BetterName'
```

	>	i don't understand this atleast for now!

	>	more:	https://docs.djangoproject.com/en/2.1/ref/models/options/



#### 3. Methods:

```python
def __str__(self):
	return self.field_name
```
	
	>	in every model you should define the standard Python class method __str__() to return 
	a human-readable string for each object.

```python
def get_absolute_url(self):
	return reverse('model-detail-view', args = [str(self.id)])
```
	
	>	returns a URL for displaying individual model records on the website.
		'self.id' is to grab particular record.



```
with all these done. now we can create, update or delete records, and to run 
queries to get all records or perticular subset of records.
```








### Model Management:


#### Create and modify records:

```python
#create new model using model's constructor
record = MyModelName(my_field_name = 'Instance #1')

#save the object into database
record.save()
```

	>	to create a record we can define an instance of the model and then call save().

	>	if no primary key decared, new record will be given one, with FIELD NAME ID.

```python

# access the model field values
print(record.id)			# return 1
print(record.my_field_name)		# return 'Instance #1'

# modify the fields, then call save()
record.my_field_name = 'New Instance Name'
record.save()

```

	>	can access the fields in this new record using dot syntax and change values.






#### Searching for records

	>	can search for records that matches certain criteria using the model's 'objects' attribute.

```python

all_books = Book.objects.all()

```

	>	get all the records for the model as an iterable object (QuerySet).

```python

wild_books = Book.objects.filter(title__contains='wild')
nunber_wild_books = wild_books.count()

```

	>	filter() method to filter the returned QuerySet

	>	title__contains => 'field_name' + '__' + 'match_type'

		->	title  =  field_name
		->	contains  =  match_type

	>	full list of 'match_type':	https://docs.djangoproject.com/en/2.1/ref/models/querysets/#field-lookups


```python

# Will match on: Fiction, Science fiction, non-fiction etc.
books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')


```

```

Note: You can use underscores (__) to navigate as many levels of relationships 
(ForeignKey/ManyToManyField) as you like. For example, a Book that had different
types, defined using a further "cover" relationship might have a parameter name:
type__cover__name__exact='hard'.

```

	>	more on queries: https://docs.djangoproject.com/en/2.1/topics/db/queries/









