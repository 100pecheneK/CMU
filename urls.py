from django.urls import path
from . import views

app_name = 'cmu'
urlpatterns = [
    path('<int:obj_id>/', views.redirect_page, name='redirect_page'),
    path('register_url/', views.register_url, name='register_url'),
]
