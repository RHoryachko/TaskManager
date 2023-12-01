from django.urls import path
from .views import UserTaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from .views import start_task, complete_task, HashTagTaskListView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', UserTaskListView.as_view(), name='user_task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/start/', start_task, name='start_task'),
    path('task/<int:pk>/complete/', complete_task, name='complete_task'),
    path('tasks/tag/<str:hashtag>/', HashTagTaskListView.as_view(), name='hash_tag_tasks'),
]