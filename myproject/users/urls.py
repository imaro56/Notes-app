from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    path('sign_up/',views.signup_view, name='sign_up'),
    path('sign_in/',views.signin_view, name='sign_in'),
    path('sign_out/',views.signout_view, name='sign_out'),
]