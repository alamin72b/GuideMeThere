from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from django.contrib.auth.views import LoginView, LogoutView

# View to handle user logout with GET method override
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

# View to handle user login
class CustomLoginView(LoginView):
    template_name = 'login/login.html'  # Template for the login page
    fields = '__all__'  # Use all fields of the default User model
    redirect_authenticated_user = True  # Redirect already logged-in users

    # Redirects to the task list upon successful login
    def get_success_url(self):
        return reverse_lazy('tasks')

# View to list all tasks (requires login)
class TaskList(LoginRequiredMixin, ListView):
    model = Task  # Specifies the model to fetch data from
    context_object_name = 'tasks'  # Name of the context variable to access the tasks in the template

# View to display the details of a single task (requires login)
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task  # Specifies the model to fetch data from
    context_object_name = 'task'  # Name of the context variable to access the task in the template

# View to create a new task (requires login)
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task  # Specifies the model to create a new instance
    fields = '__all__'  # Includes all fields of the model in the form
    success_url = reverse_lazy('tasks')  # Redirects to the tasks list page upon successful creation

# View to update an existing task (requires login)
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task  # Specifies the model to update an existing instance
    fields = '__all__'  # Includes all fields of the model in the form
    context_object_name = 'task'  # Name of the context variable to access the task in the template
    success_url = reverse_lazy('tasks')  # Redirects to the tasks list page upon successful update

# View to delete an existing task (requires login)
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task  # Specifies the model to delete an instance
    context_object_name = 'task'  # Name of the context variable to access the task in the template
    success_url = reverse_lazy('tasks')  # Redirects to the task list page after successful deletion
