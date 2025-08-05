from django.shortcuts import render
from .models import Note

# Create your views here.

def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/notes_list.html', {'notes': notes})

def note_page(request,id):
    note = Note.objects.get(id=id)
    return render(request, 'notes/note_page.html', {'note': note})

def new_note(request):
    if request.method == 'POST':



