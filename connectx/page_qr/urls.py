from django.urls import path
from .views import user_links

app_name = 'page_qr'

urlpatterns = [
    path('user_links/', user_links, name='user_links'),
]
