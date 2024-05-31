from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .forms import EditProfileForm

# Create your views here.
#sign up
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.username = user.email
            user.save()
            return redirect('signin')
        else:
            print(form.errors.as_data())
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup-new.html', {'form': form})

#log in
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                request.session[settings.USER_SESSION_ID] = user.id 
                return redirect('home')
            else:
                form.add_error(None, 'Invalid email or password. Please try again!')
                print(form.non_field_errors())
        else:
            print(form.errors.as_data())
    else:
        form = SignInForm()
    return render(request, 'accounts/signin-new.html', {'form': form})
from reservations.models import Booking
from checkout.models import OrderCo

@login_required
def account(request):
    user = request.user  

    get_user = CustomUser.objects.all()   
    bookings = Booking.objects.filter(user=user) 
    order = OrderCo.objects.filter(user=user)
    context = {'get_users': get_user,'bookings': bookings,'orders':order, }
    
    return render(request, 'accounts/account.html', context)


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Chuyển hướng về trang profile sau khi lưu thành công
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'account.html', {'user': user, 'form': form})