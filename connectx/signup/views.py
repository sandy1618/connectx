from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        # Get the form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            # Add an error message and redirect to the signup page
            messages.error(request, 'Passwords do not match.')
            return redirect('signup:signup')

        # Create a new UserProfile instance
        user = UserProfile.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=make_password(password),
        )

        # Redirect to the user's profile page
        return redirect(reverse('signup:profile', kwargs={'pk': user.pk}))

    return render(request, 'signup/signup.html')



# def signup(request):
#     if request.method == 'POST':
#         # Get the form data
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')

#         # Create a new UserProfile instance
#         user = UserProfile.objects.create(first_name=first_name, last_name=last_name, email=email)

#         # Redirect to the user's profile page
#         # return redirect('profile', pk=user.pk)
#         # print(reverse(profile, kwargs={'pk': user.pk}))

#         return redirect(reverse('signup:profile', kwargs={'pk': user.pk}))

#     return render(request, 'signup/signup.html')

from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserProfile.objects.get(email=email)
            if check_password(password, user.password):
                return redirect(reverse('signup:profile', kwargs={'pk': user.pk}))
            else:
                messages.error(request, 'Incorrect password.')
                return redirect('signup:signin')
        except UserProfile.DoesNotExist:
            messages.error(request, 'User with this email does not exist. Please sign up.')
            return redirect('signup:signup')
    return render(request, 'signup/signin.html')


def profile(request, pk):
    user = UserProfile.objects.get(pk=pk)

    return render(request, 'signup/profile.html', {'user': user})


# def profile(request, pk):
#     user = get_object_or_404(UserProfile, pk=pk)

#     return render(request, 'signup/profile.html', {'user': user})