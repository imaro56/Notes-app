from django.utils import timezone

from django.shortcuts import render, redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

@login_required(login_url='/users/sign_in/')
def notes_list(request):
    user_notes = Note.objects.filter(user_id=request.user.id).order_by('-updated_at')
    return render(request, 'notes/notes_list.html', {'notes': user_notes})


def note_page(request, id):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            note_to_delete = Note.objects.get(id=id)
            created_at = note_to_delete.created_at
            note_to_delete.delete()

            newnote = form.save(commit=False)
            newnote.user = request.user
            newnote.id = id
            newnote.created_at = created_at
            newnote.updated_at = timezone.now()
            newnote.save()
            return redirect('notes:page', id=newnote.id)
    else:
        form = forms.CreateNote()
        note = Note.objects.get(id=id)
        form.fields['title'].initial = note.title
        form.fields['body'].initial = note.body
    return render(request, 'notes/note_page.html', {'form': form, 'id': id})


@login_required(login_url="/users/sign_in/")
def note_new(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            newnote = form.save(commit=False)
            newnote.user = request.user
            newnote.created_at = timezone.now()
            newnote.updated_at = timezone.now()
            newnote.save()
            return redirect('notes:page', id=newnote.id)
    else:
        form = forms.CreateNote()
    return render(request, 'notes/note_new.html', {'form': form})

def note_delete(request, id):
    if request.method == 'POST':
        Note.objects.get(id=id).delete()
        return redirect('notes:list')
        messages.success(request, 'Note deleted successfully!')
    return redirect('notes:list')