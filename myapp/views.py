from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .forms import AuthenticationForm
from django.contrib.auth import login, logout

from .forms import MyForm


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def first(request):
    # return HttpResponse("Hey! It's your first view")
    return render(request, 'first.html')


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
        'now': datetime.now(),
    })


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


def form_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            return render(request, 'form_was_valid.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()

    return render(request, 'form.html', {'form': form})


def my_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthenticationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # some actions
            login(request, form.user)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    request.user.is_authenticated
