from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
#from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Book

# Create your views here.


def index(request):
    return HttpResponse("Book added :) ")


def detail(request, book_id):
    book =  get_object_or_404(Book, pk= book_id)
    return render(request, 'booklist/detailview.html', { 'Book' : book })



def main_page(request):
    books = Book.objects.order_by('-pub_date')[:10]
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user,'Books' : books })
    output = template.render(variables)
    return HttpResponse(output)



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


#@csrf_protect
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return render(request, 'registration/success.html')
    form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})



#@login_required()
@login_required(login_url='login')
def post(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            # print form
            book = form.save()
            book.author = request.user
            book.published_date = timezone.now()
            book.save()
            return HttpResponseRedirect('/')
    form = BookForm()
    return render(request, 'booklist/post.html', {'form': form})


































