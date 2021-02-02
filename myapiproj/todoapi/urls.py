from django.urls import path

from .views import ToDoItemList

urlpatterns = [
    path('todo/', include('todoapi.urls')),
]
