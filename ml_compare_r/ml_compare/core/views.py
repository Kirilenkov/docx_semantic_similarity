from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from ml_compare.core.models import Document
from ml_compare.core.forms import DocumentForm
from django.http import HttpResponse
from ml_compare.core.ml.single import process_files 
import uuid


def home(request):
    return render(request, 'core/home.html')

def list(request):
    documents = Document.objects.all()
    return render(request, 'core/list.html', { 'documents': documents })

def compare_docs(request):
    # views.py
    if request.method == 'POST':
        # Обработка данных из формы 1
        op1 = request.POST.get('group1')
        # Обработка данных из формы 2
        op2 = request.POST.get('group2')
        fp1,id1 = op1.split('%')
        fp2,id2 = op2.split('%')
        # Дополнительная логика обработки данных
        fn = uuid.uuid1(int(id1), int(id2))
        result_path =  f'media/documents/results/{fn}.xls'
        process_files(f'media/{fp1}', f'media/{fp2}', result_path )
        return HttpResponse(f'Comparing {fp1,id1} with {fp2,id2} result: <a href="{result_path}">result</a>')
    else:
        documents = Document.objects.all()
        return render(request, 'core/compare.html', { 'documents': documents })

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

