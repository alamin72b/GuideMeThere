from django.urls import path
from .views import homePage, TaskDetail, TaskCreate, TaskUpdate, TaskDelete,CustomLoginView

from .views import CustomLogoutView
urlpatterns = [
          # URL for user login
    path('login/', CustomLoginView.as_view(), name='login'),

    # URL for user logout
   path('logout/', CustomLogoutView.as_view(next_page='login'), name='logout'),


    # URL for the list of tasks
    path('', homePage.as_view(), name='tasks'),

    # URL for viewing the details of a specific task
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),

    # URL for creating a new task
    path('create/', TaskCreate.as_view(), name='task-create'),

    # URL for updating an existing task
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),

     path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),


]
