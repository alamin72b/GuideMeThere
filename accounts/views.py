from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm



def signup_view(request):
    """Handles the user signup process."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signing up
            return redirect('home')  # Redirect to the homepage after successful signup
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage after successful login
            else:
                form.add_error(None, "Username or Password is incorrect")
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def logout_view(request):
    """Logs out the user and redirects to the home page."""
    logout(request)
    return redirect('home')

def home_view(request):
    """A placeholder view for the homepage to ensure URL configurations work correctly."""
    # Assuming there's some template 'home.html' to show after logging in, signing up, or out.
    return render(request, 'home.html')
