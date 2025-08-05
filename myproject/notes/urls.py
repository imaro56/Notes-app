from django.urls import path
from . import views

app_name='notes'

urlpatterns = [
    path('',views.notes_list, name='list'),
    path('new_note',views.note_new, name='new'),
    path('<int:id>',views.note_page, name='page'),
]