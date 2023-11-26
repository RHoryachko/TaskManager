from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm



class UserTaskListView(ListView):
    '''Клас відображення тасків'''
    model = Task
    template_name = 'TaskManager/user_task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        '''Метод для повернення тасків користувача'''
        return Task.objects.filter(author_id=self.request.user.id)



class TaskCreateView(CreateView):
    '''Клас створення тасків'''
    model = Task
    form_class = TaskForm
    template_name = 'TaskManager/task_form.html'

    def form_valid(self, form):
        '''Метод збереження форми'''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_task_list')



class TaskUpdateView(UpdateView):
    '''Клас редагування тасків'''
    model = Task
    form_class = TaskForm
    template_name = 'TaskManager/task_form.html'

    def form_valid(self, form):
        '''Метод збереження форми'''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_task_list')



class TaskDeleteView(DeleteView):
    '''Клас видалення тасків'''
    model = Task
    template_name = 'TaskManager/task_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user_task_list')
