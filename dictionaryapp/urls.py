from django.contrib import admin
from django.urls import path, include

from dictionaryapp import views

app_name = 'dictionaryapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dictionary, name="dictionary"),
]
