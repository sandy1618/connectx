from django.urls import path
from .views import signup, profile, signin, admin_page, portfolio_page

app_name = 'signup'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('signin/', signin, name='signin'),
    path('admin/<int:pk>/', admin_page, name='admin'),
    path('portfolio/<int:pk>/', portfolio_page, name='portfolio'),

]
