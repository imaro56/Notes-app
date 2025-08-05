from django.urls import path
from . import views

app_name='notes'

urlpatterns = [
    path('',views.notes_list, name='list'),
    path('note_new',views.note_new, name='new'),
    path('<int:id>',views.note_page, name='page'),
]