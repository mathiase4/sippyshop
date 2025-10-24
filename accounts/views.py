from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# view for user registration
def register_view(request):
    """
    Handle user registration,
    Shows registration form and creates new user account.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    

# view for user login
def login_view(request):
    """
    Handle user login,
    Shows login form and logs in existing users.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
        