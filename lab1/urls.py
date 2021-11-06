from django.urls import path, re_path
from .views import index, todo_list, todo_detail, todo_delete, todo_update

app_name = 'todo'

urlpatterns = [
    path('', index, name='todo-index'),
    path('list', todo_list, name='todo-list'),
    path('task/', todo_detail, name='todo-detail'),

    path('task/<int:task_id>/update', todo_update, name='todo-update'),
    path('task/<int:task_id>/view', todo_detail, name='todo-detail'),
    path('task/<int:task_id>/delete', todo_delete, name='todo-delete')
]