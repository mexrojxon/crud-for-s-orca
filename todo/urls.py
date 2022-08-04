from django.urls import path
from .views import *

app_name = 's_orca'
urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('post/create/', TodoCreateView.as_view(), name='create'),
    path('post/update/<int:pk>/', TodoUpdateView.as_view(), name='update'),
    path('post/detail/<int:pk>/',TodoDetailView.as_view(), name='detail'),
    path('post/delete/<int:id>/', delete, name='delete')
]

