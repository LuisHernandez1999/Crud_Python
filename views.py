from django.shortcuts import get_object_or_404, render, redirect
from app.forms  import PessoaForm
from app.models import Pessoa
from django.core.paginator import Paginator

from django.shortcuts import render
from app.models import Pessoa
from django.core.paginator import Paginator

def home(request):
    data = {}
    search = request.GET.get('search')
    
    if search:
        pessoas = Pessoa.objects.filter(NomeCompleto__icontains=search)
    else:
        pessoas = Pessoa.objects.all()
    
    paginator = Paginator(pessoas, 2)  #
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    
    data['db'] = page_obj  
    
    return render(request, 'index.html', data)




def form(request):
    data = {}
    data['form'] = PessoaForm()
    return render(request, 'form.html', data)

def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request,pk):
    data = {}
    data['db']=Pessoa.objects.get(pk=pk)
    return render(request,'view.html', data)

def edit(request,pk):
    data = {}
    data['db']=Pessoa.objects.get(pk=pk)
    data['form']=PessoaForm(instance=data['db'])
    return render(request,'form.html', data)

def update(request, pk):
    instance = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PessoaForm(instance=instance)
    return render(request, 'index.hmtl', {'form': form, 'db': instance})

def delete(request, pk):
    db= Pessoa.objects.get(pk=pk)
    db.delete()
    return redirect('home')


