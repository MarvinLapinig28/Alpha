from django.shortcuts import render,redirect,HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache
def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request,'login.html')
@never_cache
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def doLogin(request):
    # Redirect authenticated users to the appropriate page
    if request.user.is_authenticated:
        return redirect('hod_home')  # Replace 'hod_home' with your main page after login

    if request.method == "POST":
        # Authenticate the user using your custom backend
        user = EmailBackEnd.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )

        # If the user is authenticated successfully
        if user is not None:
            login(request, user)
            user_type = user.user_type

            # Redirect based on user type
            if user_type == '1':
                return redirect('hod_home')  # For HOD or admin users
            elif user_type == '2':
                return HttpResponse('This is Staff Panel')  # For staff users
            else:
                messages.error(request, 'Email and Password are Invalid!')
                return redirect('login')
        else:
            # Handle failed authentication
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login')

    # Render the login page for unauthenticated GET requests
    return render(request, 'login.html')  # Replace 'login.html' with your login template


def doLogout(request):
    logout(request)
    return redirect('login')



