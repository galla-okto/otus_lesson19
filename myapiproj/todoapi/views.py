from rest_framework.views import APIView

from .models import Author, ToDoItem


class ToDoItemListView(APIView):
    def get(self, request):
        items = ToDoItem.objects.all()
        return items
