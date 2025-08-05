from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

@login_required(login_url='/users/sign_in/')
def notes_list(request):
    user_notes = Note.objects.filter(user_id_id=request.user.id).order_by('-created_at')
    return render(request, 'notes/notes_list.html', {'notes': user_notes})

def note_page(request,id):
    note = Note.objects.get(id=id)
    return render(request, 'notes/note_page.html', {'note': note})

@login_required(login_url="/users/sign_in/")
def note_new(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            newnote = form.save(commit=False)
            newnote.author = request.user
            newnote.save()
            return redirect('notes:list')
    else:
        form = forms.CreatePost()
    return render(request, 'notes/new.html',{'form': form})



