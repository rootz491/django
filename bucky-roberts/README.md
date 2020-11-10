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

## Add data to the database

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

