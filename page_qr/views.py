from django.shortcuts import render
from .models import UserLink

# # Create your views here.


def user_links(request):
    users = UserLink.objects.all()
    return render(request, 'page_qr/user_links.html', {'users': users})



