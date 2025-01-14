# Import necessary modules and classes
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task  # Import the Task model
from django.contrib.auth.views import LoginView, LogoutView

# View to handle user logout with GET method override
class CustomLogoutView(LogoutView):
    """
    Custom LogoutView class to handle user logout. Overrides the default GET method
    to call the POST method, which is responsible for logging the user out.
    This ensures that logging out is handled consistently with the expected behavior.
    """
    def get(self, request, *args, **kwargs):
        # Calls the POST method to log the user out
        return self.post(request, *args, **kwargs)

# View to handle user login
class CustomLoginView(LoginView):
    """
    Custom LoginView class to handle user login.
    - Uses a custom template for the login page.
    - Redirects already authenticated users to the task list page.
    """
    template_name = 'login/login.html'  # Custom template for the login page
    fields = '__all__'  # Use all fields from the default User model in the form
    redirect_authenticated_user = True  # Automatically redirect authenticated users to the task list

    # Redirects to the task list page upon successful login
    def get_success_url(self):
        return reverse_lazy('tasks')  # Redirect to the 'tasks' page after login

# View to list all tasks (requires login)
class homePage(LoginRequiredMixin, ListView):
    """
    View to list all tasks. This is a class-based view that extends ListView.
    It requires the user to be authenticated before displaying the task list.
    """
    model = Task  # Specifies the model from which to fetch data
    context_object_name = 'tasks'  # The context variable name used to access tasks in the template
    template_name = 'login/home.html'  # Updated to point to the correct template

# View to display the details of a single task (requires login)
class TaskDetail(LoginRequiredMixin, DetailView):
    """
    View to display the details of a single task. This is a class-based view that extends DetailView.
    It requires the user to be authenticated before viewing the task details.
    """
    model = Task  # Specifies the model from which to fetch data
    context_object_name = 'task'  # The context variable name used to access the task in the template

# View to create a new task (requires login)
class TaskCreate(LoginRequiredMixin, CreateView):
    """
    View to create a new task. This is a class-based view that extends CreateView.
    It requires the user to be authenticated before creating a new task.
    After successfully creating a task, the user is redirected to the task list.
    """
    model = Task  # Specifies the model to create a new instance of
    fields = '__all__'  # Includes all fields from the model in the form
    success_url = reverse_lazy('tasks')  # Redirects to the tasks list page after successful creation

# View to update an existing task (requires login)
class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
    View to update an existing task. This is a class-based view that extends UpdateView.
    It requires the user to be authenticated before updating a task.
    After a successful update, the user is redirected to the task list.
    """
    model = Task  # Specifies the model to update an existing task
    fields = '__all__'  # Includes all fields from the model in the form
    context_object_name = 'task'  # The context variable name used to access the task in the template
    success_url = reverse_lazy('tasks')  # Redirects to the tasks list page after successful update

# View to delete an existing task (requires login)
class TaskDelete(LoginRequiredMixin, DeleteView):
    """
    View to delete an existing task. This is a class-based view that extends DeleteView.
    It requires the user to be authenticated before deleting a task.
    After successfully deleting a task, the user is redirected to the task list.
    """
    model = Task  # Specifies the model from which to delete a task
    context_object_name = 'task'  # The context variable name used to access the task in the template
    success_url = reverse_lazy('tasks')  # Redirects to the tasks list page after successful deletion
