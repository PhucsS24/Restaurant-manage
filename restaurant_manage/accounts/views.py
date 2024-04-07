from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm

# Create your views here.
#sign up
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.username = user.first_name + ' ' + user.last_name
            user.save()
            return redirect('signin')
        else:
            print(form.errors.as_data())
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

#log in
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password. Please try again!')
                print(form.non_field_errors())
        else:
            print(form.errors.as_data())
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})