from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class UserTaskListView(LoginRequiredMixin, ListView):
    '''Клас відображення тасків'''
    model = Task
    template_name = 'TaskManager/user_task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        '''Метод для повернення тасків користувача'''
        return Task.objects.filter(author_id=self.request.user.id)



class TaskCreateView(LoginRequiredMixin, CreateView):
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



class TaskUpdateView(LoginRequiredMixin, UpdateView):
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



class TaskDeleteView(LoginRequiredMixin, DeleteView):
    '''Клас видалення тасків'''
    model = Task
    template_name = 'TaskManager/task_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('user_task_list')



class HashTagTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'TaskManager/hash_tag_task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        hashtag = self.kwargs['hashtag']
        return Task.objects.filter(author=self.request.user, hashtag=hashtag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hashtag'] = self.kwargs['hashtag']
        return context



@login_required(login_url='accounts/login/')
def start_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'В процесі'
    task.save()

    # Отримуємо попередню сторінку з HTTP-заголовка "Referer"
    # Якщо попередню сторінку не вдалося отримати, повертаємо на 'user_task_list'
    next_page = request.META.get('HTTP_REFERER', None)
    if not next_page:
        next_page = reverse('user_task_list')
    
    return redirect(next_page)



@login_required(login_url='accounts/login/')
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'Виконано'
    task.save()

    # Отримуємо попередню сторінку з HTTP-заголовка "Referer"
    # Якщо попередню сторінку не вдалося отримати, повертаємо на 'user_task_list'
    next_page = request.META.get('HTTP_REFERER', None)
    if not next_page:
        next_page = reverse('user_task_list')
    
    return redirect(next_page)
