from django.shortcuts import render, reverse, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from .models import note
from uuid import uuid4 as uuid
from django.contrib.auth.models import User                     # create user
from django.contrib.auth import authenticate, login, logout     # authenticate user
from django.contrib.auth.decorators import login_required       # ensure user's authenticated
# Create your views here.



@login_required(login_url='note:landing')
def index(request):
        print(request.user.id)
        notes = note.objects.filter(user=request.user)
        context = {'notes': notes}
        template_name = 'notes/view.html'
        return render(request, template_name, context=context)
        # template = loader.get_template('notes/view.html')
        # return HttpResponse(template.render(context, request))


@login_required(login_url='note:landing')
def search(request):
        template_name = 'notes/search.html'

        if request.method == 'GET':
                return render(request, template_name)

        elif request.method == 'POST':
                query = request.POST['search']
                notes = note.objects.filter(title__contains=query, user=request.user)
                # print(notes)
                if notes:
                        context = {
                                'notes': notes
                        }
                        return render(request, template_name, context=context)
                else:
                        context = {
                                'error_message': 'Note not available'
                        }
                        return render(request, template_name, context=context)


@login_required(login_url='note:landing')
def bookmarked(request):
        notes = note.objects.filter(is_bookmarked=True, user=request.user)
        context = {'notes': notes}
        template_name = 'notes/bookmarked.html'
        return render(request, template_name, context=context)



@login_required(login_url='note:landing')
def bookmark(request, id):
        thatNote = get_object_or_404(note, pk=id)
        if thatNote.user != request.user:
                return redirect('note:index')
        # bookmark the note
        # print(thatNote.title)
        thatNote.is_bookmarked = not thatNote.is_bookmarked
        thatNote.save()
        return HttpResponseRedirect(reverse('note:index'))



@login_required(login_url='note:landing')
def create(request):
        template_name = 'notes/create.html'

        if request.method == 'GET':
                return render(request, template_name)

        if request.method == 'POST':
                newNote = note()
                newNote.user = request.user
                newNote.title = request.POST['title']
                newNote.content = request.POST['content']
                newNote.id = key()
                newNote.save()

                # print(newNote.title)
                # print(newNote.content)

                return HttpResponseRedirect(reverse('note:index'))


@login_required(login_url='note:landing')
def edit(request, id):
        template_name = 'notes/edit.html'
        thatNote = get_object_or_404(note, pk=id)
        if thatNote.user != request.user:
                return redirect('note:index')

        elif request.method == 'GET':
                # print(thatNote.title, thatNote.content)
                return render(request, template_name, {'note': thatNote})

        elif request.method == 'POST':
                thatNote.title = request.POST['title']
                thatNote.content = request.POST['content']
                thatNote.save()
                return HttpResponseRedirect(reverse('note:index'))


@login_required(login_url='note:landing')
def delete(request, id):
        if request.method == 'POST':
                thatNote = get_object_or_404(note, pk=id)
                if thatNote.user != request.user:
                        return redirect('note:index')
                thatNote.delete()
                return HttpResponseRedirect(reverse('note:index'))



def landing(request):
        template_name = 'notes/landing.html'
        return render(request, template_name)




def register(request):
        template_name = 'notes/auth.html'

        if request.method == 'GET':
                return render(request, template_name, {'todo': 'Register'})

        elif request.method == 'POST':
                email = request.POST['email']
                username = request.POST['username']
                password = request.POST['password']
                user = User.objects.create_user(username=username, email=email, password=password)
                # user created!
                login(request, user)
                # logging in
                return redirect('note:index')



def loginUser(request):
        template_name = 'notes/auth.html'

        if request.method == 'GET':
                return render(request, template_name, {'todo': 'Login'})

        elif request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                        login(request, user)
                        # logging in
                        return redirect('note:index')

                # if error occurs
                return render(request, template_name, {'todo': 'Login', 'error_message': 'invalid Email or Password'})



def logoutUser(request):
        if request.method == 'GET':
                logout(request)
                return redirect('note:login')





# generate random primary key
def key():
        return uuid().hex