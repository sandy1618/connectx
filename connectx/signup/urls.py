from django.urls import path
from .views import signup, profile, signin

app_name = 'signup'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('signin/', signin, name='signin')

]
