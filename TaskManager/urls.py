from django.urls import path
from .views import UserTaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', UserTaskListView.as_view(), name='user_task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]