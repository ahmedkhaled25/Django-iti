from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from pprint import pprint

# Create your views here.
my_task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'Movie-1',
        'priority': 1,
        'description': "action",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Movie-2',
        'priority': 4,
        'description': "thriller",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'Movie-3',
        'priority': 2,
        'description': "drama",
    },
]

def _get_target_task(target_id):
    # Filter the list based on the task id sent and compare it toward each dictionary item in the list
    filter_result = filter(lambda d: d.get('id') == target_id, my_task_list)
    final_list = list(filter_result)
    # Getting index of the required task from my_task_list
    index_of_task = my_task_list.index(final_list[0])
    return index_of_task

def index(request):
     return HttpResponse('Hello world')

def todo_update(request, **kwargs):
    task_id = kwargs.get('task_id')
    index_to_update = _get_target_task(task_id)
    my_task_list[index_to_update]['name'] = 'Updated {}'.format(my_task_list[index_to_update].get('name'))
    return redirect('todo:todo-list')


def todo_delete(request, **kwargs):
    task_id = kwargs.get('task_id')
    index_to_delete = _get_target_task(task_id)
    if my_task_list:
        my_task_list.pop(index_to_delete)
    return redirect('todo:todo-list')

def todo_list(request):
    my_context = {'task_list': my_task_list}
    return render(request, 'lab1/lab1_list.html', context=my_context)


def todo_detail(request, *args, **kwargs):

     task_id = kwargs.get('task_id')
     task_index = _get_target_task(task_id)
     my_task_dictionary = my_task_list[task_index]

     my_context = {
         'task_id': my_task_dictionary.get('id'),
         'task_name': my_task_dictionary.get('name'),
         'task_priority': my_task_dictionary.get('priority'),
         'task_description': my_task_dictionary.get('description')
     }

     return render(request, 'lab1/lab1_detail.html', context=my_context)