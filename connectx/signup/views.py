from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        # Get the form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Create a new UserProfile instance
        user = UserProfile.objects.create(first_name=first_name, last_name=last_name, email=email)

        # Redirect to the user's profile page
        # return redirect('profile', pk=user.pk)
        # print(reverse(profile, kwargs={'pk': user.pk}))

        return redirect(reverse('signup:profile', kwargs={'pk': user.pk}))

    return render(request, 'signup/signup.html')


def profile(request, pk):
    user = UserProfile.objects.get(pk=pk)

    return render(request, 'signup/profile.html', {'user': user})


# def profile(request, pk):
#     user = get_object_or_404(UserProfile, pk=pk)

#     return render(request, 'signup/profile.html', {'user': user})