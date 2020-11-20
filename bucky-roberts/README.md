# Bucky Roberts

i'll will be following bucky robert's Django tutorial playlist here. 
so follow along with me :)
if i see anything interesting i'll also write it here so you (future me) won't 
have any problems in understanding all these things later.




### 1 install setup

Bucky is using django 1.9.1 for teaching and the latest here is 3.1.3
so i don't know what to do here maybe i'll go with my version but i hope all 
these coming tuts will go well.




### create an app

to create an app:
```shell script
$ python3 manage.py startapp <app-name>
```

after creating the app. 
configure it with main app (urls.py and settings.py)
after that being done, work on models.py to use database on that app.

now it's time to sync our app with database. (migrations)

```shell script
$ python3 manage.py makemigrations <app-name>
$ python3 manage.py migrate
```

then run the local server and check if everything is working correctly.

```shell script
$ python3 manage.py runserver
```



## let's move 

suppose we have added some querySets (data) to the database.
now we want to use it 
and most probably will render it on html page to display data.
HTML page means Templates. 
let's see how do we do that!!!


```text
there are two thing we have to configure now:
1. <app-name>/urls.py
2. <app-name>/views.py
```




### urls.py

inside urls.py, 
first we have to configure url for first time which is when
user visits the application (index page) to do that.
this is called URL MAPPING

```python
form . import views     # to use functions from views.py file

urlpatterns = [
        path(r'', views.index, name='index'),
]
```

Now we have handled base URL, let's move to next URL
which will be detailed section.

```text
philosophy:

Configuring base URL by mapping it to a index.html file (that we'll do later)
 means in this page we will display data models that we will create. 

But what if we want a detailed page about each data model that we display on 
this page, so for that reason we will configure another URL.
```

so for example, by choosing a data field for index page we'll get primary key (PK) of data. 
and then, PK will be returned to server with request (in URL, GET request probably)
and in response, server will give us new page about that  will render data on specific
data field.

```python
urlpatterns += [
        path(r'<int:primary_key>/', views.detail, name=["detail"])
]
```

REMEMBER: we are just mapping these requests/URL to the functions in views.py file.

So, now we actually have to create so function to handle those request and that we'll 
do in view.py file.

### views.py

now as we see there are two function that were mapped from views.py file in the urls.py 
file. now it's time to actually create those functions.

```python
# from models.py, import models 
from .models import data_model
# function that will handle base URL request
def index(request):
    # select all data models from database.
    all_data = data_model.objects.all()
    # now choose template in which you have to render data.
    template = loader.get_template('<app-name>/index.html')
    # context is the data that will be passed on to template file
    # context is a dictionary BTW
    context = {
        "data": all_data
    }
    # send back response with data to be rendered and file in which data will be rendered
    return HttpResponse(template.render(context, request))
``` 

this function will send index.html page whenever requested.
this html page is actually just a template which will show the 
data that is sent with it as it's context.

Here's one more example function from my project.

```python
def detail(request, album_id):
        album = Album.objects.get(pk=album_id)
        print(album.album_title)
        template = loader.get_template('music/detail.html')
        context = {
                "albumObj": album,
        }
        return HttpResponse(template.render(context, request))
```





## template

template is just a file in which our data will render.
location of file is important.
for example, if you're creating a template for <app-name>
which is an application inside main project.
so template file will be at folder:

```text
<project-name> -> <app-name> -> templates -> <app-name> -> [HTML FILE]
```

#### EXAMPLE: 

```html
<html>
    <h1>MUSIC</h1>
        {% if all_albums %}
            <ul>
                {% for album in all_albums %}
                <li><a href="{% url 'detail' album.id %}">{{ album.album_title }}</a></li>
                {% endfor %}
            </ul>
        {% else %}
            <h3>You don't have any albums yet.</h3>
        {% endif %}
</html>
```



### shortcut: template rendering 

so untill now we were using sending back the HTTP Response to the browser using:

```python
from django.http import HttpResponse
return HttpResponse(template.render(context, request))
```

but before sending we also had to locate template and this is just an extra step.

So we well do is, we just use different function that will do both work in single line.

```python
# importing the function
from django.shortcuts import render
# using method to return response
return render(request, '<app-name>/[file-name].ext', context)
```

this wil do just the same thing!
and we won't have to locate template using extra method.



## 404

so if we request a page but it don't exists, then we'll get a 404 "do not exists" error.
But if we don't handle a situations like that, then we'll get 500 "server" error.

we don't want server error, because it tells about server also.
so we can do is if we hit a 404 type situation then we have to throw 
a 404 page by ourselves.

```python
# import function to throw 404 in response
from django.http import Http404
from .models import dataModel
from django.shortcuts import render
# use that Http404 method with views.py URL/request-handling functions
def index(request, dataId):
    try:
        all_data = dataModel.objects.get(pk=dataId)
    expect dataModel.doesNotExist:
        raise Http404('Data does not exists!')
    return render(request, '<app-name>/[FILE-NAME]', {"all_data": all_data})
```

### shortcut: raise 404

return object, if not available in database then returns 404.

```python
from django.shortcuts import get_object_or_404

data = get_object_or_404(Model, pk=3)
```



## create super user (ADMIN)

It's very simple to create super user, just use the command:

```shell script
$ python3 manage.py createsuperuser
```

using Admin account, one can create update, delete and view models.
And admin can create new users and groups also.

after creating Admin.
visit:

```text
https://localhost:8000/admin
```


## Add models to admin panel

Sorry i forgot about that, but it's pretty easy. just go to <app-name> directory
look for admin.py and open up the file. In that file, you have to do following:

1. import models from models.py
2. register them under admin application.

```python
# admin.py

# import admin
from django.contrib import admin
# import models from models.py
from .models import Album, song

admin.site.register(Album)      # register album model
admin.site.register(song)       # register song model
```

## access and add data to the database

there are two ways to add data into database:

1. i'll be explaining how to add data by taking an example: add song to an album, where song and
album both are models. 

```shell script
# first open the python special shell
$ python3 manage.py shell
# import models from database
$ from music.models import Album, song
# now select a Album in which you want to add song.
$ album1 = Album.objects.get(id=1)
# create a song object
$ song = song()
# add attributes of song class (like name, file-type, album, artist etc...)
$ song.song_title = "venom"
$ song.file_type = "mp3"
$ song.album = album1     # here i've linked album1 to this song, means this song is also added to album1
$ song.save()   # after completing the changes just call save() to save changes to actual database.
```

2. another method will be shorter

```shell script
# first open the python special shell
$ python3 manage.py shell
# import models from database
$ from <app-name>.models import Album, song
# now select a Album in which you want to add song.
$ album1 = Album.objects.get(id=1)
# using album object, we can do couple of things:
$ album1.song_set.all()     # return all songs in the album
$ album1.song_set.count()   # return number of songs does this album have
# now to create new song, we can do this.
$ album1.song_set.create(song_title="godzilla", file_type="mp3")
# here we don't have to explicitly pass the name of album, because it's already in the beginning.
```




## writing proper URL (NO HARDCODING PATHS)

so until now we were writing URLs like this:

```html
<a href='/music/' + {{ object.id }}>visit music file</a>
```

But in this above reference, half path is hardcoded. and if we later change
the paths then we'll have to change paths in each file.

now we'll do some changes:

1. urls.py file

```python
datapattern += [ path(r'<int:id>/', views.function, name=['url-name']) ]
```

2. HTML template

```html
<a href="{% url "url-name" object.id %}">visit detailed file</a>
```

### namespacing

so we use this new URL to make requests, it'll look for URL with url-name in views.py
But what if we had more than one applications in our app with url-name in their views.py while
URL mapping. 

to resolve that problem, i introduce you to **namespacing** 

to implement this, follow along:

1. urls.py

```python
# to identify which application
app_name = '<app-name>'
```

2. HTML template

```html
<a href="{% url "app-name:url-name" object.id %}">visit detailed file</a>
```

so before writing url name it suppose to visit.
just add <app-name> to which URL belongs.




## HTML forms

first we will setup HTML template.

```html
<form action="{% url 'music:favourite' albumObj.pk %}", method="post">
    {% csrf_token %}
    {% for song in albumObj.song_set.all %}
        <div id="song">
            <input type="radio" id="song{{ forloop.counter }}" name="song" value="{{ song.pk }}" required>
            <label for="song{{ forloop.counter }}">
                <p>{{ song }}</p>
                    {% if song.is_fav %}
                    <img id="fav" src="https://img.icons8.com/plasticine/100/000000/star--v1.png"/>
                    {% endif %}
            </label>
        </div>
    {% endfor %}
    <input id="submit" type="submit" value="favourite">
</form>
```

>   here we have to look do work inside form tags.
>   form's attribute **action** will be **{% url 'music:favourite' albumObj.pk %}**
>   when we'll submit the form, it will redirect up to this URL.

>   there are different types of inputs inside tag, make sure to add **name** attribute to the input tags.
>   Because you can only access the inputted data through their name on server side.

let's move to **urls.py**

```python
urlpatterns += [
        path(r'album=<int:album_id>/favourite/', views.favourite, name='favourite')
]
```

>   here we just added a handling for URL that will be generated after submitting form.
>   we mapped the request to **favourite method** inside the **views.py** file.

now check out **views.py** method

```python
def favourite(request, album_id):
        album = get_object_or_404(Album, pk=album_id)
        try:
                selected_song = album.song_set.get(pk=request.POST['song'])
        except (KeyError, song.doesNotExist):
                return render(request, 'music/detail.html', {
                        'album': album,
                        'error_message': 'you did not select a valid song!'
                })
        else:
                selected_song.is_fav = not selected_song.is_fav
                selected_song.save()
        return render(request, 'music/detail.html', {"albumObj": album})
```

>   this method may seems bit tricky but it's actually easy! Let's see. 
>   First of all, about **album** variable it's just an optional argument required in that particular example
>   you can ignore it.

>   in **try** statement, i'm trying to access the song whose id is given if id is invalid. 
>   then, **except** will come into play. It will send back the response with  with error_message.

>   if everything will go like plan,  then we'll come to **else** block after try block.
>   here is our main logic, here we will do whatever we want with data. (calculations on server side) and after that
>   send back the normal response with album object.


But

There is a problem with this function response. 

>   the response will go back to same URL and if user reloads or press back button. POST request will be sent 
>   again. 
>   We don't want that so we will redirect it to detailed page using a different function.

```python
# to retrace the URL.
from django.urls import reverse
# to redirect response to that page.
from django.http import HttpResponseRedirect
# using this function we can do that!

def function(request, id):
    ...
    return  HttpResponseRedirect(reverse('<app-name>:<url-name>', args=(id,)))
```  

in **HttpResponseRedirect** function, first argument will be name of URL to redirect.
second argument is **args**, in which we'll pass the data to send to new page.


## adding static files to templates

To add some static files that are stored on server.
understand the following steps:

>   first make a directory named **static** inside <app-name> folder.
>   just like that **template** folder.
>
>   now inside that **static** folder, make another folder named same as **<app-name>**
>   
>   that's it. now folders are DONE its time to add some static files and images or whatever
>   you want. You can do that by just making files inside that. 

Now it's time to add those static files with templates.
go to top of template in which you want to add the static files. 
and add this code snippets there:

```html
{% load static %}
<!-- example: to add style.css file to the template -->
<link rel="stylesheet" href="{% static '<app-name>/style.css' %}">
```

with this little code, you have successfully added you first static file to
the template.



## base template

ok, little story time.

>	i want to use navbar to naviagate through my app. but making a navbar is a hasssle. even so, i did it
>	anyway but making one nav bar isn't enough. it should be present in each page because its common for whole
>	application. 

so to create common element we make a BASE TEMPLATE. which can be used as inital template from which we can create other 
templates. 

### how it works:

	i created a html file called *base.html* and work on it as follows:

	>	create a simple HTML file.

	>	use varaibles called *block* to create space which can be filled later using other templates.

	>	syntax for block:

```html
{% block block_name %}
	<code here>
{% endblock %}
``` 

	>	once block is added to some point in base template file.

	>	later we can add actual code there from other HTML files.

	>	we can also create multiple blocks.
		some of common uses are body, title and static.

	>	using *body*, we can add body according to page we want to serve

	>	using *title*, we can add corresponding titles to different pages

	>	using *static*, we can add other static files like css and javascript files.

### add base template to other template

	>	first declare that which template are you using. in other words, add your base template to the file.

```html
{% extends '<app-name>/base.html' %}
```

	>	now you have added base templates.

	>	remember we had create those variables called *block* Lets use/fill them.

	>	it's exactly same, just as we had created block 
		new thing is what we want to add inside it, like the actual code.

```html
{% block name %}
<div>
	hehe code here
</div>
{% endblock %}
```
	
	>	just like this we have added the code to the block now when we seve this file.

	>	it will take code from BASE template and fill its blocks by taking the code from block inside
		this file.

	>	and after that it will render the page for us.

see this way we didn't had to repeat the common code. by creating a base template. Hense _code reusablity_ 




##  Generic Views

>   until now, we have wrote a log of view functions but truth is,
>   functions are not the standard way to work with views.
>   
>   from now on we will use _generic views_
>   generic views are actually more easy than it sounds.




### let's start writing generic views

first we have to do little change in *urls.py* file, we will change
the *URLconf*, it just the middle section of URL pattern with which
we map the request handlers of views.py file


```python
from django.urls import path
from . import views

app_name = 'abc'
urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>', views.DetailView.as_view(), name='detail'),
        path('<int:some_id>', views.something, name='something'),
]
```

>   first thing to notice is that we are no more using parameter names
>   instead, im matching for *primary key* in the URL.
>
>   another thing is, as we will use classes to handle requests. so we are
>   no more using those functions for tasks like sending list of objects or 
>   detailed object.

*urls.py* part is done. Let's move to *views.py*

>   first thing we can do is to delete all old code that from views.
>   after that let's write some code that handles first request, that is
>   index.html request!

```python
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import one, two 
# these are all the things we will need in order to create our now views.py file.

class IndexView(generic.ListView):
    template_name = 'app_name/index.html'
    # template_name is use to locate and serve the template.        
    context_object_name = 'data'
    # object_context_name is the name of variable that we'll use in  our template.
    
    # get_queryset is a function in which we fetch the data from model.
    def get_queryset(self):
        # return all object that model 'one' have.
        return one.objects.all()
```

so request handling is easy now, atleast when we have to serve pages!

But still if we need to perform some functionality, then we'll again 
have to use functions instead.
same goes when we handle form submissions.

>   let's handle request to a page which shows detailed info. about particular object from model

```python
from django.views import generic
# imports will remain same!
class DetailView(generic.DetailView):
    template_name = 'app_name/detail.html'
    model = 'one'
    context_object_name = 'detailed_data'
```

That's it! we don't even need to fetch data from model ourselves.
as we define _model = one_, python will go to database and look for table named 'one'
after that, as we have provided the primary key in urlpatterns in *urls.py*
so python will take the primary key from there and fetch the corresponding row or whatever.

>   that's all we need to know about generic view.

but for revision, one last time im going to write a function which handles the request for 
marking a song as favourite. Basically form submission handling.

```python
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Albums, song

def favourite(request, album_id):
    album = get_object_or_404(Albums, pk=album_id)
    try:
        song = album.song_set.get(request.POST['name'])
    except (KeyError, song.doesNotExist):
        return HttpResponseRedirect(reverse('music:detail', args=({
                'album': album,
                'error_message': 'song does not exists',
        })))
    else:
        song.is_fav = True
    return HttpResponseRedirect(reverse('music:detail', args=(album,)))
```

so as you can see, if we get a request and want to perform some action or calculation instead of 
serving the page, then we need to write functions as usual.
