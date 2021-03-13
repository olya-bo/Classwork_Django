from django.urls import path

from .views import first, form_view

urlpatterns = [
    path('', first, name='first'),
    # path('form-url/', form_view, name='form-view'),
]
